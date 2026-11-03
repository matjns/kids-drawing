#!/usr/bin/env python3
"""Rasterize the drawing book to PNG so the paths can be checked on Linux.

Reads Sources/DrawingCore/Resources/drawings.json and writes docs/screenshots/.
New strokes are blue. Earlier strokes are grey. That is the same idea as the app.
"""

from __future__ import annotations

import json
import math
import struct
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:  # generate_drawings imports the parser without needing Pillow
    Image = None  # type: ignore
    ImageDraw = None  # type: ignore
    ImageFont = None  # type: ignore

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
JSON_PATH = ROOT / "Sources" / "DrawingCore" / "Resources" / "drawings.json"
OUT = ROOT / "docs" / "screenshots"

PAPER = (251, 246, 236, 255)
INK = (42, 42, 51, 255)
OLD = (186, 180, 170, 255)
NEW = (30, 78, 137, 255)
WHITE = (255, 255, 255, 255)


def parse_path(d: str) -> list[tuple]:
    tokens: list[str] = []
    i = 0
    n = len(d)
    while i < n:
        ch = d[i]
        if ch in " \t\r\n,":
            i += 1
            continue
        if ch in "MLCZmlcz":
            tokens.append(ch.upper())
            i += 1
            continue
        start = i
        if ch in "+-":
            i += 1
        saw_digit = False
        while i < n and d[i].isdigit():
            saw_digit = True
            i += 1
        if i < n and d[i] == ".":
            i += 1
            while i < n and d[i].isdigit():
                saw_digit = True
                i += 1
        if not saw_digit:
            raise ValueError(f"bad path near {d[max(0, start - 8):start + 12]!r}")
        if i < n and d[i] in "eE":
            j = i + 1
            if j < n and d[j] in "+-":
                j += 1
            if j < n and d[j].isdigit():
                i = j + 1
                while i < n and d[i].isdigit():
                    i += 1
        tokens.append(d[start:i])
    cmds: list[tuple] = []
    i = 0
    while i < len(tokens):
        op = tokens[i]
        if op == "M":
            cmds.append(("M", float(tokens[i + 1]), float(tokens[i + 2])))
            i += 3
        elif op == "L":
            cmds.append(("L", float(tokens[i + 1]), float(tokens[i + 2])))
            i += 3
        elif op == "C":
            nums = [float(tokens[i + k]) for k in range(1, 7)]
            cmds.append(("C", *nums))
            i += 7
        elif op == "Z":
            cmds.append(("Z",))
            i += 1
        else:
            raise ValueError(f"unsupported command {op} in {d[:80]}")
    return cmds


def _mid(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float]:
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)


def _dist_to_seg(p: tuple[float, float], a: tuple[float, float], d: tuple[float, float]) -> float:
    vx, vy = d[0] - a[0], d[1] - a[1]
    l2 = vx * vx + vy * vy
    if l2 < 1e-8:
        return math.hypot(p[0] - a[0], p[1] - a[1])
    t = max(0.0, min(1.0, ((p[0] - a[0]) * vx + (p[1] - a[1]) * vy) / l2))
    return math.hypot(p[0] - (a[0] + t * vx), p[1] - (a[1] + t * vy))


def flatten_cubic(
    p0: tuple[float, float],
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    tol: float = 0.35,
) -> list[tuple[float, float]]:
    out = [p0]

    def rec(a, b, c, d, depth: int) -> None:
        if depth > 14 or (_dist_to_seg(b, a, d) <= tol and _dist_to_seg(c, a, d) <= tol):
            out.append(d)
            return
        ab, bc, cd = _mid(a, b), _mid(b, c), _mid(c, d)
        abbc, bccd = _mid(ab, bc), _mid(bc, cd)
        mid = _mid(abbc, bccd)
        rec(a, ab, abbc, mid, depth + 1)
        rec(mid, bccd, cd, d, depth + 1)

    rec(p0, p1, p2, p3, 0)
    return out


def polylines(cmds: list[tuple], tol: float = 0.35) -> list[list[tuple[float, float]]]:
    subs: list[list[tuple[float, float]]] = []
    cur: tuple[float, float] | None = None
    start: tuple[float, float] | None = None
    pts: list[tuple[float, float]] = []

    def flush() -> None:
        nonlocal pts
        if len(pts) >= 2:
            subs.append(pts)
        pts = []

    for cmd in cmds:
        if cmd[0] == "M":
            flush()
            cur = (cmd[1], cmd[2])
            start = cur
            pts = [cur]
        elif cmd[0] == "L":
            cur = (cmd[1], cmd[2])
            pts.append(cur)
        elif cmd[0] == "C":
            if cur is None:
                cur = (0.0, 0.0)
            p1 = (cmd[1], cmd[2])
            p2 = (cmd[3], cmd[4])
            p3 = (cmd[5], cmd[6])
            seg = flatten_cubic(cur, p1, p2, p3, tol)
            pts.extend(seg[1:])
            cur = p3
        elif cmd[0] == "Z":
            if start is not None and cur != start:
                pts.append(start)
            cur = start
            flush()
    flush()
    return subs


def bounds_of(subject: dict) -> tuple[float, float, float, float]:
    xs: list[float] = []
    ys: list[float] = []
    for draw_step in subject["steps"]:
        for stroke in draw_step["strokes"]:
            for sub in polylines(parse_path(stroke["d"])):
                for x, y in sub:
                    xs.append(x)
                    ys.append(y)
    return min(xs), min(ys), max(xs), max(ys)


def _disk(radius: int) -> list[tuple[int, int]]:
    r2 = radius * radius
    pts = []
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            if x * x + y * y <= r2:
                pts.append((x, y))
    return pts


_DISKS: dict[int, list[tuple[int, int]]] = {}


def stamp(buf: bytearray, w: int, h: int, x: float, y: float, radius: float, color: tuple[int, int, int, int]) -> None:
    ri = max(1, int(round(radius)))
    disk = _DISKS.get(ri)
    if disk is None:
        disk = _disk(ri)
        _DISKS[ri] = disk
    cx, cy = int(round(x)), int(round(y))
    cr, cg, cb, ca = color
    for dx, dy in disk:
        px, py = cx + dx, cy + dy
        if 0 <= px < w and 0 <= py < h:
            i = (py * w + px) * 4
            buf[i : i + 4] = bytes((cr, cg, cb, ca))


def stroke_poly(
    buf: bytearray,
    w: int,
    h: int,
    pts: list[tuple[float, float]],
    radius: float,
    color: tuple[int, int, int, int],
) -> None:
    if len(pts) < 2:
        if pts:
            stamp(buf, w, h, pts[0][0], pts[0][1], radius, color)
        return
    step = max(0.8, radius * 0.45)
    stamp(buf, w, h, pts[0][0], pts[0][1], radius, color)
    px, py = pts[0]
    for x, y in pts[1:]:
        dist = math.hypot(x - px, y - py)
        count = max(1, int(dist / step))
        for s in range(1, count + 1):
            t = s / count
            stamp(buf, w, h, px + (x - px) * t, py + (y - py) * t, radius, color)
        px, py = x, y


def fill_poly(buf: bytearray, w: int, h: int, pts: list[tuple[float, float]], color: tuple[int, int, int, int]) -> None:
    if len(pts) < 3:
        return
    ys = [p[1] for p in pts]
    y0 = max(0, int(math.floor(min(ys))))
    y1 = min(h - 1, int(math.ceil(max(ys))))
    cr, cg, cb, ca = color
    packed = bytes((cr, cg, cb, ca))
    n = len(pts)
    for y in range(y0, y1 + 1):
        yscan = y + 0.5
        xs: list[float] = []
        for i in range(n):
            x1, y1 = pts[i]
            x2, y2 = pts[(i + 1) % n]
            if y1 == y2:
                continue
            if (y1 <= yscan < y2) or (y2 <= yscan < y1):
                t = (yscan - y1) / (y2 - y1)
                xs.append(x1 + t * (x2 - x1))
        xs.sort()
        row = y * w * 4
        pair = 0
        while pair + 1 < len(xs):
            xa = max(0, int(math.ceil(xs[pair])))
            xb = min(w - 1, int(math.floor(xs[pair + 1])))
            for x in range(xa, xb + 1):
                buf[row + x * 4 : row + x * 4 + 4] = packed
            pair += 2


def render_subject(
    subject: dict,
    size: int = 480,
    step_index: int | None = None,
    highlight: bool = False,
    background: tuple[int, int, int, int] = WHITE,
) -> Image.Image:
    """step_index None draws every stroke. highlight paints earlier steps grey."""
    vb = subject.get("viewBox", [0, 0, 200, 200])
    min_x, min_y, vw, vh = vb
    pad = size * 0.08
    scale = (size - 2 * pad) / max(vw, vh)
    ox = (size - vw * scale) / 2 - min_x * scale
    oy = (size - vh * scale) / 2 - min_y * scale
    ss = 2
    W, H = size * ss, size * ss
    buf = bytearray(background * (W * H))

    def map_pt(x: float, y: float) -> tuple[float, float]:
        return ((ox + x * scale) * ss, (oy + y * scale) * ss)

    steps = subject["steps"]
    last = len(steps) - 1 if step_index is None else step_index
    for index, draw_step in enumerate(steps):
        if index > last:
            break
        if highlight and step_index is not None and index < step_index:
            color = OLD
        elif highlight and step_index is not None and index == step_index:
            color = NEW
        else:
            color = INK
        for stroke in draw_step["strokes"]:
            width = float(stroke.get("width", 4.6)) * scale * ss
            for sub in polylines(parse_path(stroke["d"]), tol=0.45):
                mapped = [map_pt(x, y) for x, y in sub]
                if stroke.get("fill"):
                    fill_poly(buf, W, H, mapped, color)
                else:
                    stroke_poly(buf, W, H, mapped, max(1.0, width / 2), color)
    raw = bytes(buf)
    big = Image.frombytes("RGBA", (W, H), raw)
    return big.resize((size, size), Image.Resampling.LANCZOS)


def font(size: int) -> ImageFont.ImageFont:
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ):
        if Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


def font_bold(size: int) -> ImageFont.ImageFont:
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ):
        if Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return font(size)


CATEGORY_TITLES = {
    "animals": "Animals",
    "fantasy": "Fantasy",
    "vehicles": "Vehicles",
    "food": "Food",
    "nature": "Nature",
    "space": "Space",
    "buildings": "Buildings",
    "everyday": "Everyday Things",
}


def contact_sheet(subjects: list[dict], title: str, path: Path, columns: int = 5) -> None:
    cell = 220
    label_h = 36
    header = 64
    rows = math.ceil(len(subjects) / columns)
    width = columns * cell + 24
    height = header + rows * (cell + label_h) + 16
    sheet = Image.new("RGBA", (width, height), PAPER)
    draw = ImageDraw.Draw(sheet)
    draw.text((20, 16), title, fill=INK[:3], font=font_bold(28))
    for i, subject in enumerate(subjects):
        col = i % columns
        row = i // columns
        x = 12 + col * cell
        y = header + row * (cell + label_h)
        art = render_subject(subject, size=cell - 16)
        sheet.paste(art, (x + 8, y), art)
        draw.text((x + 10, y + cell - 12), subject["title"], fill=INK[:3], font=font(18))
    sheet.convert("RGB").save(path, "PNG")
    print(f"wrote {path.relative_to(ROOT)}")


def step_strip(subject: dict, path: Path) -> None:
    panel = 280
    steps = subject["steps"]
    count = len(steps) + 1
    header = 78
    caption = 64
    width = count * panel + 20
    height = header + panel + caption
    sheet = Image.new("RGBA", (width, height), PAPER)
    draw = ImageDraw.Draw(sheet)
    draw.text((16, 12), subject["title"], fill=INK[:3], font=font_bold(28))
    draw.text(
        (16, 46),
        "Blue lines are the new ones. Grey lines are already drawn.",
        fill=(60, 60, 70),
        font=font(16),
    )
    for i in range(len(steps)):
        art = render_subject(subject, size=panel - 24, step_index=i, highlight=True)
        x = 10 + i * panel
        sheet.paste(art, (x + 12, header), art)
        draw.text((x + 16, header + panel - 28), f"Step {i + 1}", fill=NEW[:3], font=font_bold(16))
    art = render_subject(subject, size=panel - 24, highlight=False)
    x = 10 + len(steps) * panel
    sheet.paste(art, (x + 12, header), art)
    draw.text((x + 16, header + panel - 28), "Finished", fill=INK[:3], font=font_bold(16))
    sheet.convert("RGB").save(path, "PNG")
    print(f"wrote {path.relative_to(ROOT)}")


def save_one(subject: dict, path: Path, size: int = 640) -> None:
    render_subject(subject, size=size).convert("RGB").save(path, "PNG")
    print(f"wrote {path.relative_to(ROOT)}")


def rounded_mask(size: int, radius: int) -> Image.Image:
    mask = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle((0, 0, size - 1, size - 1), radius=radius, fill=255)
    return mask


def draw_icon(path: Path) -> None:
    """A pencil on warm paper. Readable at dock size."""
    size = 1024
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, size - 1, size - 1), radius=220, fill=(244, 162, 97, 255))
    d.rounded_rectangle((70, 70, size - 71, size - 71), radius=170, fill=(255, 250, 242, 255))
    # Pencil body, diagonal.
    body = [(250, 760), (690, 250), (790, 340), (350, 850)]
    d.polygon(body, fill=(244, 208, 96, 255), outline=(42, 42, 51, 255))
    # The polygon outline from PIL is thin. Stroke by drawing a slightly larger ink polygon first.
    # Tip
    d.polygon([(690, 250), (860, 150), (790, 340)], fill=(244, 232, 208, 255), outline=(42, 42, 51, 255))
    d.polygon([(760, 210), (860, 150), (800, 250)], fill=(42, 42, 51, 255))
    # Eraser
    d.polygon([(250, 760), (350, 850), (230, 930), (140, 820)], fill=(224, 112, 96, 255), outline=(42, 42, 51, 255))
    d.line([(250, 760), (350, 850)], fill=(42, 42, 51, 255), width=28)
    # Band
    d.line([(300, 700), (400, 790)], fill=(196, 144, 90, 255), width=36)
    # Star
    star_pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        r = 70 if i % 2 == 0 else 30
        star_pts.append((230 + r * math.cos(ang), 250 + r * math.sin(ang)))
    d.polygon(star_pts, fill=(30, 78, 137, 255))
    img.save(path, "PNG")
    print(f"wrote {path.relative_to(ROOT)}")
    write_icns(img, ROOT / "Config" / "AppIcon.icns")


def write_icns(img: Image.Image, path: Path) -> None:
    """PNG-based icns (ic07 128, ic08 256, ic09 512, ic10 1024, ic11 32@2x, ic12 16@2x)."""
    specs = [
        (b"ic12", 32),
        (b"ic11", 64),
        (b"ic07", 128),
        (b"ic08", 256),
        (b"ic09", 512),
        (b"ic10", 1024),
    ]
    chunks: list[bytes] = []
    for ostype, side in specs:
        resized = img.resize((side, side), Image.Resampling.LANCZOS)
        # Flatten onto the apricot background so the corners stay opaque in the dock.
        bg = Image.new("RGBA", (side, side), (244, 162, 97, 255))
        bg.alpha_composite(resized)
        import io

        blob_io = io.BytesIO()
        bg.convert("RGB").save(blob_io, format="PNG")
        data = blob_io.getvalue()
        chunks.append(ostype + struct.pack(">I", len(data) + 8) + data)
    body = b"".join(chunks)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"icns" + struct.pack(">I", len(body) + 8) + body)
    print(f"wrote {path.relative_to(ROOT)}")


def load_book() -> list[dict]:
    payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    return payload["subjects"]


def main() -> None:
    if Image is None:
        raise SystemExit("Install Pillow to render previews: pip install pillow")
    subjects = load_book()
    by_id = {s["id"]: s for s in subjects}
    OUT.mkdir(parents=True, exist_ok=True)
    groups: dict[str, list[dict]] = {}
    for subject in subjects:
        groups.setdefault(subject["category"], []).append(subject)
    for category, items in groups.items():
        contact_sheet(items, CATEGORY_TITLES.get(category, category), OUT / f"contact-{category}.png")
    for sid in ("cat", "dog", "dragon", "unicorn", "rocket", "house", "dinosaur", "bicycle"):
        save_one(by_id[sid], OUT / f"{sid}.png", size=720)
    step_strip(by_id["cat"], OUT / "cat-steps.png")
    step_strip(by_id["dragon"], OUT / "dragon-steps.png")
    step_strip(by_id["rocket"], OUT / "rocket-steps.png")
    draw_icon(ROOT / "Config" / "AppIcon-1024.png")


if __name__ == "__main__":
    main()
