#!/usr/bin/env python3
"""Developer helper: render chosen subjects (finished + step strip) for a visual check.

python3 tools/review.py [--out=PATH] [--steps] whale cat dog
(default output: /tmp/review.png)
"""
from __future__ import annotations
import sys, importlib
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import generate_drawings as g
from render_previews import render_subject, font, PAPER, INK
from PIL import Image, ImageDraw

def main() -> None:
    args = sys.argv[1:]
    out = "/tmp/review.png"
    if args and args[0].startswith("--out="):
        out = args.pop(0)[6:]
    steps = False
    if args and args[0] == "--steps":
        steps = True
        args.pop(0)
    subjects = {s["id"]: s for s in g.collect()}
    ids = args or list(subjects)
    cell = 300
    if steps:
        rows = []
        for sid in ids:
            s = subjects[sid]
            n = len(s["steps"])
            row = Image.new("RGBA", ((n + 1) * 200, 230), PAPER)
            d = ImageDraw.Draw(row)
            for i in range(n):
                art = render_subject(s, size=200, step_index=i, highlight=True)
                row.paste(art, (i * 200, 0), art)
                d.text((i * 200 + 6, 204), f"{i+1}", fill=INK[:3], font=font(16))
            art = render_subject(s, size=200)
            row.paste(art, (n * 200, 0), art)
            d.text((n * 200 + 6, 204), sid, fill=INK[:3], font=font(16))
            rows.append(row)
        W = max(r.width for r in rows); H = sum(r.height for r in rows)
        sheet = Image.new("RGB", (W, H), PAPER[:3]); y = 0
        for r in rows:
            sheet.paste(r, (0, y), r); y += r.height
    else:
        cols = min(4, len(ids)); rows_n = (len(ids) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * cell, rows_n * (cell + 24)), PAPER[:3])
        d = ImageDraw.Draw(sheet)
        for i, sid in enumerate(ids):
            art = render_subject(subjects[sid], size=cell)
            x, y = (i % cols) * cell, (i // cols) * (cell + 24)
            sheet.paste(art, (x, y), art)
            d.text((x + 8, y + cell), sid, fill=INK[:3], font=font(18))
    sheet.save(out)
    print(out)

if __name__ == "__main__":
    main()
