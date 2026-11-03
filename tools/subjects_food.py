"""Food. Familiar shapes: a circle apple, a triangle pizza slice, a cone."""

from shapes import THIN, W, arc, circ, curve, ell, ink, leaf, lines, ln, pg, rr, smile, spiral, step, subject


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


def apple() -> dict:
    return subject(
        "apple",
        "Apple",
        "food",
        ["apple", "apples", "aple"],
        [
            step(
                "Draw a circle, but tuck a bite into the right side.",
                ink(_apple_outline()),
            ),
            step("Add a short stem.", ink(curve(100, 48, 108, 30, 112, 22), width=W)),
            step("Draw a leaf on the stem.", ink(leaf(128, 30, 22, 16))),
            step(
                "Add a small shine curve on the left.",
                ink(arc(78, 78, 10, 16, 200, 340), width=THIN),
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
                "Draw the outer curve, from the stem down to the tip.",
                ink(curve(96, 42, 46, 90, 78, 168)),
            ),
            step(
                "Draw the inner curve and close both ends so the banana is one shape.",
                ink(curve(112, 52, 78, 100, 96, 156)),
                ink(ln(96, 42, 112, 52), width=W),
                ink(ln(78, 168, 96, 156), width=W),
            ),
            step(
                "Add a small stem at the top.",
                ink(pg([(100, 40), (112, 26), (108, 46)], close=True)),
            ),
            step(
                "Draw two short lines along the peel.",
                ink(curve(90, 78, 82, 110, 86, 140), width=THIN),
                ink(curve(98, 90, 90, 120, 94, 148), width=THIN),
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
                "Draw a triangle pointing down. This is the slice.",
                ink(pg([(46, 58), (154, 58), (100, 168)], close=True)),
            ),
            step(
                "Draw a line across the top for the crust. Keep it inside the triangle.",
                ink(ln(54, 88, 146, 88), width=W),
            ),
            step(
                "Draw three pepperoni circles.",
                ink(circ(86, 96, 10), width=THIN),
                ink(circ(116, 90, 9), width=THIN),
                ink(circ(102, 122, 8), width=THIN),
            ),
            step(
                "Add a drip of cheese on one side.",
                ink(curve(64, 70, 52, 96, 66, 112), width=THIN),
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
                "Draw a triangle cone, point down.",
                ink(pg([(70, 96), (130, 96), (100, 176)], close=True)),
            ),
            step(
                "Add two crisscross lines on the cone.",
                ink(ln(82, 112, 118, 150), width=THIN),
                ink(ln(118, 112, 82, 150), width=THIN),
            ),
            step("Draw the bottom scoop. A circle sitting on the cone.", ink(circ(100, 88, 26))),
            step("Add a second scoop on top.", ink(circ(100, 58, 22))),
            step(
                "Put a cherry on the very top.",
                ink(circ(100, 30, 8)),
                ink(curve(104, 24, 116, 16, 112, 10), width=THIN),
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
            step("Draw the bottom layer, a wide rectangle.", ink(rr(36, 112, 128, 52, 6))),
            step(
                "Add a wavy frosting line on top of the layer.",
                ink(curve(36, 112, 60, 96, 84, 112), width=W),
                ink(curve(84, 112, 112, 96, 136, 112), width=W),
                ink(curve(136, 112, 154, 100, 164, 112), width=W),
            ),
            step(
                "Draw a candle and a flame.",
                ink(rr(94, 62, 12, 50, 2)),
                ink(curve(100, 62, 90, 40, 100, 28), width=THIN),
                ink(curve(100, 62, 110, 40, 100, 28), width=THIN),
            ),
            step(
                "Add three dots on the cake.",
                ink(circ(62, 136, 4), width=2, fill=True),
                ink(circ(100, 142, 4), width=2, fill=True),
                ink(circ(138, 136, 4), width=2, fill=True),
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
                "Draw a long triangle, point down.",
                ink(pg([(70, 70), (130, 70), (100, 180)], close=True)),
            ),
            step(
                "Add two short lines across the carrot.",
                ink(ln(82, 110, 118, 110), width=THIN),
                ink(ln(90, 140, 110, 140), width=THIN),
            ),
            step(
                "Draw three leaves at the top.",
                ink(leaf(86, 48, 18, 36)),
                ink(leaf(108, 40, 16, 40)),
                ink(leaf(126, 52, 16, 32)),
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
                "Draw a big triangle. This is one slice.",
                ink(pg([(28, 78), (172, 78), (100, 176)], close=True)),
            ),
            step(
                "Add a rind line just inside the top edge.",
                ink(ln(40, 96, 160, 96), width=W),
            ),
            step(
                "Draw teardrop seeds.",
                ink(ell(78, 124, 4, 7)),
                ink(ell(100, 136, 4, 7)),
                ink(ell(122, 120, 4, 7)),
                ink(ell(96, 108, 3, 5), width=THIN),
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
                "Draw a plump triangle with a rounded bottom. A tall heart shape works.",
                ink(_berry()),
            ),
            step(
                "Add seed marks. Short little lines are enough.",
                lines(
                    [
                        (78, 96, 86, 104),
                        (100, 90, 108, 98),
                        (122, 100, 130, 108),
                        (84, 122, 92, 130),
                        (112, 124, 120, 132),
                        (96, 146, 104, 154),
                    ],
                    width=THIN,
                ),
            ),
            step(
                "Draw a leafy cap on top.",
                ink(leaf(78, 62, 28, 22)),
                ink(leaf(100, 52, 24, 26)),
                ink(leaf(124, 64, 26, 20)),
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
    return subject(
        "hot-dog",
        "Hot Dog",
        "food",
        ["hot dog", "hotdog", "hot dogs", "hotdogs", "sausage"],
        [
            step("Draw the bottom bun, a long flat oval.", ink(ell(100, 128, 70, 22))),
            step("Add the sausage, a slimmer oval on top of the bun.", ink(ell(100, 112, 62, 14))),
            step("Draw the top bun, another long oval.", ink(ell(100, 96, 64, 16))),
            step(
                "Squiggle mustard along the sausage.",
                ink(curve(52, 112, 70, 100, 90, 112), width=THIN),
                ink(curve(90, 112, 112, 124, 132, 110), width=THIN),
                ink(curve(132, 110, 148, 102, 156, 114), width=THIN),
            ),
        ],
    )
