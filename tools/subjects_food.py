"""Food. Familiar shapes: a circle apple, a triangle pizza slice, a cone."""

from shapes import THIN, W, arc, circ, curve, ell, ink, leaf, lines, ln, pg, rr, smile, spiral, step, subject
from shapes import arc, mirror, scallop, sp, tube


def all_subjects() -> list[dict]:
    return [
        apple(),
        banana(),
        pizza(),
        ice_cream(),
        cake(),
        cookie(),
        carrot(),
        cupcake(),
        watermelon(),
        donut(),
        strawberry(),
        hot_dog(),
    ]


def _cone_lines() -> list[tuple[float, float, float, float]]:
    def left(t: float) -> tuple[float, float]:
        return (70 + 30 * t, 100 + 84 * t)

    def right(t: float) -> tuple[float, float]:
        return (130 - 30 * t, 100 + 84 * t)

    out = []
    for a, b in [(0.0, 0.42), (0.25, 0.72), (0.0, 0.0)]:
        if a == b:
            continue
        out.append((*left(a), *right(b)))
        out.append((*right(a), *left(b)))
    out.append((*left(0.45), *right(0.85)))
    out.append((*right(0.45), *left(0.85)))
    return out


def apple() -> dict:
    return subject(
        "apple",
        "Apple",
        "food",
        ["apple", "apples", "aple"],
        [
            step(
                "Draw the apple: two round bumps on top with a dip in the middle, and a rounded bottom.",
                ink(sp([(100, 62, 1), (118, 50), (146, 52), (164, 76), (166, 110), (152, 146), (130, 164), (114, 164),
                        (100, 160), (86, 164), (70, 164), (48, 146), (34, 110), (36, 76), (54, 52), (82, 50)],
                       closed=True)),
            ),
            step(
                "Add a short stem coming out of the dip.",
                ink(sp([(100, 64), (102, 48), (108, 32)])),
            ),
            step(
                "Draw a leaf next to the stem, with a line down its middle.",
                ink(sp([(104, 46), (120, 30), (148, 28, 1), (134, 46), (108, 48)], closed=True), width=THIN),
                ink(sp([(108, 46), (126, 38), (144, 30)]), width=2),
            ),
            step(
                "Finish with a curved shine line on the left side.",
                ink(sp([(54, 86), (54, 104), (60, 120)]), width=THIN),
            ),
        ],
    )


def _apple_outline() -> str:
    # Circle-like apple with a concave bite on the right.
    p_cmds = (
        "M 100 42 "
        "C 70 42 46 66 46 100 "
        "C 46 140 72 164 100 164 "
        "C 122 164 138 152 146 136 "
        "C 132 128 134 112 148 104 "
        "C 138 78 128 42 100 42 Z"
    )
    return p_cmds


def banana() -> dict:
    return subject(
        "banana",
        "Banana",
        "food",
        ["banana", "bananas"],
        [
            step(
                "Draw a long curved shape like a smile turned on its side, pointy at the bottom left.",
                ink(sp([(152, 34), (166, 64), (166, 104), (150, 140), (118, 164), (80, 174), (48, 170, 1), (64, 160),
                        (100, 152), (128, 130), (144, 98), (148, 62), (146, 36)], closed=True)),
            ),
            step(
                "Add a short stem at the top with a flat end.",
                ink(sp([(146, 36), (146, 22, 1), (156, 22, 1), (152, 34)])),
            ),
            step(
                "Draw a line along the banana to show its edge.",
                ink(sp([(62, 166), (104, 162), (138, 140), (158, 100), (156, 56)]), width=THIN),
            ),
            step(
                "Finish with a dark tip at the bottom.",
                ink(sp([(48, 170), (56, 164), (58, 170)], closed=True), width=2, fill=True),
            ),
        ],
    )


def pizza() -> dict:
    return subject(
        "pizza",
        "Pizza",
        "food",
        ["pizza", "slice", "pizza slice", "piza"],
        [
            step(
                "Draw a big slice: a point at the bottom and a curved edge at the top.",
                ink(sp([(100, 178, 1), (34, 52, 1), (100, 30), (166, 52, 1)], closed=True)),
            ),
            step(
                "Draw a second curve under the top to make the thick crust.",
                ink(sp([(44, 66), (100, 46), (156, 66)])),
            ),
            step(
                "Add round pepperoni slices.",
                ink(circ(80, 82, 11), width=THIN),
                ink(circ(120, 86, 10), width=THIN),
                ink(circ(98, 118, 10), width=THIN),
                ink(circ(102, 150, 7), width=THIN),
            ),
            step(
                "Finish with little olive rings and bits of green pepper.",
                ink(circ(70, 104, 4), width=2.2),
                ink(circ(124, 112, 4), width=2.2),
                ink(circ(96, 92, 3.6), width=2.2),
                ink(sp([(80, 136), (86, 132), (90, 138)]), width=2.2),
                ink(sp([(112, 128), (118, 124), (120, 132)]), width=2.2),
            ),
        ],
    )


def ice_cream() -> dict:
    return subject(
        "ice-cream",
        "Ice Cream",
        "food",
        ["ice cream", "icecream", "ice-cream", "cone", "ice"],
        [
            step(
                "Draw a cone: a long triangle with the point at the bottom.",
                ink(sp([(70, 100, 1), (100, 184, 1), (130, 100, 1)])),
            ),
            step(
                "Draw criss-cross lines on the cone, like a waffle.",
                lines(_cone_lines(), width=2.2),
            ),
            step(
                "Draw a big round scoop on top with drips around the bottom.",
                ink(sp([(66, 100), (62, 80), (72, 56), (100, 42), (128, 56), (138, 80), (134, 100), (126, 110),
                        (118, 100), (108, 114), (98, 102), (86, 110), (76, 100)], closed=True)),
            ),
            step(
                "Finish with a cherry and a little stem on top.",
                ink(circ(102, 36, 8)),
                ink(sp([(104, 28), (108, 16), (116, 10)]), width=THIN),
            ),
        ],
    )


def cake() -> dict:
    return subject(
        "cake",
        "Cake",
        "food",
        ["cake", "cakes", "birthday cake", "birthday"],
        [
            step("Draw a wide oval for the top of the cake.", ink(ell(100, 96, 56, 12))),
            step(
                "Draw the sides going down and a curved bottom.",
                ink(ln(44, 96, 44, 158)),
                ink(ln(156, 96, 156, 158)),
                ink(sp([(44, 158), (100, 172), (156, 158)])),
            ),
            step(
                "Add drippy frosting under the top edge, and a curved line for the filling.",
                ink(sp([(44, 100), (52, 116), (60, 106), (70, 120), (80, 108), (92, 122), (104, 110), (116, 122),
                        (128, 108), (140, 118), (150, 106), (156, 100)]), width=THIN),
                ink(sp([(44, 136), (100, 150), (156, 136)]), width=THIN),
            ),
            step(
                "Draw three thin candles on top.",
                ink(rr(70, 66, 8, 28, 2), width=THIN),
                ink(rr(96, 58, 8, 32, 2), width=THIN),
                ink(rr(122, 66, 8, 28, 2), width=THIN),
            ),
            step(
                "Finish with a little flame on each candle.",
                [ink(sp([(x, top), (x - 5, top - 8), (x, top - 18, 1), (x + 5, top - 8)], closed=True), width=2.4)
                 for x, top in [(74, 62), (100, 54), (126, 62)]],
            ),
        ],
    )


def cookie() -> dict:
    return subject(
        "cookie",
        "Cookie",
        "food",
        ["cookie", "cookies", "biscuit", "biscuits", "cooky"],
        [
            step("Draw a circle.", ink(circ(100, 104, 58))),
            step(
                "Add chocolate chips. Small circles scattered on the cookie.",
                ink(circ(78, 86, 7), width=THIN),
                ink(circ(112, 78, 6), width=THIN),
                ink(circ(124, 108, 7), width=THIN),
                ink(circ(86, 122, 6), width=THIN),
                ink(circ(108, 132, 5), width=THIN),
            ),
            step(
                "Draw a little bite on the upper right: a small curve cutting the edge.",
                ink(arc(142, 70, 16, 14, 40, 200), width=W),
            ),
        ],
    )


def carrot() -> dict:
    return subject(
        "carrot",
        "Carrot",
        "food",
        ["carrot", "carrots"],
        [
            step(
                "Draw a long carrot shape: wide and round at the top, and pointy at the bottom.",
                ink(sp([(78, 66), (100, 58), (122, 66), (120, 100), (110, 140), (98, 180, 1), (90, 140), (80, 100)],
                       closed=True)),
            ),
            step(
                "Add short curved lines across the carrot.",
                ink(sp([(80, 86), (88, 88), (94, 86)]), width=2.2),
                ink(sp([(106, 104), (112, 106), (118, 104)]), width=2.2),
                ink(sp([(86, 122), (92, 124), (98, 122)]), width=2.2),
                ink(sp([(102, 144), (106, 146), (110, 144)]), width=2.2),
            ),
            step(
                "Draw three long, leafy stems sticking out of the top.",
                ink(sp([(94, 60), (80, 40), (72, 18, 1), (90, 34), (100, 58)], closed=True), width=THIN),
                ink(sp([(98, 58), (96, 32), (102, 8, 1), (108, 32), (104, 58)], closed=True), width=THIN),
                ink(sp([(102, 58), (114, 34), (130, 18, 1), (122, 40), (108, 60)], closed=True), width=THIN),
            ),
            step(
                "Finish with a line down the middle of each leaf.",
                lines([(97, 58, 78, 26), (101, 58, 102, 16), (105, 58, 126, 24)], width=1.8),
            ),
        ],
    )


def cupcake() -> dict:
    return subject(
        "cupcake",
        "Cupcake",
        "food",
        ["cupcake", "cupcakes", "cup cake", "fairy cake"],
        [
            step(
                "Draw the wrapper. It is a trapezoid, wider at the top.",
                ink(pg([(58, 108), (142, 108), (128, 168), (72, 168)], close=True)),
            ),
            step(
                "Add pleat lines on the wrapper.",
                lines([(80, 112, 86, 164), (100, 108, 100, 168), (120, 112, 114, 164)], width=THIN),
            ),
            step("Swirl a round frosting cloud on top.", ink(ell(100, 96, 48, 28))),
            step(
                "Add a cherry.",
                ink(circ(100, 62, 10)),
                ink(curve(106, 56, 118, 46, 114, 38), width=THIN),
            ),
        ],
    )


def watermelon() -> dict:
    return subject(
        "watermelon",
        "Watermelon",
        "food",
        ["watermelon", "melon"],
        [
            step(
                "Draw a big half circle: a flat line on top and a round bottom.",
                ink(ln(24, 80, 176, 80)),
                ink(arc(100, 80, 76, 76, 0, 180)),
            ),
            step(
                "Draw a second curve inside to make the green skin.",
                ink(arc(100, 80, 64, 63, 0, 180), width=THIN),
            ),
            step(
                "Add a third curve close to the skin for the white part.",
                ink(arc(100, 80, 58, 57, 0, 180), width=2),
            ),
            step(
                "Finish with seeds shaped like little teardrops.",
                [ink(sp([(x, y - 5, 1), (x + 3, y + 1), (x, y + 4), (x - 3, y + 1)], closed=True), width=1.6, fill=True)
                 for x, y in [(70, 98), (100, 96), (130, 98), (84, 116), (116, 116), (100, 132), (60, 108), (140, 108)]],
            ),
        ],
    )


def donut() -> dict:
    return subject(
        "donut",
        "Donut",
        "food",
        ["donut", "donuts", "doughnut", "doughnuts"],
        [
            step("Draw a big circle.", ink(circ(100, 104, 62))),
            step("Draw a smaller circle in the middle for the hole.", ink(circ(100, 104, 24))),
            step(
                "Add sprinkle marks around the ring.",
                lines(
                    [
                        (70, 70, 78, 60),
                        (108, 58, 116, 48),
                        (142, 78, 156, 70),
                        (150, 112, 166, 116),
                        (132, 146, 142, 158),
                        (96, 150, 90, 164),
                        (64, 128, 48, 136),
                        (60, 92, 46, 84),
                    ],
                    width=THIN,
                ),
            ),
        ],
    )


def strawberry() -> dict:
    return subject(
        "strawberry",
        "Strawberry",
        "food",
        ["strawberry", "strawberries", "berry"],
        [
            step(
                "Draw a berry that is wide at the top and comes to a round point at the bottom.",
                ink(sp([(60, 72), (100, 62), (140, 72), (152, 98), (140, 134), (118, 162), (100, 172), (82, 162),
                        (60, 134), (48, 98)], closed=True)),
            ),
            step(
                "Draw a leafy cap with pointy leaves on top.",
                ink(sp([(100, 60), (84, 58), (64, 72, 1), (84, 70), (78, 86, 1), (96, 72), (102, 88, 1), (108, 72),
                        (124, 84, 1), (118, 70), (138, 72, 1), (118, 58)], closed=True), width=THIN),
            ),
            step(
                "Add a short stem.",
                ink(sp([(100, 60), (102, 48), (108, 38)])),
            ),
            step(
                "Finish with lots of tiny seeds.",
                [ink(ell(x, y, 1.6, 2.6), width=1.4, fill=True) for x, y in [
                    (70, 96), (90, 92), (112, 92), (132, 96), (62, 116), (82, 112), (104, 110), (126, 112),
                    (142, 114), (74, 134), (96, 130), (118, 132), (86, 150), (108, 150), (100, 164)]],
            ),
        ],
    )


def _berry() -> str:
    return (
        "M 100 40 "
        "C 70 70 58 100 64 140 "
        "C 70 168 130 168 136 140 "
        "C 142 100 130 70 100 40 Z"
    )


def hot_dog() -> dict:
    zig = [(36 + i * 8, 94 if i % 2 == 0 else 100) for i in range(17)]
    return subject(
        "hot-dog",
        "Hot Dog",
        "food",
        ["hot dog", "hotdog", "hot dogs", "hotdogs", "sausage"],
        [
            step(
                "Draw a long sausage with round ends.",
                ink(sp([(20, 98), (30, 88), (100, 90), (170, 88), (182, 98), (172, 108), (100, 110), (28, 108)],
                       closed=True)),
            ),
            step(
                "Draw the back of the bun peeking up behind the sausage.",
                ink(sp([(34, 89), (44, 74), (100, 70), (156, 74), (166, 89)])),
            ),
            step(
                "Draw the front of the bun: a big curve under the sausage.",
                ink(sp([(22, 104), (30, 128), (70, 140), (130, 140), (170, 128), (178, 104)])),
                ink(sp([(26, 108), (100, 118), (174, 108)]), width=THIN),
            ),
            step(
                "Finish with a wiggly line of mustard along the top.",
                ink(sp(zig), width=2.6),
            ),
        ],
    )
