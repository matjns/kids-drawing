"""Everyday things kids ask to draw."""

from shapes import (
    THIN,
    W,
    arc,
    circ,
    curve,
    ell,
    heart,
    ink,
    lines,
    ln,
    pg,
    rr,
    smile,
    spiral,
    star,
    step,
    subject,
)
from shapes import arc, mirror, scallop, sp, tube


def all_subjects() -> list[dict]:
    return [
        ball(),
        book(),
        cup(),
        clock(),
        hat(),
        umbrella(),
        pencil(),
        kite(),
        balloon(),
        heart_subject(),
        gift(),
        robot(),
        chair(),
        lamp(),
    ]


def _ball_parts() -> tuple[list, list, list]:
    import math

    def at(r: float, deg: float) -> tuple[float, float]:
        a = math.radians(deg - 90)
        return (100 + r * math.cos(a), 100 + r * math.sin(a))

    pent = [at(20, i * 72) for i in range(5)]
    seams = []
    for i in range(5):
        a = i * 72
        seams.append((*at(20, a), *at(36, a)))
        seams.append((*at(36, a), *at(46, a + 24)))
        seams.append((*at(36, a), *at(46, a - 24)))
        seams.append((*at(46, a + 24), *at(60, a + 30)))
        seams.append((*at(46, a - 24), *at(60, a - 30)))
    edge = []
    for i in range(5):
        a = i * 72 + 36
        edge.append([at(48, a - 12), at(48, a + 12), at(59, a + 16), at(59, a - 16)])
    return pent, seams, edge


def ball() -> dict:
    pent, seams, edge = _ball_parts()
    return subject(
        "ball",
        "Ball",
        "everyday",
        ["ball", "beach ball", "beachball", "soccer ball", "football"],
        [
            step("Draw a big circle.", ink(circ(100, 100, 60))),
            step(
                "Draw a five-sided shape in the middle and color it in.",
                ink(pg(pent, close=True), width=2, fill=True),
            ),
            step(
                "Draw lines from each corner out toward the edge, splitting into a Y.",
                lines(seams, width=2.4),
            ),
            step(
                "Color in the patches near the edge, between the Y lines.",
                [ink(pg(p, close=True), width=2, fill=True) for p in edge],
            ),
        ],
    )


def book() -> dict:
    return subject(
        "book",
        "Book",
        "everyday",
        ["book", "books"],
        [
            step(
                "Draw the open cover: two pages with a curved bottom.",
                ink(pg([(28, 48), (96, 40), (96, 160), (36, 168)], close=True)),
                ink(pg([(104, 40), (172, 48), (164, 168), (104, 160)], close=True)),
            ),
            step("Add the spine in the middle.", ink(ln(100, 36, 100, 164), width=W)),
            step(
                "Draw writing lines on each page.",
                lines(
                    [
                        (44, 70, 84, 66),
                        (42, 88, 84, 84),
                        (42, 106, 82, 102),
                        (44, 124, 80, 120),
                        (116, 66, 156, 70),
                        (116, 84, 158, 88),
                        (116, 102, 156, 106),
                        (118, 120, 154, 124),
                    ],
                    width=THIN,
                ),
            ),
            step(
                "Add a bookmark ribbon.",
                ink(pg([(92, 40), (108, 40), (104, 78), (100, 70), (96, 78)], close=True)),
            ),
        ],
    )


def cup() -> dict:
    return subject(
        "cup",
        "Cup",
        "everyday",
        ["cup", "cups", "mug", "mugs"],
        [
            step("Draw a wide oval for the top of the mug.", ink(ell(90, 62, 40, 10))),
            step(
                "Draw the sides going down and a round bottom.",
                ink(sp([(50, 62), (52, 110), (54, 150)])),
                ink(sp([(130, 62), (128, 110), (126, 150)])),
                ink(sp([(54, 150), (90, 162), (126, 150)])),
            ),
            step(
                "Add a big curved handle on the right.",
                ink(sp([(130, 80), (156, 78), (166, 104), (152, 130), (127, 134)])),
                ink(sp([(129, 92), (148, 92), (152, 106), (144, 120), (127, 122)])),
            ),
            step(
                "Finish with a line for the drink inside, and wavy steam on top.",
                ink(sp([(56, 64), (90, 70), (124, 64)]), width=2),
                ink(sp([(78, 44), (72, 34), (80, 24), (74, 14)]), width=THIN),
                ink(sp([(100, 44), (94, 34), (102, 24), (96, 14)]), width=THIN),
            ),
        ],
    )


def clock() -> dict:
    return subject(
        "clock",
        "Clock",
        "everyday",
        ["clock", "clocks"],
        [
            step("Draw a circle.", ink(circ(100, 108, 62))),
            step(
                "Add tick marks at the top, bottom, left, and right.",
                lines(
                    [
                        (100, 52, 100, 64),
                        (100, 152, 100, 164),
                        (44, 108, 56, 108),
                        (144, 108, 156, 108),
                    ],
                    width=W,
                ),
            ),
            step(
                "Draw the hands. The short hand points right. The long hand points up.",
                ink(ln(100, 108, 132, 108), width=W),
                ink(ln(100, 108, 100, 68), width=THIN),
                ink(circ(100, 108, 4), width=2, fill=True),
            ),
            step(
                "Add two bells and little feet to make an alarm clock.",
                ink(circ(70, 52, 12)),
                ink(circ(130, 52, 12)),
                ink(ln(82, 48, 118, 48), width=THIN),
                ink(ell(72, 172, 12, 6)),
                ink(ell(128, 172, 12, 6)),
            ),
        ],
    )


def hat() -> dict:
    return subject(
        "hat",
        "Hat",
        "everyday",
        ["hat", "hats", "top hat", "tophat"],
        [
            step("Draw the brim, a wide flat oval.", ink(ell(100, 132, 70, 16))),
            step("Add the crown, a tall rectangle.", ink(rr(68, 48, 64, 86, 4))),
            step("Draw the top of the hat, a smaller oval.", ink(ell(100, 48, 32, 10))),
            step("Add a band around the crown.", ink(rr(68, 96, 64, 14, 2), width=THIN)),
        ],
    )


def umbrella() -> dict:
    ribs = [24, 62, 100, 138, 176]
    edge = []
    for i, x in enumerate(ribs):
        edge.append((x, 100, 1))
        if i < len(ribs) - 1:
            edge.append(((x + ribs[i + 1]) / 2, 90))
    return subject(
        "umbrella",
        "Umbrella",
        "everyday",
        ["umbrella", "umbrellas", "brolly"],
        [
            step(
                "Draw a big dome for the top of the umbrella.",
                ink(sp([(24, 100, 1), (38, 62), (100, 30), (162, 62), (176, 100, 1)])),
            ),
            step(
                "Draw the bottom edge as four curved bumps.",
                ink(sp(edge)),
            ),
            step(
                "Draw curved lines from the top down to each point.",
                ink(sp([(100, 30), (70, 52), (62, 100)]), width=THIN),
                ink(sp([(100, 30), (130, 52), (138, 100)]), width=THIN),
                ink(ln(100, 30, 100, 100), width=THIN),
            ),
            step(
                "Finish with a long handle that curls at the bottom like a J, and a tip on top.",
                ink(ln(100, 100, 100, 160)),
                ink(sp([(100, 160), (100, 172), (110, 180), (120, 172), (120, 166)])),
                ink(ln(100, 30, 100, 20)),
            ),
        ],
    )


def pencil() -> dict:
    return subject(
        "pencil",
        "Pencil",
        "everyday",
        ["pencil", "pencils"],
        [
            step("Draw the long body.", ink(rr(48, 86, 110, 28, 2))),
            step(
                "Add the wood tip, a triangle, and a lead point.",
                ink(pg([(48, 86), (18, 100), (48, 114)], close=True)),
                ink(pg([(28, 94), (12, 100), (28, 106)], close=True)),
            ),
            step(
                "Draw the eraser and the metal band.",
                ink(rr(158, 86, 22, 28, 4)),
                ink(rr(148, 86, 12, 28, 1), width=THIN),
            ),
            step(
                "Add a line where the wood meets the body.",
                ink(ln(48, 86, 48, 114), width=THIN),
            ),
        ],
    )


def kite() -> dict:
    return subject(
        "kite",
        "Kite",
        "everyday",
        ["kite", "kites"],
        [
            step(
                "Draw a diamond.",
                ink(pg([(100, 24), (160, 90), (100, 168), (40, 90)], close=True)),
            ),
            step(
                "Add the cross spars.",
                ink(ln(100, 24, 100, 168), width=THIN),
                ink(ln(40, 90, 160, 90), width=THIN),
            ),
            step(
                "Draw a tail with two bows.",
                ink(smooth_tail(), width=THIN),
                ink(pg([(112, 150), (132, 142), (128, 160)], close=True), width=THIN),
                ink(pg([(96, 176), (116, 170), (108, 188)], close=True), width=THIN),
            ),
        ],
    )


def smooth_tail() -> str:
    return curve(100, 168, 130, 160, 108, 188)


def balloon() -> dict:
    return subject(
        "balloon",
        "Balloon",
        "everyday",
        ["balloon", "balloons"],
        [
            step("Draw an oval balloon.", ink(ell(100, 78, 42, 52))),
            step(
                "Add the knot, a small triangle.",
                ink(pg([(92, 126), (108, 126), (100, 142)], close=True)),
            ),
            step(
                "Draw a curly string.",
                ink(spiral(104, 168, 4, 18, 1.1, a0=-1.2), width=THIN),
            ),
            step(
                "Add a shine curve on the balloon.",
                ink(arc(82, 70, 12, 22, 200, 330), width=THIN),
            ),
        ],
    )


def heart_subject() -> dict:
    return subject(
        "heart",
        "Heart",
        "everyday",
        ["heart", "hearts", "love"],
        [
            step("Draw a big heart: two bumps on top and a point at the bottom.", ink(heart(100, 96, 120, 110))),
            step("Draw a smaller heart inside.", ink(heart(100, 100, 64, 58), width=THIN)),
            step(
                "Add two little sparkle stars.",
                ink(star(36, 40, 12, 5), width=THIN),
                ink(star(168, 56, 10, 4), width=THIN),
            ),
        ],
    )


def gift() -> dict:
    return subject(
        "gift",
        "Gift",
        "everyday",
        ["gift", "gifts", "present", "presents"],
        [
            step("Draw the box.", ink(rr(40, 88, 120, 88, 4))),
            step("Add the lid line.", ink(ln(36, 88, 164, 88), width=W)),
            step(
                "Draw the ribbon, one line down and one across.",
                ink(ln(100, 48, 100, 176), width=W),
                ink(ln(40, 124, 160, 124), width=W),
            ),
            step(
                "Add a bow on top: two loops and two tails.",
                ink(ell(80, 62, 18, 12)),
                ink(ell(120, 62, 18, 12)),
                ink(circ(100, 64, 6), width=THIN),
                ink(pg([(86, 74), (70, 96), (90, 84)], close=True), width=THIN),
                ink(pg([(114, 74), (132, 96), (110, 84)], close=True), width=THIN),
            ),
        ],
    )


def robot() -> dict:
    return subject(
        "robot",
        "Robot",
        "everyday",
        ["robot", "robots"],
        [
            step("Draw a rounded square head.", ink(rr(62, 28, 76, 58, 10))),
            step("Draw a bigger rounded body.", ink(rr(52, 96, 96, 70, 10))),
            step(
                "Add eyes, a smile, and an antenna.",
                ink(circ(86, 52, 8)),
                ink(circ(114, 52, 8)),
                ink(circ(86, 52, 3), width=2, fill=True),
                ink(circ(114, 52, 3), width=2, fill=True),
                smile(100, 70, 24, 8),
                ink(ln(100, 28, 100, 12), width=THIN),
                ink(circ(100, 10, 5)),
            ),
            step(
                "Draw arms and legs.",
                ink(rr(24, 104, 22, 48, 8)),
                ink(rr(154, 104, 22, 48, 8)),
                ink(rr(64, 168, 24, 22, 6)),
                ink(rr(112, 168, 24, 22, 6)),
            ),
            step(
                "Add a chest panel.",
                ink(rr(80, 112, 40, 28, 4), width=THIN),
                lines([(88, 122, 112, 122), (88, 130, 112, 130)], width=THIN),
            ),
        ],
    )


def chair() -> dict:
    return subject(
        "chair",
        "Chair",
        "everyday",
        ["chair", "chairs", "seat"],
        [
            step(
                "Draw the seat as a slanted box shape, like you are looking from the side.",
                ink(pg([(48, 112), (124, 112), (150, 96), (76, 96)], close=True)),
                ink(pg([(48, 112), (48, 120), (124, 120), (150, 104), (150, 96)]), width=THIN),
            ),
            step(
                "Draw two tall posts going up from the back of the seat.",
                ink(ln(78, 96, 78, 26)),
                ink(ln(148, 96, 148, 26)),
            ),
            step(
                "Add a curved bar across the top and two slats under it.",
                ink(sp([(74, 28), (113, 20), (152, 28)])),
                ink(sp([(74, 38), (113, 30), (152, 38)])),
                lines([(102, 34, 102, 96), (124, 34, 124, 96)], width=THIN),
            ),
            step(
                "Draw four legs. The back legs are a little shorter because they are farther away.",
                ink(ln(50, 120, 50, 178)),
                ink(ln(122, 120, 122, 178)),
                ink(ln(148, 104, 148, 164)),
                ink(ln(80, 120, 80, 164), width=THIN),
            ),
        ],
    )


def lamp() -> dict:
    return subject(
        "lamp",
        "Lamp",
        "everyday",
        ["lamp", "lamps"],
        [
            step("Draw the base, a flat oval.", ink(ell(100, 170, 36, 10))),
            step("Add the stem.", ink(ln(100, 160, 100, 86), width=W)),
            step(
                "Draw the lampshade, a trapezoid wider at the bottom.",
                ink(pg([(52, 86), (148, 86), (128, 42), (72, 42)], close=True)),
            ),
            step(
                "Add a pull cord and two light lines.",
                ink(ln(118, 86, 118, 112), width=THIN),
                ink(circ(118, 118, 4), width=THIN),
                lines([(64, 96, 48, 112), (136, 96, 156, 112)], width=THIN),
            ),
        ],
    )
