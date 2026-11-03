"""Vehicles, drawn from the side so the wheels and windows are easy to copy."""

from shapes import THIN, W, circ, curve, ell, ink, lines, ln, pg, rr, step, subject, wheel


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
                "Draw the body: a long rounded rectangle.",
                ink(rr(28, 108, 146, 40, 16)),
            ),
            step(
                "Add the cabin. A trapezoid with a flat top sits on the body.",
                ink(pg([(70, 108), (84, 70), (132, 70), (150, 108)], close=True)),
            ),
            step(
                "Draw two wheels with smaller circles in the middle.",
                wheel(62, 152, 18),
                wheel(138, 152, 18),
            ),
            step(
                "Add a window line, a door line, and a headlight.",
                ink(ln(100, 74, 100, 108), width=THIN),
                ink(ln(108, 116, 108, 144), width=THIN),
                ink(circ(160, 124, 6), width=THIN),
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
            step("Draw the body: a long rounded rectangle.", ink(rr(28, 86, 146, 30, 14))),
            step(
                "Add the big wing and a small tail wing.",
                ink(pg([(78, 100), (118, 156), (148, 156), (124, 108)], close=True)),
                ink(pg([(146, 100), (176, 128), (186, 120), (160, 100)], close=True)),
            ),
            step(
                "Draw the tail fin.",
                ink(pg([(150, 86), (184, 48), (184, 86)], close=True)),
            ),
            step(
                "Add windows and a nose circle.",
                ink(circ(48, 100, 4), width=THIN),
                ink(circ(64, 100, 4), width=THIN),
                ink(circ(80, 100, 4), width=THIN),
                ink(circ(96, 100, 4), width=THIN),
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
                "Draw two wheels.",
                wheel(58, 132, 30),
                wheel(148, 132, 30),
            ),
            step(
                "Connect the wheels with a triangle frame.",
                lines(
                    [
                        (58, 132, 104, 132),
                        (58, 132, 100, 78),
                        (104, 132, 100, 78),
                        (104, 132, 148, 132),
                    ]
                ),
            ),
            step(
                "Add the seat, handlebars, and the front fork.",
                ink(ln(86, 78, 114, 78), width=W),
                ink(ln(100, 78, 100, 70), width=THIN),
                ink(pg([(148, 132), (132, 62), (156, 58)])),
                ink(ln(124, 60, 164, 64), width=W),
            ),
            step(
                "Draw the pedal circle in the middle of the frame.",
                ink(circ(104, 132, 8), width=THIN),
                ink(ln(96, 132, 112, 132), width=THIN),
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
            step("Draw an oval body.", ink(ell(78, 112, 36, 24))),
            step(
                "Add a long tail and a small tail fin.",
                ink(rr(108, 104, 62, 10, 5)),
                ink(pg([(168, 96), (188, 70), (188, 114), (168, 114)], close=True)),
            ),
            step(
                "Draw the main rotor: a long thin oval and a short line across it.",
                ink(ell(78, 62, 70, 6)),
                ink(ln(78, 48, 78, 86), width=THIN),
            ),
            step(
                "Add the skids, a tail rotor, and a window.",
                lines([(52, 134, 40, 156), (104, 134, 116, 156), (36, 156, 122, 156)]),
                ink(circ(176, 108, 6), width=THIN),
                ink(ell(70, 108, 12, 8), width=THIN),
            ),
        ],
    )
