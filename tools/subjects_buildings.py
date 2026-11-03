"""Buildings and a bridge."""

from shapes import THIN, W, arc, circ, curve, ell, ink, lines, ln, pg, rr, step, subject


def all_subjects() -> list[dict]:
    return [house(), castle(), school(), barn(), lighthouse(), bridge()]


def house() -> dict:
    return subject(
        "house",
        "House",
        "buildings",
        ["house", "houses", "home", "homes"],
        [
            step("Draw a square for the walls.", ink(rr(48, 96, 104, 84, 2))),
            step(
                "Add a triangle roof.",
                ink(pg([(36, 100), (100, 40), (164, 100)], close=True)),
            ),
            step("Draw a door.", ink(rr(88, 132, 28, 48, 3))),
            step(
                "Add a window with a cross.",
                ink(rr(60, 112, 28, 24, 2), width=THIN),
                ink(ln(74, 112, 74, 136), width=THIN),
                ink(ln(60, 124, 88, 124), width=THIN),
            ),
            step(
                "Draw a chimney, a doorknob, and two smoke puffs.",
                ink(rr(124, 58, 16, 32, 2)),
                ink(circ(108, 158, 2.4), width=2, fill=True),
                ink(circ(136, 40, 6), width=THIN),
                ink(circ(150, 28, 8), width=THIN),
            ),
        ],
    )


def castle() -> dict:
    return subject(
        "castle",
        "Castle",
        "buildings",
        ["castle", "castles"],
        [
            step("Draw the main wall.", ink(rr(40, 96, 120, 80, 2))),
            step(
                "Add three towers. Make the middle one taller.",
                ink(rr(28, 70, 28, 106, 2)),
                ink(rr(86, 40, 28, 136, 2)),
                ink(rr(144, 70, 28, 106, 2)),
            ),
            step(
                "Draw battlements: small squares along the tops.",
                ink(rr(28, 58, 10, 14, 1), width=THIN),
                ink(rr(46, 58, 10, 14, 1), width=THIN),
                ink(rr(86, 28, 10, 14, 1), width=THIN),
                ink(rr(104, 28, 10, 14, 1), width=THIN),
                ink(rr(144, 58, 10, 14, 1), width=THIN),
                ink(rr(162, 58, 10, 14, 1), width=THIN),
            ),
            step(
                "Add an arched door and two windows.",
                _arch(86, 128, 28, 48),
                ink(rr(52, 112, 14, 16, 2), width=THIN),
                ink(rr(134, 112, 14, 16, 2), width=THIN),
            ),
            step(
                "Put a triangle flag on the middle tower.",
                ink(ln(100, 28, 100, 12), width=THIN),
                ink(pg([(100, 12), (122, 18), (100, 24)], close=True)),
            ),
        ],
    )


def _arch(x: float, y: float, w: float, h: float) -> dict:
    # Door: rectangle bottom with a semicircle top. One path.
    r = w / 2
    d = (
        f"M {x} {y + h} "
        f"L {x} {y + r} "
        f"C {x} {y + r * 0.45} {x + r * 0.45} {y} {x + r} {y} "
        f"C {x + w - r * 0.45} {y} {x + w} {y + r * 0.45} {x + w} {y + r} "
        f"L {x + w} {y + h} Z"
    )
    return ink(d)


def school() -> dict:
    return subject(
        "school",
        "School",
        "buildings",
        ["school", "schools"],
        [
            step("Draw a wide rectangle for the building.", ink(rr(24, 78, 152, 96, 2))),
            step(
                "Add a small bell tower on the roof.",
                ink(rr(86, 40, 28, 40, 2)),
                ink(pg([(80, 44), (100, 18), (120, 44)], close=True)),
                ink(circ(100, 52, 5), width=THIN),
            ),
            step("Draw the door.", ink(rr(86, 128, 28, 46, 3))),
            step(
                "Add a grid of windows.",
                ink(rr(36, 96, 22, 18, 2), width=THIN),
                ink(rr(64, 96, 16, 18, 2), width=THIN),
                ink(rr(120, 96, 16, 18, 2), width=THIN),
                ink(rr(142, 96, 22, 18, 2), width=THIN),
                ink(rr(36, 122, 22, 16, 2), width=THIN),
                ink(rr(142, 122, 22, 16, 2), width=THIN),
            ),
            step(
                "Draw two steps.",
                ink(rr(78, 174, 44, 6, 1), width=THIN),
                ink(rr(70, 180, 60, 6, 1), width=THIN),
            ),
        ],
    )


def barn() -> dict:
    return subject(
        "barn",
        "Barn",
        "buildings",
        ["barn", "barns"],
        [
            step("Draw the barn walls.", ink(rr(28, 96, 110, 84, 2))),
            step(
                "Add a gambrel roof: a house roof with an extra bend.",
                ink(pg([(22, 100), (48, 62), (78, 46), (118, 62), (144, 100)], close=True)),
            ),
            step(
                "Draw the big door with an X.",
                ink(rr(58, 124, 48, 56, 2)),
                ink(ln(58, 124, 106, 180), width=THIN),
                ink(ln(106, 124, 58, 180), width=THIN),
            ),
            step(
                "Add a silo beside the barn.",
                ink(rr(148, 78, 32, 102, 4)),
                ink(ell(164, 78, 16, 10)),
            ),
            step(
                "Draw a small window in the roof.",
                ink(rr(78, 70, 18, 16, 2), width=THIN),
            ),
        ],
    )


def lighthouse() -> dict:
    return subject(
        "lighthouse",
        "Lighthouse",
        "buildings",
        ["lighthouse", "lighthouses", "light house"],
        [
            step(
                "Draw the tower, wider at the bottom.",
                ink(pg([(78, 48), (122, 48), (136, 160), (64, 160)], close=True)),
            ),
            step(
                "Add stripe lines.",
                lines([(74, 78, 126, 78), (70, 104, 130, 104), (68, 130, 132, 130)], width=THIN),
            ),
            step(
                "Draw the lantern room and a dome.",
                ink(rr(80, 28, 40, 24, 2)),
                ink(arc(100, 30, 16, 14, 180, 360), width=W),
            ),
            step(
                "Add light rays and a door.",
                lines([(40, 36, 18, 28), (40, 44, 16, 48), (160, 36, 184, 28), (160, 44, 186, 50)], width=THIN),
                ink(rr(92, 120, 16, 28, 2), width=THIN),
            ),
            step(
                "Draw rocks at the base.",
                ink(ell(52, 172, 18, 10)),
                ink(ell(100, 178, 22, 8)),
                ink(ell(148, 172, 18, 10)),
            ),
        ],
    )


def bridge() -> dict:
    return subject(
        "bridge",
        "Bridge",
        "buildings",
        ["bridge", "bridges"],
        [
            step("Draw the deck, a long flat shape.", ink(rr(16, 112, 168, 14, 3))),
            step(
                "Add two towers.",
                ink(rr(48, 48, 16, 78, 2)),
                ink(rr(136, 48, 16, 78, 2)),
            ),
            step(
                "Hang two curved cables.",
                ink(arc(100, 40, 70, 78, 35, 145), width=THIN),
                ink(arc(100, 48, 58, 64, 40, 140), width=THIN),
            ),
            step(
                "Draw water underneath.",
                ink(curve(16, 156, 50, 146, 84, 156), width=THIN),
                ink(curve(84, 162, 120, 150, 156, 160), width=THIN),
                ink(curve(24, 176, 70, 166, 120, 176), width=THIN),
            ),
        ],
    )
