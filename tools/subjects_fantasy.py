"""Dragon, unicorn, crown, and a magic wand."""

from shapes import THIN, W, Path, circ, curve, ell, ink, lines, ln, pg, rr, smile, star, step, subject, smooth


def all_subjects() -> list[dict]:
    return [dragon(), unicorn(), crown(), wand()]


def dragon() -> dict:
    return subject(
        "dragon",
        "Dragon",
        "fantasy",
        ["dragon", "dragons", "dragin"],
        [
            step("Draw an oval body.", ink(ell(122, 132, 38, 22))),
            step(
                "Add a neck, a head, a snout, and two small horns.",
                ink(pg([(104, 122), (82, 90), (74, 72), (92, 80), (112, 126)], close=True)),
                ink(ell(60, 70, 20, 14)),
                ink(pg([(44, 66), (22, 74), (46, 82)], close=True)),
                ink(pg([(50, 58), (44, 38), (62, 56)], close=True)),
                ink(pg([(66, 56), (76, 34), (78, 58)], close=True)),
            ),
            step(
                "Draw one curved wing, then a line for the bone.",
                ink(_dragon_wing()),
                ink(ln(112, 120, 128, 48), width=THIN),
            ),
            step(
                "Add a curved tail and two legs.",
                ink(smooth([(156, 128), (180, 116), (188, 136)]), width=W),
                ink(pg([(108, 150), (100, 176), (118, 176), (120, 152)], close=True)),
                ink(pg([(132, 150), (130, 178), (148, 178), (144, 150)], close=True)),
            ),
            step(
                "Finish with an eye and a small flame in front of the snout.",
                ink(circ(52, 66, 2.4), width=2, fill=True),
                ink(pg([(24, 72), (8, 64), (14, 76), (6, 86), (26, 80)], close=True), width=THIN),
            ),
        ],
    )


def unicorn() -> dict:
    return subject(
        "unicorn",
        "Unicorn",
        "fantasy",
        ["unicorn", "unicorns", "unicron"],
        [
            step("Draw a long oval for the body.", ink(ell(104, 124, 42, 22))),
            step(
                "Add four straight legs and a short hoof on each one.",
                lines([(76, 142, 72, 176), (96, 144, 94, 178), (122, 144, 126, 178), (140, 140, 148, 174)]),
                lines([(66, 176, 80, 176), (86, 178, 102, 178), (118, 178, 136, 178), (140, 174, 156, 174)], width=THIN),
            ),
            step(
                "Draw a neck, an oval head, and one ear.",
                ink(pg([(126, 110), (150, 76), (164, 66), (156, 88), (136, 122)], close=True)),
                ink(ell(178, 66, 18, 12)),
                ink(pg([(166, 60), (158, 38), (176, 56)], close=True)),
            ),
            step(
                "Add a horn, a short mane, and a tail.",
                ink(pg([(172, 56), (180, 24), (190, 56)], close=True)),
                lines([(148, 74, 138, 58), (142, 88, 130, 74), (136, 102, 122, 90)], width=THIN),
                ink(smooth([(64, 112), (40, 104), (28, 128), (42, 150)]), width=W),
            ),
            step(
                "Draw an eye.",
                ink(circ(184, 64, 2.4), width=2, fill=True),
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


def _dragon_wing() -> str:
    p = Path()
    p.M(112, 124)
    p.C(78, 78, 96, 32, 148, 50)
    p.C(146, 86, 132, 116, 116, 134)
    p.Z()
    return p.text()


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
