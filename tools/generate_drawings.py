#!/usr/bin/env python3
"""Build the offline drawing book (Sources/DrawingCore/Resources/drawings.json).

The JSON file is what the app ships. Edit the subject modules in this folder,
then run this script again. See docs/DRAWING_FORMAT.md.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "Sources" / "DrawingCore" / "Resources" / "drawings.json"

sys.path.insert(0, str(HERE))

from subjects_animals import all_subjects as animals  # noqa: E402
from subjects_buildings import all_subjects as buildings  # noqa: E402
from subjects_everyday import all_subjects as everyday  # noqa: E402
from subjects_fantasy import all_subjects as fantasy  # noqa: E402
from subjects_food import all_subjects as food  # noqa: E402
from subjects_nature import all_subjects as nature  # noqa: E402
from subjects_space import all_subjects as space  # noqa: E402
from subjects_vehicles import all_subjects as vehicles  # noqa: E402
from render_previews import bounds_of, parse_path  # noqa: E402


CATEGORIES = ["animals", "fantasy", "vehicles", "food", "nature", "space", "buildings", "everyday"]


def normalize(raw: str) -> str:
    out: list[str] = []
    spaced = False
    for ch in raw.lower():
        if ch.isalpha() or ch.isdigit():
            out.append(ch)
            spaced = False
        elif ch in "'’":
            continue
        else:
            if out and not spaced:
                out.append(" ")
                spaced = True
    return "".join(out).strip()


def collect() -> list[dict]:
    subjects: list[dict] = []
    for batch in (animals(), fantasy(), vehicles(), food(), nature(), space(), buildings(), everyday()):
        subjects.extend(batch)
    return subjects


def validate(subjects: list[dict]) -> None:
    if len(subjects) < 60:
        raise SystemExit(f"need at least 60 subjects, found {len(subjects)}")
    ids: set[str] = set()
    alias_owner: dict[str, str] = {}
    for subject in subjects:
        sid = subject["id"]
        if sid in ids:
            raise SystemExit(f"duplicate id {sid}")
        ids.add(sid)
        if subject["category"] not in CATEGORIES:
            raise SystemExit(f"{sid} has unknown category {subject['category']}")
        if len(subject["steps"]) < 3:
            raise SystemExit(f"{sid} needs at least 3 steps")
        names = [sid, subject["title"], *subject["words"]]
        for name in names:
            key = normalize(name)
            if not key:
                raise SystemExit(f"{sid} has an empty word")
            other = alias_owner.get(key)
            if other is not None and other != sid:
                raise SystemExit(f"word {key!r} belongs to both {other} and {sid}")
            alias_owner[key] = sid
        for index, draw_step in enumerate(subject["steps"], start=1):
            text = draw_step["instruction"].strip()
            if len(text) < 12:
                raise SystemExit(f"{sid} step {index} instruction is too short")
            if "http" in text.lower() or "www." in text.lower():
                raise SystemExit(f"{sid} step {index} has a link")
            if not draw_step["strokes"]:
                raise SystemExit(f"{sid} step {index} has no strokes")
            for stroke in draw_step["strokes"]:
                parse_path(stroke["d"])
        min_x, min_y, max_x, max_y = bounds_of(subject)
        if min_x < -8 or min_y < -8 or max_x > 208 or max_y > 208:
            print(
                f"warning: {sid} bounds ({min_x:.1f}, {min_y:.1f})-({max_x:.1f}, {max_y:.1f})",
                file=sys.stderr,
            )


def main() -> None:
    subjects = collect()
    validate(subjects)
    payload = {"formatVersion": 1, "subjects": subjects}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    counts: dict[str, int] = {}
    for subject in subjects:
        counts[subject["category"]] = counts.get(subject["category"], 0) + 1
    print(f"wrote {len(subjects)} subjects to {OUT.relative_to(ROOT)}")
    for name in CATEGORIES:
        print(f"  {name}: {counts.get(name, 0)}")


if __name__ == "__main__":
    main()
