"""Space drawings: rocket, planets, and a friendly astronaut."""

from shapes import THIN, W, circ, curve, ell, flame, ink, lines, ln, pg, rr, smile, star, step, subject, dot_eyes
from shapes import arc, mirror, scallop, sp, tube


def all_subjects() -> list[dict]:
    return [rocket(), planet(), star_subject(), moon(), alien(), astronaut()]


def rocket() -> dict:
    return subject(
        "rocket",
        "Rocket",
        "space",
        ["rocket", "rockets", "spaceship", "space ship", "rockit"],
        [
            step("Draw the rocket body, a tall rounded rectangle.", ink(rr(78, 48, 44, 100, 18))),
            step(
                "Add a triangle nose.",
                ink(pg([(78, 62), (100, 16), (122, 62)], close=True)),
            ),
            step("Draw a round window.", ink(circ(100, 96, 12))),
            step(
                "Add a fin on each side.",
                ink(pg([(78, 112), (52, 156), (78, 148)], close=True)),
                ink(pg([(122, 112), (148, 156), (122, 148)], close=True)),
            ),
            step(
                "Draw the flame underneath.",
                ink(flame(100, 148, 42, 16)),
                ink(flame(100, 156, 26, 8), width=THIN),
            ),
        ],
    )


def planet() -> dict:
    return subject(
        "planet",
        "Planet",
        "space",
        ["planet", "planets", "saturn"],
        [
            step("Draw a circle.", ink(circ(100, 100, 40))),
            step(
                "Add a wide ring around it. A flat oval works.",
                ink(ell(100, 108, 74, 16)),
            ),
            step(
                "Draw a few crater circles on the planet.",
                ink(circ(86, 90, 8), width=THIN),
                ink(circ(112, 108, 6), width=THIN),
                ink(circ(96, 118, 5), width=THIN),
            ),
        ],
    )


def star_subject() -> dict:
    return subject(
        "star",
        "Star",
        "space",
        ["star", "stars"],
        [
            step("Draw a five-point star.", ink(star(100, 100, 78, 34))),
            step(
                "Add two eyes and a smile in the middle.",
                dot_eyes(100, 96, gap=16, r=3),
                smile(100, 112, 18, 8),
            ),
            step(
                "Draw two tiny stars nearby.",
                ink(star(28, 36, 12, 5), width=THIN),
                ink(star(176, 48, 10, 4), width=THIN),
            ),
        ],
    )


def moon() -> dict:
    return subject(
        "moon",
        "Moon",
        "space",
        ["moon", "crescent"],
        [
            step("Draw the crescent outline.", ink(_crescent())),
            step(
                "Add a sleepy face: two closed eyes and a small smile.",
                ink(curve(78, 96, 86, 90, 94, 96), width=THIN),
                ink(curve(106, 96, 114, 90, 122, 96), width=THIN),
                smile(100, 116, 18, 8),
            ),
            step(
                "Sprinkle three tiny stars around the moon.",
                ink(star(36, 48, 10, 4), width=THIN),
                ink(star(168, 60, 8, 3.5), width=THIN),
                ink(star(160, 150, 7, 3), width=THIN),
            ),
        ],
    )


def _crescent() -> str:
    # Outer right-hand curve and an inner curve back, tips at upper left and lower left.
    return (
        "M 78 42 "
        "C 150 42 176 78 176 104 "
        "C 176 140 140 170 78 164 "
        "C 118 156 132 128 132 104 "
        "C 132 78 112 58 78 42 Z"
    )


def alien() -> dict:
    return subject(
        "alien",
        "Alien",
        "space",
        ["alien", "aliens", "martian"],
        [
            step("Draw a big oval head.", ink(ell(100, 78, 40, 46))),
            step(
                "Add two large oval eyes.",
                ink(ell(82, 78, 14, 18)),
                ink(ell(118, 78, 14, 18)),
                ink(ell(84, 80, 5, 8), width=2, fill=True),
                ink(ell(120, 80, 5, 8), width=2, fill=True),
            ),
            step(
                "Draw antennae with little balls on the ends.",
                ink(ln(82, 36, 64, 16), width=THIN),
                ink(ln(118, 36, 136, 16), width=THIN),
                ink(circ(62, 14, 5)),
                ink(circ(138, 14, 5)),
            ),
            step(
                "Add a small body, two arms, and a smile.",
                ink(rr(78, 126, 44, 36, 12)),
                ink(curve(78, 140, 52, 150, 40, 132), width=W),
                ink(curve(122, 140, 150, 150, 164, 132), width=W),
                smile(100, 100, 20, 8),
            ),
        ],
    )


def astronaut() -> dict:
    arm = [(72, 86), (58, 104), (54, 124)]
    leg_l = [(80, 134), (78, 166), (96, 166, 1), (98, 136)]
    boot_l = [(74, 166, 1), (98, 166, 1), (100, 180, 1), (68, 180, 1)]
    return subject(
        "astronaut",
        "Astronaut",
        "space",
        ["astronaut", "astronauts", "spaceman"],
        [
            step(
                "Draw a big round helmet with a wide window in the front.",
                ink(circ(100, 46, 26)),
                ink(sp([(80, 42), (90, 32), (110, 32), (120, 42), (116, 56), (100, 60), (84, 56)], closed=True), width=THIN),
            ),
            step(
                "Draw a puffy suit body under the helmet.",
                ink(sp([(76, 74), (124, 74), (132, 92), (128, 128), (122, 136), (78, 136), (72, 128), (68, 92)],
                       closed=True)),
            ),
            step(
                "Add two puffy arms with round gloves.",
                ink(tube(arm, 17, 15, closed_start=False, keep=6)),
                ink(tube(mirror(arm), 17, 15, closed_start=False, keep=6)),
                ink(circ(54, 132, 8)),
                ink(circ(146, 132, 8)),
            ),
            step(
                "Draw two legs with big boots.",
                ink(sp(leg_l)),
                ink(sp(mirror(leg_l))),
                ink(sp(boot_l, closed=True)),
                ink(sp(mirror(boot_l), closed=True)),
            ),
            step(
                "Finish with a control box on the chest and a shine on the helmet window.",
                ink(rr(88, 92, 24, 16, 3), width=THIN),
                ink(circ(95, 100, 2), width=1.4, fill=True),
                ink(circ(105, 100, 2), width=1.4, fill=True),
                ink(sp([(88, 40), (94, 36), (100, 36)]), width=2),
                ink(ln(76, 124, 124, 124), width=2),
            ),
        ],
    )
