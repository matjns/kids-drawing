"""Dragon, unicorn, crown, and a magic wand."""

from shapes import THIN, W, circ, curve, ell, flame, ink, lines, ln, pg, rr, smile, star, step, subject, smooth


def all_subjects() -> list[dict]:
    return [dragon(), unicorn(), crown(), wand()]


def dragon() -> dict:
    return subject(
        "dragon",
        "Dragon",
        "fantasy",
        ["dragon", "dragons", "dragin"],
        [
            step("Draw an oval body.", ink(ell(112, 118, 36, 24))),
            step(
                "Add a long neck and a head with a snout.",
                ink(smooth([(96, 100), (70, 80), (58, 58)]), width=W),
                ink(ell(48, 52, 22, 14)),
                ink(pg([(30, 48), (12, 56), (28, 62)], close=True)),
                ink(pg([(36, 36), (28, 16), (48, 36)], close=True)),
                ink(pg([(52, 32), (64, 14), (60, 40)], close=True)),
            ),
            step(
                "Draw a bat-shaped wing and two lines for the wing bones.",
                ink(pg([(104, 100), (64, 62), (96, 36), (132, 48), (158, 84), (128, 104)], close=True)),
                ink(ln(104, 100, 96, 40), width=THIN),
                ink(ln(104, 100, 140, 56), width=THIN),
            ),
            step(
                "Add a tail, two legs, and spikes on the back.",
                ink(smooth([(144, 112), (176, 100), (188, 124), (170, 136)]), width=W),
                ink(pg([(96, 136), (84, 170), (104, 170), (108, 140)], close=True)),
                ink(pg([(124, 136), (120, 172), (142, 172), (140, 140)], close=True)),
                ink(pg([(120, 96), (128, 78), (136, 98)], close=True), width=THIN),
                ink(pg([(136, 100), (146, 82), (152, 104)], close=True), width=THIN),
            ),
            step(
                "Finish with an eye, a nostril, and a puff of fire.",
                ink(circ(40, 48, 2.6), width=2, fill=True),
                ink(circ(18, 54, 1.8), width=1.5, fill=True),
                ink(pg([(24, 50), (6, 40), (12, 54), (2, 64), (22, 60)], close=True), width=THIN),
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
            step("Draw an oval body.", ink(ell(108, 118, 46, 26))),
            step(
                "Add a neck and a head.",
                ink(pg([(132, 100), (154, 62), (170, 66), (156, 108)], close=True)),
                ink(ell(176, 58, 20, 14)),
                ink(ell(196, 62, 8, 5)),
            ),
            step(
                "Draw four legs and little hooves.",
                lines(
                    [
                        (78, 138, 72, 176),
                        (96, 140, 94, 178),
                        (126, 140, 130, 178),
                        (146, 136, 154, 174),
                    ]
                ),
                lines(
                    [(66, 176, 80, 176), (86, 178, 102, 178), (122, 178, 140, 178), (146, 174, 162, 174)],
                    width=THIN,
                ),
            ),
            step(
                "Add the horn, a mane, and a tail.",
                ink(pg([(168, 46), (176, 16), (184, 46)], close=True)),
                lines([(156, 70, 140, 52), (152, 82, 134, 66), (148, 94, 130, 80)], width=THIN),
                ink(smooth([(66, 104), (36, 96), (24, 120), (40, 142)]), width=W),
            ),
            step(
                "Draw an eye and a smile.",
                ink(circ(182, 54, 2.4), width=2, fill=True),
                smile(186, 64, 12, 4),
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
