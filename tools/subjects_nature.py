"""Nature: trees, weather, and a snowman."""

from shapes import THIN, W, arc, circ, cloud_outline, curve, ell, ink, leaf, lines, ln, pg, rr, smile, step, subject, dot_eyes


def all_subjects() -> list[dict]:
    return [
        tree(),
        flower(),
        sun(),
        cloud(),
        rainbow(),
        mountain(),
        leaf_subject(),
        mushroom(),
        snowman(),
        rain(),
    ]


def tree() -> dict:
    return subject(
        "tree",
        "Tree",
        "nature",
        ["tree", "trees"],
        [
            step(
                "Draw the trunk. A tall trapezoid, wider at the bottom.",
                ink(pg([(90, 118), (110, 118), (120, 178), (80, 178)], close=True)),
            ),
            step(
                "Add one bumpy shape for the leaves. It sits on the trunk.",
                ink(cloud_outline(100, 86, 120, 78)),
            ),
            step(
                "Draw a small knot on the trunk.",
                ink(ell(100, 146, 6, 8), width=THIN),
            ),
            step(
                "Add two short grass lines beside the trunk.",
                lines([(78, 178, 68, 188), (122, 178, 132, 188)], width=THIN),
            ),
        ],
    )


def flower() -> dict:
    return subject(
        "flower",
        "Flower",
        "nature",
        ["flower", "flowers", "blossom"],
        [
            step("Draw a straight stem.", ink(ln(100, 112, 100, 186), width=W)),
            step(
                "Add two leaves.",
                ink(leaf(78, 146, 28, 18)),
                ink(leaf(124, 162, 26, 16)),
            ),
            step("Draw a circle in the middle of the flower.", ink(circ(100, 78, 14))),
            step(
                "Add six oval petals around the center.",
                ink(ell(100, 42, 12, 18)),
                ink(ell(100, 114, 12, 18)),
                ink(ell(64, 60, 18, 12)),
                ink(ell(136, 60, 18, 12)),
                ink(ell(64, 98, 18, 12)),
                ink(ell(136, 98, 18, 12)),
            ),
            step(
                "Give the center a face.",
                dot_eyes(100, 76, gap=8, r=1.8),
                smile(100, 84, 10, 4),
            ),
        ],
    )


def sun() -> dict:
    return subject(
        "sun",
        "Sun",
        "nature",
        ["sun", "sunshine", "sunny"],
        [
            step("Draw a circle for the face.", ink(circ(100, 100, 40))),
            step(
                "Add rays all the way around. Straight lines are perfect.",
                lines(
                    [
                        (100, 48, 100, 18),
                        (100, 152, 100, 184),
                        (52, 100, 18, 100),
                        (148, 100, 182, 100),
                        (66, 66, 40, 40),
                        (134, 66, 160, 40),
                        (66, 134, 40, 160),
                        (134, 134, 160, 160),
                    ]
                ),
            ),
            step(
                "Draw two eyes and a smile.",
                dot_eyes(100, 94, gap=18, r=3.4),
                smile(100, 108, 24, 12),
            ),
        ],
    )


def cloud() -> dict:
    return subject(
        "cloud",
        "Cloud",
        "nature",
        ["cloud", "clouds"],
        [
            step(
                "Draw one cloud outline: three bumps on top and a smooth bottom.",
                ink(cloud_outline(100, 104, 140, 80)),
            ),
            step(
                "Add two eyes.",
                dot_eyes(100, 108, gap=22, r=3),
            ),
            step(
                "Draw a smile.",
                smile(100, 122, 22, 8),
            ),
            step(
                "Add a short shine curve on the left bump.",
                ink(curve(62, 96, 70, 84, 82, 90), width=THIN),
            ),
        ],
    )


def rainbow() -> dict:
    return subject(
        "rainbow",
        "Rainbow",
        "nature",
        ["rainbow", "rainbows"],
        [
            step("Draw a big arch.", ink(arc(100, 150, 78, 70, 180, 360), width=W)),
            step("Draw a second arch inside the first.", ink(arc(100, 150, 60, 54, 180, 360), width=W)),
            step("Draw a third, smaller arch.", ink(arc(100, 150, 42, 38, 180, 360), width=W)),
            step(
                "Add a small cloud at each end.",
                ink(circ(26, 156, 14)),
                ink(circ(174, 156, 14)),
            ),
        ],
    )


def mountain() -> dict:
    return subject(
        "mountain",
        "Mountain",
        "nature",
        ["mountain", "mountains", "hill"],
        [
            step(
                "Draw a big triangle.",
                ink(pg([(16, 168), (100, 36), (168, 168)], close=True)),
            ),
            step(
                "Add a smaller triangle beside it.",
                ink(pg([(90, 168), (150, 78), (190, 168)], close=True)),
            ),
            step(
                "Cap the tall peak with a snow zigzag.",
                ink(pg([(78, 78), (100, 36), (122, 80), (108, 70), (100, 86), (90, 68)], close=True)),
            ),
            step(
                "Put a small sun in the corner.",
                ink(circ(36, 40, 14)),
                lines([(36, 20, 36, 12), (50, 28, 58, 22), (52, 42, 62, 44), (22, 28, 14, 22)], width=THIN),
            ),
        ],
    )


def leaf_subject() -> dict:
    return subject(
        "leaf",
        "Leaf",
        "nature",
        ["leaf", "leaves"],
        [
            step("Draw a pointed leaf outline.", ink(leaf(100, 104, 70, 120))),
            step("Add the center vein, from the stem to the tip.", ink(ln(100, 156, 100, 52), width=THIN)),
            step("Draw a short stem.", ink(ln(100, 164, 100, 186), width=W)),
            step(
                "Add side veins.",
                lines(
                    [
                        (100, 80, 78, 70),
                        (100, 100, 74, 96),
                        (100, 120, 76, 128),
                        (100, 80, 124, 72),
                        (100, 100, 128, 98),
                        (100, 120, 126, 130),
                    ],
                    width=THIN,
                ),
            ),
        ],
    )


def mushroom() -> dict:
    return subject(
        "mushroom",
        "Mushroom",
        "nature",
        ["mushroom", "mushrooms", "toadstool"],
        [
            step("Draw the cap. A wide oval is the top.", ink(ell(100, 86, 62, 28))),
            step(
                "Close the cap with a curved line underneath.",
                ink(arc(100, 96, 58, 16, 15, 165), width=W),
            ),
            step("Draw the stem.", ink(rr(82, 100, 36, 72, 10))),
            step(
                "Add spots on the cap.",
                ink(circ(70, 78, 8), width=THIN),
                ink(circ(100, 70, 7), width=THIN),
                ink(circ(128, 82, 8), width=THIN),
            ),
        ],
    )


def snowman() -> dict:
    return subject(
        "snowman",
        "Snowman",
        "nature",
        ["snowman", "snowmen"],
        [
            step(
                "Stack three circles, biggest at the bottom.",
                ink(circ(100, 150, 36)),
                ink(circ(100, 100, 26)),
                ink(circ(100, 58, 18)),
            ),
            step(
                "Add a top hat.",
                ink(ell(100, 40, 28, 6)),
                ink(rr(84, 14, 32, 26, 3)),
                ink(ell(100, 14, 16, 5), width=THIN),
            ),
            step(
                "Draw eyes, a carrot nose, a smile, and buttons.",
                dot_eyes(100, 54, gap=12, r=2.2),
                ink(pg([(104, 60), (124, 64), (104, 68)], close=True)),
                smile(100, 70, 14, 5),
                ink(circ(100, 96, 3), width=2, fill=True),
                ink(circ(100, 112, 3), width=2, fill=True),
                ink(circ(100, 146, 3.2), width=2, fill=True),
            ),
            step(
                "Add stick arms.",
                ink(pg([(76, 100), (40, 80), (46, 74)])),
                ink(pg([(124, 100), (162, 78), (168, 86)])),
            ),
        ],
    )


def rain() -> dict:
    return subject(
        "rain",
        "Rain",
        "nature",
        ["rain", "rainy", "raining"],
        [
            step(
                "Draw one cloud at the top of the page.",
                ink(cloud_outline(108, 58, 120, 64)),
            ),
            step(
                "Add raindrops underneath. Straight lines are easy to copy.",
                lines(
                    [
                        (60, 100, 48, 140),
                        (84, 104, 72, 150),
                        (108, 100, 100, 156),
                        (132, 104, 124, 148),
                        (156, 102, 148, 138),
                    ]
                ),
            ),
            step(
                "Add shorter drops between the long ones.",
                lines([(72, 112, 66, 136), (96, 114, 92, 140), (120, 112, 116, 138), (144, 110, 140, 132)], width=THIN),
            ),
            step(
                "Draw a puddle at the bottom.",
                ink(ell(100, 176, 50, 10)),
            ),
        ],
    )
