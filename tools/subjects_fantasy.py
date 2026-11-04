"""Dragon, unicorn, crown, and a magic wand."""

from shapes import THIN, W, Path, circ, curve, ell, ink, lines, ln, pg, rr, smile, sp, star, step, subject, smooth
from subjects_animals import dot, horse_body


def all_subjects() -> list[dict]:
    return [dragon(), unicorn(), crown(), wand()]


def dragon() -> dict:
    return subject(
        "dragon",
        "Dragon",
        "fantasy",
        ["dragon", "dragons", "dragin"],
        [
            step(
                "Draw the head facing left, with a long snout, and two horns curving back.",
                ink(sp([(56, 44), (44, 36), (28, 38), (14, 46), (10, 56, 1), (24, 60), (44, 62), (56, 58)],
                       closed=True)),
                ink(sp([(50, 40), (60, 26), (72, 18, 1)]), width=THIN),
                ink(sp([(44, 37), (50, 24), (58, 16, 1)]), width=THIN),
            ),
            step(
                "Draw a long neck down to the body, then a long tail with a pointy end.",
                ink(sp([(56, 46), (70, 60), (86, 84), (112, 94), (142, 98), (166, 108), (184, 128),
                        (190, 150, 1)])),
                ink(sp([(190, 150), (176, 136), (158, 126), (140, 130)])),
                ink(sp([(52, 62), (60, 84), (74, 110), (92, 126), (112, 132)])),
                ink(sp([(186, 146), (180, 164, 1), (194, 160, 1), (191, 144)]), width=THIN),
            ),
            step(
                "Draw a big bat wing on the back. The bottom edge has curvy points.",
                ink(sp([(100, 92), (108, 60), (128, 24, 1), (150, 28), (176, 34, 1), (166, 52), (170, 70, 1),
                        (152, 70), (152, 88, 1), (138, 86), (132, 97)])),
                ink(sp([(128, 26), (142, 50), (152, 70)]), width=2.4),
                ink(sp([(128, 26), (150, 40), (170, 68)]), width=2.4),
            ),
            step(
                "Add a front leg and a big strong back leg, both with claws.",
                ink(sp([(76, 114), (70, 140), (66, 160), (56, 168, 1), (80, 168, 1), (78, 156), (86, 134),
                        (92, 126)])),
                ink(sp([(118, 132), (114, 150), (120, 162), (116, 170), (104, 178, 1), (134, 178, 1), (130, 166),
                        (138, 148), (146, 128)])),
                lines([(58, 168, 56, 172), (66, 168, 65, 172), (74, 168, 74, 172), (108, 178, 106, 182),
                       (118, 178, 117, 182), (128, 178, 128, 182)], width=2),
            ),
            step(
                "Finish with an eye, a nostril, and little spikes down the neck and back.",
                dot(36, 46, 3),
                dot(15, 50, 1.6),
                ink(sp([(62, 52), (70, 44, 1), (72, 58), (82, 54, 1), (82, 72), (94, 70, 1), (96, 88)]), width=THIN),
                ink(sp([(150, 100), (160, 92, 1), (164, 104), (176, 100, 1), (176, 116)]), width=THIN),
            ),
        ],
    )


def unicorn() -> dict:
    return subject(
        "unicorn",
        "Unicorn",
        "fantasy",
        ["unicorn", "unicorns", "unicron"],
        horse_body()
        + [
            step(
                "Add a long pointy horn on the forehead with a spiral, then an eye and a nostril.",
                ink(sp([(39, 42), (30, 10, 1), (48, 37)])),
                lines([(36, 34, 42, 32), (34, 26, 40, 24), (33, 19, 37, 18)], width=2),
                dot(37, 52, 3),
                ink(sp([(19, 75), (22, 72), (24, 76)]), width=2.4),
            ),
        ],
    )


def crown() -> dict:
    return subject(
        "crown",
        "Crown",
        "fantasy",
        ["crown", "crowns", "tiara"],
        [
            step("Draw the base band.", ink(rr(36, 112, 128, 36, 6))),
            step(
                "Add three tall points.",
                ink(pg([(36, 112), (58, 48), (80, 112)], close=True)),
                ink(pg([(78, 112), (100, 28), (122, 112)], close=True)),
                ink(pg([(120, 112), (142, 48), (164, 112)], close=True)),
            ),
            step(
                "Put a circle jewel on each point and on the band.",
                ink(circ(58, 56, 6)),
                ink(circ(100, 36, 7)),
                ink(circ(142, 56, 6)),
                ink(circ(70, 130, 5), width=THIN),
                ink(circ(100, 130, 5), width=THIN),
                ink(circ(130, 130, 5), width=THIN),
            ),
        ],
    )


def wand() -> dict:
    return subject(
        "wand",
        "Wand",
        "fantasy",
        ["wand", "wands", "magic wand"],
        [
            step(
                "Draw a long thin stick, tilted a little.",
                ink(pg([(78, 168), (92, 168), (128, 48), (114, 48)], close=True)),
            ),
            step("Add a star at the tip.", ink(star(132, 36, 28, 12))),
            step(
                "Draw two smaller sparkle stars.",
                ink(star(168, 28, 10, 4), width=THIN),
                ink(star(156, 64, 8, 3.5), width=THIN),
            ),
            step(
                "Add two bands on the handle.",
                ink(ln(82, 150, 96, 150), width=THIN),
                ink(ln(86, 136, 100, 136), width=THIN),
            ),
        ],
    )
