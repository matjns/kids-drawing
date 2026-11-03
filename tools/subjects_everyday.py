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


def ball() -> dict:
    return subject(
        "ball",
        "Ball",
        "everyday",
        ["ball", "beach ball", "beachball", "soccer ball", "football"],
        [
            step("Draw a big circle.", ink(circ(100, 100, 70))),
            step(
                "Draw a line across the middle and a line from top to bottom.",
                ink(ln(30, 100, 170, 100), width=THIN),
                ink(ln(100, 30, 100, 170), width=THIN),
            ),
            step(
                "Add four curved panel lines that meet in the middle.",
                ink(curve(100, 32, 60, 60, 32, 100), width=THIN),
                ink(curve(100, 32, 140, 60, 168, 100), width=THIN),
                ink(curve(100, 168, 60, 140, 32, 100), width=THIN),
                ink(curve(100, 168, 140, 140, 168, 100), width=THIN),
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
            step(
                "Draw the cup. A rounded rectangle open at the top is fine, then an oval rim.",
                ink(pg([(58, 70), (142, 70), (132, 150), (68, 150)], close=True)),
                ink(ell(100, 70, 42, 12)),
            ),
            step(
                "Add a handle on the right.",
                ink(arc(148, 108, 22, 28, 280, 80), width=W),
            ),
            step(
                "Draw two curls of steam.",
                ink(curve(80, 52, 70, 36, 84, 22), width=THIN),
                ink(curve(112, 48, 124, 30, 108, 16), width=THIN),
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
    return subject(
        "umbrella",
        "Umbrella",
        "everyday",
        ["umbrella", "umbrellas", "brolly"],
        [
            step("Draw the canopy, a big arch.", ink(arc(100, 120, 70, 62, 180, 360), width=W)),
            step("Close the canopy with a straight line.", ink(ln(30, 120, 170, 120), width=W)),
            step(
                "Add three ribs from the middle of the canopy down to the edge.",
                lines([(100, 58, 100, 120), (60, 86, 100, 120), (140, 86, 100, 120)], width=THIN),
            ),
            step(
                "Draw the shaft and a J-shaped handle.",
                ink(ln(100, 120, 100, 168), width=W),
                ink(arc(86, 168, 14, 14, 0, 180), width=W),
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
            step("Draw the seat, a flat rectangle.", ink(rr(48, 96, 104, 18, 3))),
            step(
                "Add the back: two posts and a top rail.",
                ink(rr(56, 36, 12, 64, 2)),
                ink(rr(132, 36, 12, 64, 2)),
                ink(rr(56, 28, 88, 16, 4)),
            ),
            step(
                "Draw four legs.",
                lines([(58, 114, 46, 176), (78, 114, 74, 176), (122, 114, 126, 176), (142, 114, 156, 176)]),
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
