"""Small helpers for kid-copyable pen drawings.

Coordinates are a 200 by 200 sketchbook page. Y grows downward, same as SVG.
Paths use only absolute M, L, C, and Z so the Mac app and the preview renderer
agree. Strokes stay on the page: the finished picture is every step added up,
with nothing erased.
"""

from __future__ import annotations

import math

W = 4.6
THIN = 3.1
KAPPA = 0.5522847498


def _n(v: float) -> str:
    v = round(float(v), 2)
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    text = f"{v:.2f}".rstrip("0").rstrip(".")
    return text


class Path:
    def __init__(self) -> None:
        self.parts: list[str] = []

    def M(self, x: float, y: float) -> "Path":
        self.parts.append(f"M {_n(x)} {_n(y)}")
        return self

    def L(self, x: float, y: float) -> "Path":
        self.parts.append(f"L {_n(x)} {_n(y)}")
        return self

    def C(self, x1: float, y1: float, x2: float, y2: float, x: float, y: float) -> "Path":
        self.parts.append(
            f"C {_n(x1)} {_n(y1)} {_n(x2)} {_n(y2)} {_n(x)} {_n(y)}"
        )
        return self

    def Z(self) -> "Path":
        self.parts.append("Z")
        return self

    def poly(self, pts: list[tuple[float, float]], close: bool = False) -> "Path":
        x0, y0 = pts[0]
        self.M(x0, y0)
        for x, y in pts[1:]:
            self.L(x, y)
        if close:
            self.Z()
        return self

    def circle(self, cx: float, cy: float, r: float) -> "Path":
        return self.ellipse(cx, cy, r, r)

    def ellipse(self, cx: float, cy: float, rx: float, ry: float) -> "Path":
        kx = KAPPA * rx
        ky = KAPPA * ry
        self.M(cx, cy - ry)
        self.C(cx + kx, cy - ry, cx + rx, cy - ky, cx + rx, cy)
        self.C(cx + rx, cy + ky, cx + kx, cy + ry, cx, cy + ry)
        self.C(cx - kx, cy + ry, cx - rx, cy + ky, cx - rx, cy)
        self.C(cx - rx, cy - ky, cx - kx, cy - ry, cx, cy - ry)
        self.Z()
        return self

    def round_rect(self, x: float, y: float, w: float, h: float, r: float) -> "Path":
        r = max(0.0, min(r, w / 2, h / 2))
        k = KAPPA * r
        self.M(x + r, y)
        self.L(x + w - r, y)
        self.C(x + w - r + k, y, x + w, y + r - k, x + w, y + r)
        self.L(x + w, y + h - r)
        self.C(x + w, y + h - r + k, x + w - r + k, y + h, x + w - r, y + h)
        self.L(x + r, y + h)
        self.C(x + r - k, y + h, x, y + h - r + k, x, y + h - r)
        self.L(x, y + r)
        self.C(x, y + r - k, x + r - k, y, x + r, y)
        self.Z()
        return self

    def q(self, x0: float, y0: float, cx: float, cy: float, x1: float, y1: float) -> "Path":
        """Quadratic curve, stored as a cubic. Includes the starting move."""
        c1x = x0 + 2 / 3 * (cx - x0)
        c1y = y0 + 2 / 3 * (cy - y0)
        c2x = x1 + 2 / 3 * (cx - x1)
        c2y = y1 + 2 / 3 * (cy - y1)
        self.M(x0, y0)
        self.C(c1x, c1y, c2x, c2y, x1, y1)
        return self

    def arc(self, cx: float, cy: float, rx: float, ry: float, a0: float, a1: float) -> "Path":
        """Elliptical arc. 0° is east, and degrees increase clockwise because Y is down."""
        sweep = a1 - a0
        if abs(sweep) < 0.01 or rx <= 0 or ry <= 0:
            return self
        segs = max(1, int(math.ceil(abs(sweep) / 90.0)))
        delta = sweep / segs

        def pt(deg: float) -> tuple[float, float]:
            rad = math.radians(deg)
            return (cx + rx * math.cos(rad), cy + ry * math.sin(rad))

        def deriv(deg: float) -> tuple[float, float]:
            rad = math.radians(deg)
            return (-rx * math.sin(rad), ry * math.cos(rad))

        x, y = pt(a0)
        self.M(x, y)
        for i in range(segs):
            a_start = a0 + delta * i
            a_end = a_start + delta
            alpha = (4.0 / 3.0) * math.tan(math.radians(delta) / 4.0)
            p0 = pt(a_start)
            p3 = pt(a_end)
            d0 = deriv(a_start)
            d3 = deriv(a_end)
            c1 = (p0[0] + alpha * d0[0], p0[1] + alpha * d0[1])
            c2 = (p3[0] - alpha * d3[0], p3[1] - alpha * d3[1])
            self.C(*c1, *c2, *p3)
        return self

    def text(self) -> str:
        return " ".join(self.parts)


def circ(cx: float, cy: float, r: float) -> str:
    return Path().circle(cx, cy, r).text()


def ell(cx: float, cy: float, rx: float, ry: float) -> str:
    return Path().ellipse(cx, cy, rx, ry).text()


def ln(x1: float, y1: float, x2: float, y2: float) -> str:
    return Path().M(x1, y1).L(x2, y2).text()


def pg(pts: list[tuple[float, float]], close: bool = False) -> str:
    return Path().poly(pts, close=close).text()


def rr(x: float, y: float, w: float, h: float, r: float) -> str:
    return Path().round_rect(x, y, w, h, r).text()


def curve(x0: float, y0: float, cx: float, cy: float, x1: float, y1: float) -> str:
    return Path().q(x0, y0, cx, cy, x1, y1).text()


def arc(cx: float, cy: float, rx: float, ry: float, a0: float, a1: float) -> str:
    return Path().arc(cx, cy, rx, ry, a0, a1).text()


def smooth(points: list[tuple[float, float]]) -> str:
    """Open curve through points (Catmull-Rom converted to cubics)."""
    if len(points) < 2:
        return ""
    p = Path()
    p.M(*points[0])
    n = len(points)
    for i in range(n - 1):
        p0 = points[i - 1] if i > 0 else points[0]
        p1 = points[i]
        p2 = points[i + 1]
        p3 = points[i + 2] if i + 2 < n else points[-1]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6.0, p1[1] + (p2[1] - p0[1]) / 6.0)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6.0, p2[1] - (p3[1] - p1[1]) / 6.0)
        p.C(c1[0], c1[1], c2[0], c2[1], p2[0], p2[1])
    return p.text()


def spiral(cx: float, cy: float, r0: float, r1: float, turns: float, a0: float = 0.0, samples: int = 36) -> str:
    pts = []
    total = turns * 2 * math.pi
    for i in range(samples + 1):
        t = i / samples
        ang = a0 + t * total
        rad = r0 + (r1 - r0) * t
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    return Path().poly(pts, close=False).text()


def star(cx: float, cy: float, r_out: float, r_in: float, n: int = 5) -> str:
    pts = []
    for i in range(n * 2):
        ang = math.radians(-90 + i * 180 / n)
        r = r_out if i % 2 == 0 else r_in
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return Path().poly(pts, close=True).text()


def heart(cx: float, cy: float, w: float, h: float) -> str:
    left = cx - w / 2
    right = cx + w / 2
    top = cy - h / 2
    bot = cy + h / 2
    p = Path()
    p.M(cx, bot)
    p.C(cx - w * 0.05, bot - h * 0.22, left, cy + h * 0.12, left + w * 0.02, top + h * 0.32)
    p.C(left - w * 0.02, top + h * 0.08, cx - w * 0.08, top, cx, top + h * 0.22)
    p.C(cx + w * 0.08, top, right + w * 0.02, top + h * 0.08, right - w * 0.02, top + h * 0.32)
    p.C(right, cy + h * 0.12, cx + w * 0.05, bot - h * 0.22, cx, bot)
    p.Z()
    return p.text()


def leaf(cx: float, cy: float, w: float, h: float) -> str:
    p = Path()
    p.M(cx, cy - h / 2)
    p.C(cx + w * 0.62, cy - h * 0.18, cx + w * 0.48, cy + h * 0.28, cx, cy + h / 2)
    p.C(cx - w * 0.48, cy + h * 0.28, cx - w * 0.62, cy - h * 0.18, cx, cy - h / 2)
    p.Z()
    return p.text()


def flame(cx: float, top: float, h: float, w: float) -> str:
    p = Path()
    p.M(cx, top + h)
    p.C(cx - w, top + h * 0.62, cx - w * 0.45, top + h * 0.18, cx, top)
    p.C(cx + w * 0.45, top + h * 0.18, cx + w, top + h * 0.62, cx, top + h)
    p.Z()
    return p.text()


def ink(d: str, width: float = W, fill: bool = False) -> dict:
    return {"d": d, "width": width, "fill": fill}


def step(instruction: str, *strokes: dict | list | None) -> dict:
    flat: list[dict] = []
    for item in strokes:
        if item is None:
            continue
        if isinstance(item, list):
            flat.extend(item)
        else:
            flat.append(item)
    if not flat:
        raise ValueError(f"step has no strokes: {instruction}")
    return {"instruction": instruction, "strokes": flat}


def subject(sid: str, title: str, category: str, words: list[str], steps: list[dict]) -> dict:
    return {
        "id": sid,
        "title": title,
        "category": category,
        "words": words,
        "viewBox": [0, 0, 200, 200],
        "steps": steps,
    }


def eyes(x: float, y: float, gap: float = 22, r: float = 7.2, pupil: float = 3.1) -> list[dict]:
    return [
        ink(circ(x - gap / 2, y, r), width=THIN),
        ink(circ(x + gap / 2, y, r), width=THIN),
        ink(circ(x - gap / 2 + 1.2, y + 0.6, pupil), width=2, fill=True),
        ink(circ(x + gap / 2 + 1.2, y + 0.6, pupil), width=2, fill=True),
    ]


def dot_eyes(x: float, y: float, gap: float = 18, r: float = 3.3) -> list[dict]:
    return [
        ink(circ(x - gap / 2, y, r), width=2, fill=True),
        ink(circ(x + gap / 2, y, r), width=2, fill=True),
    ]


def smile(x: float, y: float, w: float = 22, drop: float = 12, width: float = THIN) -> dict:
    return ink(curve(x - w / 2, y, x, y + drop, x + w / 2, y), width=width)


def nose(x: float, y: float, r: float = 2.6) -> dict:
    return ink(circ(x, y, r), width=2, fill=True)


def wheel(cx: float, cy: float, r: float) -> list[dict]:
    return [
        ink(circ(cx, cy, r)),
        ink(circ(cx, cy, r * 0.38), width=THIN),
    ]


def window(x: float, y: float, s: float) -> list[dict]:
    return [
        ink(rr(x, y, s, s, 2), width=THIN),
        ink(ln(x + s / 2, y, x + s / 2, y + s), width=THIN),
        ink(ln(x, y + s / 2, x + s, y + s / 2), width=THIN),
    ]


def lines(pairs: list[tuple[float, float, float, float]], width: float = THIN) -> list[dict]:
    return [ink(ln(a, b, c, d), width=width) for a, b, c, d in pairs]
