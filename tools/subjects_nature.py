"""Nature: trees, weather, and a snowman."""

from shapes import THIN, W, arc, circ, cloud_outline, curve, ell, ink, leaf, lines, ln, pg, rr, smile, step, subject, dot_eyes
from shapes import arc, mirror, scallop, sp, tube


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


def _petal(angle: float) -> list:
    import math

    def at(r: float, a: float) -> tuple[float, float]:
        return (100 + r * math.cos(math.radians(a)), 62 + r * math.sin(math.radians(a)))

    return [at(13, angle - 9), at(30, angle - 10), at(42, angle), at(30, angle + 10), at(13, angle + 9)]


def tree() -> dict:
    return subject(
        "tree",
        "Tree",
        "nature",
        ["tree", "trees"],
        [
            step(
                "Draw a thick trunk that spreads out into roots at the bottom.",
                ink(sp([(78, 182, 1), (90, 172), (93, 150), (93, 122)])),
                ink(sp([(124, 182, 1), (110, 172), (107, 150), (107, 122)])),
            ),
            step(
                "Draw a big, bumpy cloud of leaves on top of the trunk.",
                ink(scallop(100, 72, 76, 50, n=10, puff=0.13)),
            ),
            step(
                "Add branches growing up from the trunk into the leaves.",
                ink(sp([(94, 124), (82, 110), (66, 98)]), width=THIN),
                ink(sp([(106, 122), (120, 108), (136, 98)]), width=THIN),
                ink(sp([(100, 122), (100, 104), (98, 90)]), width=THIN),
            ),
            step(
                "Finish with bark lines on the trunk and a line for the ground.",
                lines([(98, 140, 99, 152), (103, 158, 102, 168)], width=2),
                ink(sp([(40, 182), (100, 184), (160, 182)]), width=THIN),
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
            step("Draw a circle for the middle of the flower.", ink(circ(100, 62, 13))),
            step(
                "Draw long, thin petals all the way around, like the spokes of a wheel.",
                [ink(sp(_petal(a)), width=THIN) for a in range(0, 360, 30)],
            ),
            step(
                "Draw a long stem that bends a little on the way down.",
                ink(sp([(100, 104), (104, 134), (98, 186)])),
            ),
            step(
                "Add two pointy leaves on the stem.",
                ink(sp([(102, 150), (80, 136), (58, 136, 1), (76, 150), (100, 158)], closed=True), width=THIN),
                ink(sp([(103, 128), (124, 114), (146, 112, 1), (130, 126), (104, 136)], closed=True), width=THIN),
            ),
            step(
                "Finish with little dots in the middle.",
                [ink(circ(100 + x, 62 + y, 1.8), width=1.4, fill=True) for x, y in
                 [(-5, -4), (4, -5), (6, 3), (-3, 5), (0, 0)]],
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
            step(
                "Draw a round cap like a dome, with a gently curved bottom edge.",
                ink(sp([(24, 100, 1), (34, 62), (68, 36), (100, 30), (132, 36), (166, 62), (176, 100, 1), (150, 108),
                        (100, 112), (50, 108)], closed=True)),
            ),
            step(
                "Draw a thick stem that gets a little wider at the bottom.",
                ink(sp([(80, 110), (78, 140), (72, 170), (86, 178), (114, 178), (128, 170), (122, 140), (120, 110)])),
            ),
            step(
                "Add thin lines under the cap for the gills.",
                lines([(56, 106, 80, 112), (144, 106, 120, 112), (68, 109, 84, 112), (132, 109, 116, 112)], width=1.8),
            ),
            step(
                "Finish with round spots on the cap and a few blades of grass.",
                ink(circ(70, 62, 9), width=THIN),
                ink(circ(104, 48, 10), width=THIN),
                ink(circ(138, 66, 8), width=THIN),
                ink(circ(96, 84, 6), width=THIN),
                lines([(60, 180, 56, 166), (64, 180, 66, 168), (138, 180, 136, 168), (142, 180, 146, 166)], width=2.4),
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
