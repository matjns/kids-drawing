"""Vehicles, drawn from the side so the wheels and windows are easy to copy."""

from shapes import THIN, W, circ, curve, ell, ink, lines, ln, pg, rr, step, subject, wheel
from shapes import arc, mirror, scallop, sp, tube


def all_subjects() -> list[dict]:
    return [car(), bus(), truck(), train(), airplane(), boat(), bicycle(), helicopter()]


def car() -> dict:
    return subject(
        "car",
        "Car",
        "vehicles",
        ["car", "cars", "auto", "automobile", "kar"],
        [
            step(
                "Draw the side of the car: a low trunk, a curved roof, and a long hood. Leave round bumps for the wheels.",
                ink(sp([(18, 132, 1), (16, 112), (22, 100), (56, 96), (74, 72), (92, 62), (130, 62), (152, 90),
                        (180, 98), (188, 112), (188, 132, 1), (166, 132, 1), (162, 118), (146, 110), (130, 118),
                        (126, 132, 1), (74, 132, 1), (70, 118), (54, 110), (38, 118), (34, 132, 1)], closed=True)),
            ),
            step(
                "Draw two wheels in the bumps, each with a small circle in the middle.",
                ink(circ(54, 134, 17)),
                ink(circ(54, 134, 7), width=THIN),
                ink(circ(146, 134, 17)),
                ink(circ(146, 134, 7), width=THIN),
            ),
            step(
                "Add two side windows under the roof.",
                ink(sp([(78, 94, 1), (92, 70, 1), (108, 70, 1), (108, 94, 1)], closed=True), width=THIN),
                ink(sp([(114, 94, 1), (114, 70, 1), (128, 70), (144, 92, 1)], closed=True), width=THIN),
            ),
            step(
                "Draw the door lines, door handles, a headlight, and a taillight.",
                ink(ln(111, 96, 112, 124), width=THIN),
                ink(ln(76, 96, 76, 124), width=THIN),
                lines([(92, 102, 100, 102), (126, 102, 134, 102)], width=2.6),
                ink(ell(180, 106, 5, 4), width=THIN),
                ink(sp([(18, 104, 1), (26, 104, 1), (26, 112, 1), (17, 112, 1)]), width=THIN),
            ),
            step(
                "Finish with a road line under the wheels.",
                ink(sp([(8, 152), (100, 152), (192, 152)]), width=THIN),
            ),
        ],
    )


def bus() -> dict:
    return subject(
        "bus",
        "Bus",
        "vehicles",
        ["bus", "buses", "school bus", "schoolbus"],
        [
            step("Draw a long rounded rectangle for the bus.", ink(rr(22, 64, 158, 78, 12))),
            step(
                "Add a row of square windows.",
                ink(rr(36, 76, 22, 18, 2), width=THIN),
                ink(rr(64, 76, 22, 18, 2), width=THIN),
                ink(rr(92, 76, 22, 18, 2), width=THIN),
                ink(rr(120, 76, 22, 18, 2), width=THIN),
            ),
            step(
                "Draw two wheels.",
                wheel(58, 148, 16),
                wheel(142, 148, 16),
            ),
            step(
                "Add a door and two headlights.",
                ink(rr(148, 96, 22, 40, 3), width=THIN),
                ink(circ(36, 124, 4), width=THIN),
                ink(circ(36, 136, 4), width=THIN),
            ),
        ],
    )


def truck() -> dict:
    return subject(
        "truck",
        "Truck",
        "vehicles",
        ["truck", "trucks", "lorry", "lorries"],
        [
            step("Draw the cab on the left. A rounded square is fine.", ink(rr(24, 78, 58, 58, 8))),
            step("Add the long cargo box on the right.", ink(rr(82, 70, 96, 66, 6))),
            step(
                "Draw three wheels.",
                wheel(46, 150, 16),
                wheel(112, 150, 16),
                wheel(154, 150, 16),
            ),
            step(
                "Add a window on the cab and a headlight.",
                ink(rr(34, 88, 28, 22, 3), width=THIN),
                ink(circ(30, 124, 5), width=THIN),
            ),
        ],
    )


def train() -> dict:
    return subject(
        "train",
        "Train",
        "vehicles",
        ["train", "trains", "locomotive", "choo choo", "choochoo"],
        [
            step("Draw the engine body, a long rounded rectangle.", ink(rr(36, 96, 130, 48, 10))),
            step("Add the cabin, a taller rectangle at the back.", ink(rr(118, 62, 48, 82, 6))),
            step(
                "Draw a chimney and three smoke puffs.",
                ink(rr(52, 70, 18, 28, 3)),
                ink(circ(48, 48, 8), width=THIN),
                ink(circ(64, 34, 10), width=THIN),
                ink(circ(82, 46, 7), width=THIN),
            ),
            step(
                "Add three wheels and a triangle cowcatcher on the front.",
                wheel(62, 152, 14),
                wheel(96, 152, 14),
                wheel(142, 152, 14),
                ink(pg([(36, 120), (14, 144), (36, 144)], close=True)),
            ),
            step(
                "Draw a window on the cabin.",
                ink(rr(128, 74, 26, 20, 3), width=THIN),
            ),
        ],
    )


def airplane() -> dict:
    return subject(
        "airplane",
        "Airplane",
        "vehicles",
        ["airplane", "airplanes", "plane", "planes", "jet", "aeroplane", "airplaine"],
        [
            step(
                "Draw a long tube for the body with a round nose on the right. It gets thinner and turns up at the tail.",
                ink(sp([(186, 102), (178, 92), (150, 88), (60, 88), (26, 76, 1), (20, 86, 1), (50, 106), (150, 112),
                        (178, 110)], closed=True)),
            ),
            step(
                "Draw the big wing sweeping back under the body, and the far wing peeking over the top.",
                ink(sp([(118, 106), (96, 132), (70, 156, 1), (56, 156, 1), (80, 108)])),
                ink(sp([(110, 88), (92, 66, 1), (80, 66, 1), (88, 88)])),
            ),
            step(
                "Add a tall fin on the tail and a small flat wing beside it.",
                ink(sp([(54, 88), (34, 46, 1), (20, 46, 1), (28, 78)])),
                ink(sp([(44, 98), (14, 108, 1), (24, 110, 1), (54, 102)])),
            ),
            step(
                "Hang a round engine under the wing.",
                ink(sp([(84, 118), (106, 116), (112, 124), (106, 132), (84, 132), (80, 125)], closed=True)),
                ink(ell(84, 125, 4, 7), width=THIN),
            ),
            step(
                "Finish with the cockpit window at the front and a row of little windows.",
                ink(sp([(170, 94), (180, 96), (182, 100), (172, 100)], closed=True), width=2.4),
                [ink(circ(x, 97, 2.6), width=2, fill=True) for x in range(62, 160, 12)],
            ),
        ],
    )


def boat() -> dict:
    return subject(
        "boat",
        "Boat",
        "vehicles",
        ["boat", "boats", "ship", "ships", "sailboat", "sail boat"],
        [
            step(
                "Draw the hull. It is a trapezoid, wider at the top.",
                ink(pg([(36, 112), (164, 112), (146, 150), (54, 150)], close=True)),
            ),
            step("Add a straight mast.", ink(ln(100, 112, 100, 28), width=W)),
            step(
                "Draw a triangle sail.",
                ink(pg([(100, 34), (100, 108), (148, 108)], close=True)),
            ),
            step(
                "Add a flag, a porthole, and two wave lines.",
                ink(pg([(100, 28), (124, 36), (100, 44)], close=True)),
                ink(circ(92, 130, 6), width=THIN),
                ink(curve(24, 168, 60, 156, 100, 168), width=THIN),
                ink(curve(100, 174, 140, 160, 180, 172), width=THIN),
            ),
        ],
    )


def bicycle() -> dict:
    return subject(
        "bicycle",
        "Bicycle",
        "vehicles",
        ["bicycle", "bike", "bikes", "cycle"],
        [
            step(
                "Draw two big wheels side by side, each with a tiny circle in the middle.",
                ink(circ(50, 130, 32)),
                ink(circ(150, 130, 32)),
                ink(circ(50, 130, 4), width=THIN),
                ink(circ(150, 130, 4), width=THIN),
            ),
            step(
                "Draw the frame: two triangles that share the line under the seat.",
                ink(pg([(50, 130), (94, 132), (84, 80)], close=True), width=4),
                ink(pg([(84, 80), (138, 80), (142, 92), (94, 132)], close=True), width=4),
            ),
            step(
                "Add the front fork down to the wheel, and handlebars on top.",
                ink(ln(142, 92, 150, 130), width=4),
                ink(ln(138, 80, 134, 64), width=4),
                ink(sp([(122, 64), (134, 63), (146, 58), (152, 66)]), width=4),
            ),
            step(
                "Draw the seat on a short post, and the pedals in the middle.",
                ink(ln(84, 80, 82, 70), width=4),
                ink(sp([(68, 68), (88, 66), (96, 70), (80, 74)], closed=True), width=THIN),
                ink(circ(94, 132, 7), width=THIN),
                ink(ln(94, 132, 104, 148), width=THIN),
                ink(ln(98, 148, 112, 148), width=4),
            ),
            step(
                "Finish with thin spokes in both wheels.",
                lines([(50, 100, 50, 160), (20, 130, 80, 130), (29, 109, 71, 151), (29, 151, 71, 109),
                       (150, 100, 150, 160), (120, 130, 180, 130), (129, 109, 171, 151), (129, 151, 171, 109)],
                      width=1.6),
            ),
        ],
    )


def helicopter() -> dict:
    return subject(
        "helicopter",
        "Helicopter",
        "vehicles",
        ["helicopter", "helicopters", "chopper", "copter"],
        [
            step(
                "Draw a round cabin, like a big egg lying on its side, with the front on the left.",
                ink(sp([(40, 110), (46, 86), (70, 72), (110, 70), (130, 80), (136, 104), (126, 124), (80, 128),
                        (50, 124)], closed=True)),
            ),
            step(
                "Draw a long, thin tail going out to the right, with a small fin at the end.",
                ink(sp([(134, 86), (160, 87), (184, 88)])),
                ink(sp([(132, 106), (160, 100), (184, 96)])),
                ink(sp([(182, 88), (188, 64, 1), (196, 66, 1), (194, 96, 1), (184, 97)])),
            ),
            step(
                "Draw a big window at the front and a door line.",
                ink(sp([(46, 104), (52, 86), (70, 78), (90, 78), (90, 104)], closed=True), width=THIN),
                ink(sp([(100, 76), (100, 120)]), width=THIN),
            ),
            step(
                "Add a short post on top and long, thin spinning blades.",
                ink(rr(86, 58, 10, 13, 2), width=THIN),
                ink(sp([(14, 54, 1), (90, 51), (174, 54, 1), (90, 58)], closed=True), width=THIN),
                ink(sp([(184, 76), (194, 84)]), width=THIN),
                ink(sp([(194, 72), (184, 88)]), width=THIN),
            ),
            step(
                "Finish with two legs and a long skid to land on.",
                lines([(68, 127, 62, 146), (112, 126, 118, 146)], width=THIN),
                ink(sp([(28, 140), (36, 148), (150, 148), (158, 142)])),
            ),
        ],
    )
