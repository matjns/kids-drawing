"""Animals. Each picture is built from circles, ovals, triangles, and a few curves."""

from shapes import (
    THIN,
    W,
    arc,
    circ,
    curve,
    dot_eyes,
    ell,
    eyes,
    flame,
    ink,
    leaf,
    lines,
    ln,
    nose,
    pg,
    rr,
    smile,
    smooth,
    spiral,
    step,
    subject,
)


def all_subjects() -> list[dict]:
    return [
        cat(),
        dog(),
        bird(),
        fish(),
        rabbit(),
        horse(),
        cow(),
        pig(),
        duck(),
        frog(),
        turtle(),
        butterfly(),
        elephant(),
        lion(),
        mouse(),
        owl(),
        penguin(),
        bear(),
        fox(),
        whale(),
        shark(),
        dinosaur(),
        snake(),
        spider(),
        bee(),
        sheep(),
        crab(),
        octopus(),
        giraffe(),
        monkey(),
    ]


def cat() -> dict:
    return subject(
        "cat",
        "Cat",
        "animals",
        ["cat", "cats", "kitty", "kitten", "kittens", "kitties", "kat", "catt", "kitteh"],
        [
            step("Draw a big circle for the head.", ink(circ(100, 78, 34))),
            step(
                "Add two triangle ears on top. The points face up.",
                ink(pg([(74, 54), (56, 16), (96, 46)], close=True)),
                ink(pg([(126, 54), (144, 16), (104, 46)], close=True)),
            ),
            step("Draw a wide oval under the head for the body.", ink(ell(100, 142, 44, 32))),
            step(
                "Add the face: two eyes, a nose, a smile, and three whiskers on each side.",
                eyes(100, 76, gap=26, r=6.5, pupil=2.8),
                nose(100, 92, 2.5),
                ink(ln(100, 94, 100, 102), width=THIN),
                smile(100, 102, 20, 8),
                lines(
                    [
                        (78, 90, 42, 82),
                        (78, 98, 40, 98),
                        (80, 106, 46, 114),
                        (122, 90, 158, 82),
                        (122, 98, 160, 98),
                        (120, 106, 154, 114),
                    ]
                ),
            ),
            step(
                "Draw two front legs and little oval paws.",
                lines([(82, 158, 76, 176), (118, 158, 124, 176)], width=W),
                ink(ell(72, 180, 10, 5), width=THIN),
                ink(ell(128, 180, 10, 5), width=THIN),
            ),
            step(
                "Finish with a curved tail on the right.",
                ink(smooth([(136, 128), (168, 118), (178, 86), (158, 68)]), width=W),
            ),
        ],
    )


def dog() -> dict:
    return subject(
        "dog",
        "Dog",
        "animals",
        ["dog", "dogs", "puppy", "puppies", "doggy", "doggie", "dogg", "pup", "hound", "puppi"],
        [
            step("Draw a circle for the head.", ink(circ(100, 74, 30))),
            step(
                "Hang a floppy oval ear on each side.",
                ink(ell(64, 92, 16, 28)),
                ink(ell(136, 92, 16, 28)),
            ),
            step("Draw a big oval body under the head.", ink(ell(100, 146, 42, 30))),
            step(
                "Add a snout, nose, eyes, and a tongue.",
                ink(ell(100, 96, 16, 12)),
                nose(100, 96, 3.2),
                dot_eyes(100, 68, gap=20, r=3.4),
                smile(100, 108, 16, 6),
                ink(ell(108, 118, 6, 8), width=THIN),
            ),
            step(
                "Add two front legs and a tail that curls up.",
                lines([(84, 162, 80, 182), (116, 162, 122, 182)]),
                ink(smooth([(138, 136), (168, 124), (176, 96)]), width=W),
            ),
        ],
    )


def bird() -> dict:
    return subject(
        "bird",
        "Bird",
        "animals",
        ["bird", "birds", "tweety", "sparrow", "brid"],
        [
            step("Draw an oval for the body, a little wider than it is tall.", ink(ell(96, 112, 38, 26))),
            step("Add a smaller circle for the head, up and to the right.", ink(circ(142, 78, 18))),
            step(
                "Draw a triangle beak pointing right, and a dot for the eye.",
                ink(pg([(156, 72), (180, 80), (156, 88)], close=True)),
                ink(circ(146, 74, 2.6), width=2, fill=True),
            ),
            step(
                "Add a wing on the body and a triangle tail on the left.",
                ink(ell(88, 112, 18, 11)),
                ink(pg([(62, 100), (28, 86), (28, 112), (60, 118)], close=True)),
            ),
            step(
                "Draw two thin legs and little feet.",
                lines([(88, 136, 84, 168), (108, 136, 114, 168)], width=THIN),
                lines([(84, 168, 74, 168), (84, 168, 92, 174), (114, 168, 106, 168), (114, 168, 124, 174)], width=THIN),
            ),
        ],
    )


def fish() -> dict:
    return subject(
        "fish",
        "Fish",
        "animals",
        ["fish", "fishes", "goldfish", "fis"],
        [
            step("Draw a wide oval for the body.", ink(ell(96, 104, 50, 30))),
            step(
                "Add a triangle tail on the left.",
                ink(pg([(52, 104), (18, 70), (18, 138)], close=True)),
            ),
            step(
                "Draw a top fin and a bottom fin. Each one is a triangle.",
                ink(pg([(80, 76), (108, 48), (124, 78)], close=True)),
                ink(pg([(90, 132), (112, 162), (128, 130)], close=True)),
            ),
            step(
                "Add an eye, a smile, and a curved gill.",
                ink(circ(128, 96, 3.2), width=2, fill=True),
                smile(124, 108, 16, 6),
                ink(arc(112, 104, 10, 16, 100, 260), width=THIN),
            ),
        ],
    )


def rabbit() -> dict:
    return subject(
        "rabbit",
        "Rabbit",
        "animals",
        ["rabbit", "rabbits", "bunny", "bunnies", "hare", "rabit"],
        [
            step("Draw a circle for the head.", ink(circ(104, 112, 28))),
            step(
                "Add two long oval ears above the head.",
                ink(ell(82, 58, 12, 36)),
                ink(ell(118, 52, 12, 38)),
                ink(ell(82, 62, 5, 22), width=THIN),
                ink(ell(118, 56, 5, 22), width=THIN),
            ),
            step("Draw an oval body under the head.", ink(ell(100, 158, 36, 22))),
            step(
                "Add eyes, a nose, two teeth, and a smile.",
                dot_eyes(104, 110, gap=18, r=3.2),
                nose(104, 122, 2.6),
                ink(rr(98, 126, 5, 8, 1), width=THIN),
                ink(rr(105, 126, 5, 8, 1), width=THIN),
                smile(104, 128, 14, 5),
            ),
            step(
                "Finish with a round tail and two feet.",
                ink(circ(148, 150, 12)),
                ink(ell(78, 176, 16, 7)),
                ink(ell(118, 178, 16, 7)),
            ),
        ],
    )


def horse() -> dict:
    return subject(
        "horse",
        "Horse",
        "animals",
        ["horse", "horses", "pony", "ponies", "hors"],
        [
            step("Draw a long oval for the body.", ink(ell(108, 112, 48, 26))),
            step(
                "Add four straight legs. Make the bottom of each leg a tiny hoof line.",
                lines(
                    [
                        (78, 132, 74, 176),
                        (96, 134, 94, 178),
                        (128, 134, 132, 178),
                        (148, 132, 154, 176),
                    ]
                ),
                lines([(68, 176, 82, 176), (88, 178, 102, 178), (124, 178, 140, 178), (146, 176, 162, 176)], width=THIN),
            ),
            step(
                "Draw the neck and a long head pointing right.",
                ink(pg([(136, 96), (158, 62), (176, 66), (168, 84), (150, 108)], close=True)),
                ink(ell(176, 62, 18, 12)),
                ink(pg([(186, 52), (198, 40), (190, 58)], close=True)),
            ),
            step(
                "Add a mane of short curves, an eye, and a tail.",
                lines(
                    [
                        (150, 70, 140, 52),
                        (146, 82, 134, 66),
                        (142, 94, 128, 80),
                    ],
                    width=THIN,
                ),
                ink(circ(180, 60, 2.4), width=2, fill=True),
                ink(smooth([(64, 100), (40, 108), (28, 136), (40, 156)]), width=W),
            ),
        ],
    )


def cow() -> dict:
    return subject(
        "cow",
        "Cow",
        "animals",
        ["cow", "cows", "calf", "moo"],
        [
            step("Draw a large oval body.", ink(ell(112, 122, 52, 34))),
            step("Add a circle head on the left.", ink(circ(58, 108, 26))),
            step(
                "Draw two short horns, two ears, and a snout.",
                ink(pg([(42, 86), (34, 68), (50, 84)], close=True)),
                ink(pg([(70, 84), (82, 66), (74, 88)], close=True)),
                ink(ell(36, 112, 10, 7)),
                ink(ell(78, 118, 9, 6)),
                ink(ell(40, 118, 12, 9)),
            ),
            step(
                "Add spots, eyes, and a nose.",
                ink(circ(100, 112, 10), width=THIN),
                ink(ell(130, 128, 12, 8), width=THIN),
                ink(circ(150, 116, 7), width=THIN),
                dot_eyes(58, 104, gap=16, r=2.8),
                nose(36, 118, 2.2),
                ink(circ(44, 120, 1.6), width=1.5, fill=True),
            ),
            step(
                "Draw four legs and a thin tail with a tuft.",
                lines([(80, 150, 76, 182), (100, 152, 98, 184), (132, 152, 136, 184), (152, 148, 158, 180)]),
                ink(smooth([(160, 112), (182, 124), (176, 148)]), width=THIN),
                ink(circ(174, 154, 5), width=THIN),
            ),
        ],
    )


def pig() -> dict:
    return subject(
        "pig",
        "Pig",
        "animals",
        ["pig", "pigs", "piggy", "piglet", "hog"],
        [
            step("Draw a big oval body.", ink(ell(108, 118, 50, 34))),
            step("Add a circle head on the left, overlapping the body.", ink(circ(58, 112, 28))),
            step(
                "Draw a snout oval with two nostrils, and two triangle ears.",
                ink(ell(34, 120, 14, 11)),
                ink(circ(28, 118, 2), width=2, fill=True),
                ink(circ(38, 122, 2), width=2, fill=True),
                ink(pg([(40, 90), (28, 68), (54, 88)], close=True)),
                ink(pg([(72, 90), (88, 70), (78, 96)], close=True)),
            ),
            step(
                "Add eyes and a smile.",
                dot_eyes(62, 104, gap=16, r=2.8),
                smile(58, 112, 14, 6),
            ),
            step(
                "Draw four short legs and a curly tail.",
                lines([(86, 146, 82, 172), (104, 148, 102, 174), (128, 148, 132, 174), (146, 144, 152, 170)]),
                ink(spiral(168, 104, 4, 14, 1.15, a0=0.4), width=THIN),
            ),
        ],
    )


def duck() -> dict:
    return subject(
        "duck",
        "Duck",
        "animals",
        ["duck", "ducks", "ducky", "duckling"],
        [
            step("Draw a low oval body.", ink(ell(96, 124, 42, 26))),
            step("Add a round head.", ink(circ(142, 86, 22))),
            step(
                "Draw a wide flat beak.",
                ink(ell(172, 92, 18, 8)),
                ink(ln(156, 92, 188, 92), width=THIN),
            ),
            step(
                "Add a wing and an eye.",
                ink(ell(90, 122, 18, 12)),
                ink(circ(148, 80, 2.8), width=2, fill=True),
            ),
            step(
                "Draw two webbed feet.",
                ink(pg([(80, 148), (62, 168), (96, 164)], close=True)),
                ink(pg([(112, 150), (108, 172), (136, 164)], close=True)),
            ),
        ],
    )


def frog() -> dict:
    return subject(
        "frog",
        "Frog",
        "animals",
        ["frog", "frogs", "toad"],
        [
            step("Draw a wide oval body.", ink(ell(100, 124, 52, 32))),
            step(
                "Sit two big circles on top for the eyes.",
                ink(circ(70, 78, 18)),
                ink(circ(130, 78, 18)),
                ink(circ(70, 78, 7), width=2, fill=True),
                ink(circ(130, 78, 7), width=2, fill=True),
            ),
            step("Add a big smile.", ink(arc(100, 118, 28, 18, 200, 340), width=W)),
            step(
                "Draw two bent back legs and two small front feet.",
                ink(smooth([(58, 140), (28, 150), (22, 176), (48, 178)]), width=W),
                ink(smooth([(142, 140), (174, 150), (180, 176), (154, 178)]), width=W),
                ink(ell(78, 150, 10, 6), width=THIN),
                ink(ell(122, 150, 10, 6), width=THIN),
            ),
        ],
    )


def turtle() -> dict:
    return subject(
        "turtle",
        "Turtle",
        "animals",
        ["turtle", "turtles", "tortoise"],
        [
            step("Draw a big dome for the shell. An oval is enough.", ink(ell(100, 112, 58, 40))),
            step(
                "Divide the shell with one line across and one line down, then add a small center oval.",
                ink(ln(48, 112, 152, 112), width=THIN),
                ink(ln(100, 76, 100, 148), width=THIN),
                ink(ell(100, 112, 16, 12), width=THIN),
            ),
            step("Add a small head sticking out on the right.", ink(circ(162, 112, 14))),
            step(
                "Draw four feet and a tiny tail.",
                ink(ell(62, 150, 14, 8)),
                ink(ell(100, 158, 14, 8)),
                ink(ell(138, 150, 12, 8)),
                ink(ell(70, 86, 12, 7)),
                ink(pg([(46, 112), (28, 106), (28, 118)], close=True)),
            ),
            step(
                "Add an eye and a smile on the head.",
                ink(circ(168, 108, 2.2), width=2, fill=True),
                smile(164, 116, 10, 4),
            ),
        ],
    )


def butterfly() -> dict:
    return subject(
        "butterfly",
        "Butterfly",
        "animals",
        ["butterfly", "butterflies", "buterfly"],
        [
            step(
                "Draw a long thin body and a small head.",
                ink(ell(100, 112, 8, 32)),
                ink(circ(100, 70, 10)),
            ),
            step(
                "Add two big upper wings.",
                ink(ell(62, 96, 30, 24)),
                ink(ell(138, 96, 30, 24)),
            ),
            step(
                "Add two smaller lower wings.",
                ink(ell(68, 140, 22, 18)),
                ink(ell(132, 140, 22, 18)),
            ),
            step(
                "Draw two antennae with dots on the ends.",
                ink(curve(96, 62, 70, 36, 62, 28), width=THIN),
                ink(curve(104, 62, 130, 36, 138, 28), width=THIN),
                ink(circ(62, 26, 3.2), width=2, fill=True),
                ink(circ(138, 26, 3.2), width=2, fill=True),
            ),
            step(
                "Decorate the wings with circles, and add a smile.",
                ink(circ(58, 92, 6), width=THIN),
                ink(circ(142, 92, 6), width=THIN),
                ink(circ(66, 138, 4), width=THIN),
                ink(circ(134, 138, 4), width=THIN),
                smile(100, 72, 10, 4),
            ),
        ],
    )


def elephant() -> dict:
    return subject(
        "elephant",
        "Elephant",
        "animals",
        ["elephant", "elephants", "elefant"],
        [
            step("Draw a large oval body.", ink(ell(118, 118, 48, 36))),
            step("Add a round head on the left.", ink(circ(68, 100, 28))),
            step("Draw a big ear on the head.", ink(ell(42, 108, 24, 30))),
            step(
                "Add a trunk that curls at the end, and one tusk.",
                ink(smooth([(58, 118), (40, 140), (36, 168), (58, 172)]), width=W),
                ink(curve(78, 118, 96, 132, 88, 142), width=THIN),
            ),
            step(
                "Draw four legs, an eye, and a thin tail.",
                lines([(92, 146, 88, 182), (112, 148, 110, 184), (136, 148, 140, 184), (156, 144, 162, 178)]),
                ink(circ(78, 92, 2.8), width=2, fill=True),
                ink(smooth([(162, 108), (186, 116), (180, 136)]), width=THIN),
            ),
        ],
    )


def lion() -> dict:
    return subject(
        "lion",
        "Lion",
        "animals",
        ["lion", "lions", "lioness"],
        [
            step("Draw a big circle. This is the mane.", ink(circ(100, 86, 48))),
            step("Draw a smaller circle inside for the face.", ink(circ(100, 90, 28))),
            step(
                "Add two round ears on the mane.",
                ink(circ(62, 52, 12)),
                ink(circ(138, 52, 12)),
            ),
            step(
                "Draw eyes, a nose, and a mouth.",
                dot_eyes(100, 86, gap=18, r=3),
                nose(100, 100, 3),
                ink(ln(100, 102, 100, 110), width=THIN),
                smile(100, 110, 16, 6),
            ),
            step(
                "Add a small body, two paws, and a tail with a tuft.",
                ink(ell(100, 158, 36, 18)),
                ink(ell(78, 176, 12, 6)),
                ink(ell(122, 176, 12, 6)),
                ink(smooth([(132, 150), (164, 156), (176, 140)]), width=THIN),
                ink(circ(180, 134, 6), width=THIN),
            ),
        ],
    )


def mouse() -> dict:
    return subject(
        "mouse",
        "Mouse",
        "animals",
        ["mouse", "mice", "mous"],
        [
            step("Draw a circle for the head and body.", ink(circ(96, 112, 32))),
            step(
                "Add two very big round ears.",
                ink(circ(62, 74, 22)),
                ink(circ(118, 66, 22)),
                ink(circ(62, 74, 10), width=THIN),
                ink(circ(118, 66, 10), width=THIN),
            ),
            step(
                "Draw eyes, a nose, and a smile.",
                dot_eyes(96, 108, gap=18, r=3),
                nose(112, 122, 2.8),
                smile(100, 124, 16, 6),
            ),
            step(
                "Add a long thin tail curling to the right.",
                ink(smooth([(124, 130), (160, 150), (178, 132), (168, 108), (184, 96)]), width=THIN),
            ),
            step(
                "Draw two tiny feet and three whiskers.",
                ink(ell(80, 144, 10, 5), width=THIN),
                ink(ell(110, 146, 10, 5), width=THIN),
                lines([(112, 118, 150, 110), (114, 124, 154, 124), (112, 130, 148, 136)]),
            ),
        ],
    )


def owl() -> dict:
    return subject(
        "owl",
        "Owl",
        "animals",
        ["owl", "owls", "owlet"],
        [
            step("Draw a tall oval body.", ink(ell(100, 116, 42, 52))),
            step(
                "Add two large eye circles.",
                ink(circ(82, 104, 16)),
                ink(circ(118, 104, 16)),
                ink(circ(82, 104, 5), width=2, fill=True),
                ink(circ(118, 104, 5), width=2, fill=True),
            ),
            step(
                "Draw a small triangle beak and two ear tufts.",
                ink(pg([(100, 116), (92, 128), (108, 128)], close=True)),
                ink(pg([(70, 70), (78, 42), (96, 68)], close=True)),
                ink(pg([(130, 70), (122, 42), (104, 68)], close=True)),
            ),
            step(
                "Add a curved wing on each side and a few belly marks.",
                ink(curve(58, 112, 26, 132, 52, 158), width=W),
                ink(curve(142, 112, 174, 132, 148, 158), width=W),
                lines([(86, 146, 96, 154), (104, 146, 114, 154), (84, 160, 96, 168), (104, 160, 116, 168)], width=THIN),
            ),
            step(
                "Draw two feet.",
                lines([(88, 164, 80, 180), (88, 164, 96, 180), (112, 164, 106, 180), (112, 164, 122, 180)], width=THIN),
            ),
        ],
    )


def penguin() -> dict:
    return subject(
        "penguin",
        "Penguin",
        "animals",
        ["penguin", "penguins", "pengin"],
        [
            step("Draw a tall oval for the body.", ink(ell(100, 112, 40, 56))),
            step("Draw a smaller oval inside for the white belly.", ink(ell(100, 126, 24, 34), width=THIN)),
            step(
                "Add two eyes and a triangle beak.",
                dot_eyes(100, 78, gap=18, r=3.2),
                ink(pg([(112, 88), (132, 94), (112, 100)], close=True)),
            ),
            step(
                "Draw a wing on each side.",
                ink(ell(62, 120, 12, 28)),
                ink(ell(138, 120, 12, 28)),
            ),
            step(
                "Add two flat feet.",
                ink(ell(82, 170, 16, 7)),
                ink(ell(118, 170, 16, 7)),
            ),
        ],
    )


def bear() -> dict:
    return subject(
        "bear",
        "Bear",
        "animals",
        ["bear", "bears", "teddy", "teddy bear"],
        [
            step("Draw a round head.", ink(circ(100, 78, 32))),
            step(
                "Add two round ears.",
                ink(circ(72, 50, 14)),
                ink(circ(128, 50, 14)),
                ink(circ(72, 50, 6), width=THIN),
                ink(circ(128, 50, 6), width=THIN),
            ),
            step("Draw an oval snout.", ink(ell(100, 96, 16, 12))),
            step("Add an oval body under the head.", ink(ell(100, 146, 40, 30))),
            step(
                "Draw eyes, a nose, a smile, and two short legs.",
                dot_eyes(100, 74, gap=20, r=3),
                nose(100, 94, 3.4),
                smile(100, 104, 14, 5),
                ink(ell(78, 174, 14, 8)),
                ink(ell(122, 174, 14, 8)),
            ),
        ],
    )


def fox() -> dict:
    return subject(
        "fox",
        "Fox",
        "animals",
        ["fox", "foxes", "foxy"],
        [
            step("Draw an oval body.", ink(ell(112, 128, 38, 26))),
            step(
                "Add a round head and a pointy snout.",
                ink(circ(74, 100, 22)),
                ink(pg([(58, 96), (28, 108), (58, 116)], close=True)),
            ),
            step(
                "Draw two triangle ears that do not cross.",
                ink(pg([(58, 84), (46, 46), (78, 78)], close=True)),
                ink(pg([(86, 80), (108, 40), (100, 88)], close=True)),
            ),
            step(
                "Draw a big bushy tail.",
                ink(ell(164, 112, 28, 16)),
                ink(pg([(186, 104), (198, 88), (188, 118)], close=True)),
            ),
            step(
                "Add four legs, an eye, a nose, and a smile.",
                lines([(90, 148, 86, 180), (108, 150, 106, 182), (128, 150, 132, 182), (146, 146, 152, 176)]),
                ink(circ(66, 96, 2.6), width=2, fill=True),
                nose(32, 108, 2.4),
                smile(70, 112, 14, 5),
            ),
        ],
    )


def whale() -> dict:
    return subject(
        "whale",
        "Whale",
        "animals",
        ["whale", "whales"],
        [
            step("Draw a very wide oval body.", ink(ell(104, 112, 62, 32))),
            step(
                "Add a tail with two flukes on the left.",
                ink(pg([(46, 112), (16, 86), (28, 112)], close=True)),
                ink(pg([(46, 112), (16, 140), (30, 116)], close=True)),
            ),
            step(
                "Draw a top fin and a small bottom fin.",
                ink(pg([(120, 82), (146, 48), (150, 84)], close=True)),
                ink(pg([(130, 140), (150, 162), (156, 136)], close=True)),
            ),
            step(
                "Add an eye, a smile, and a curved waterspout.",
                ink(circ(150, 104, 3), width=2, fill=True),
                smile(142, 116, 18, 6),
                ink(curve(96, 82, 78, 48, 64, 36), width=THIN),
                ink(curve(104, 80, 108, 40, 124, 34), width=THIN),
                ink(curve(112, 84, 132, 56, 140, 44), width=THIN),
            ),
        ],
    )


def shark() -> dict:
    return subject(
        "shark",
        "Shark",
        "animals",
        ["shark", "sharks"],
        [
            step("Draw a long pointed body. Start with a wide oval.", ink(ell(108, 108, 58, 26))),
            step(
                "Add a triangle nose on the left and a forked tail on the right.",
                ink(pg([(52, 108), (18, 96), (18, 120)], close=True)),
                ink(pg([(162, 100), (192, 70), (176, 108)], close=True)),
                ink(pg([(162, 116), (192, 146), (176, 112)], close=True)),
            ),
            step(
                "Draw the tall top fin and a side fin.",
                ink(pg([(100, 84), (124, 36), (138, 86)], close=True)),
                ink(pg([(120, 126), (148, 150), (150, 124)], close=True)),
            ),
            step(
                "Add an eye, gill lines, and a zigzag mouth.",
                ink(circ(48, 100, 3), width=2, fill=True),
                lines([(70, 96, 70, 116), (78, 94, 78, 118), (86, 96, 86, 116)], width=THIN),
                ink(pg([(36, 114), (46, 120), (56, 114), (66, 120), (76, 114)]), width=THIN),
            ),
        ],
    )


def dinosaur() -> dict:
    return subject(
        "dinosaur",
        "Dinosaur",
        "animals",
        ["dinosaur", "dinosaurs", "dino", "t rex", "trex", "t-rex"],
        [
            step("Draw a big oval body.", ink(ell(118, 118, 36, 28))),
            step(
                "Add a large head on the left and an open smile.",
                ink(ell(62, 78, 30, 22)),
                ink(pg([(36, 86), (16, 96), (34, 100)], close=True)),
                smile(52, 88, 22, 8),
                ink(circ(48, 70, 3), width=2, fill=True),
            ),
            step(
                "Draw a long tail to the right.",
                ink(smooth([(146, 112), (172, 100), (190, 112), (176, 128)]), width=W),
                ink(ln(146, 124, 188, 124), width=W),
            ),
            step(
                "Add two strong legs and feet.",
                ink(pg([(100, 140), (88, 176), (108, 176), (112, 150)], close=True)),
                ink(pg([(128, 142), (124, 178), (148, 178), (146, 148)], close=True)),
                ink(ln(82, 176, 112, 176), width=THIN),
                ink(ln(118, 178, 154, 178), width=THIN),
            ),
            step(
                "Draw two tiny arms.",
                ink(smooth([(96, 108), (80, 112), (70, 104)]), width=THIN),
                ink(smooth([(104, 112), (92, 122), (84, 116)]), width=THIN),
            ),
        ],
    )


def snake() -> dict:
    return subject(
        "snake",
        "Snake",
        "animals",
        ["snake", "snakes"],
        [
            step(
                "Draw a big S for the body. Make the line nice and thick.",
                ink(smooth([(40, 46), (120, 40), (160, 78), (70, 100), (40, 140), (110, 168), (168, 156)]), width=12),
            ),
            step("Add a circle head at the top of the S.", ink(circ(40, 40, 16))),
            step(
                "Draw a forked tongue and an eye.",
                lines([(26, 36, 10, 28), (26, 36, 12, 40)], width=THIN),
                ink(circ(34, 36, 2.6), width=2, fill=True),
            ),
            step(
                "Add a smile.",
                smile(36, 44, 12, 5),
            ),
        ],
    )


def spider() -> dict:
    return subject(
        "spider",
        "Spider",
        "animals",
        ["spider", "spiders"],
        [
            step(
                "Draw two circles: a round body and a smaller head.",
                ink(circ(100, 112, 28)),
                ink(circ(100, 74, 16)),
            ),
            step(
                "Add four bent legs on the left.",
                ink(pg([(76, 96), (40, 70), (22, 78)])),
                ink(pg([(74, 108), (36, 104), (18, 116)])),
                ink(pg([(74, 120), (38, 136), (24, 156)])),
                ink(pg([(80, 132), (52, 156), (40, 176)])),
            ),
            step(
                "Add four bent legs on the right.",
                ink(pg([(124, 96), (160, 70), (178, 78)])),
                ink(pg([(126, 108), (164, 104), (182, 116)])),
                ink(pg([(126, 120), (162, 136), (176, 156)])),
                ink(pg([(120, 132), (148, 156), (160, 176)])),
            ),
            step(
                "Draw eyes and a smile on the head.",
                dot_eyes(100, 72, gap=10, r=2.4),
                smile(100, 80, 12, 4),
            ),
        ],
    )


def bee() -> dict:
    return subject(
        "bee",
        "Bee",
        "animals",
        ["bee", "bees", "bumblebee", "bumble bee"],
        [
            step("Draw an oval body.", ink(ell(100, 116, 28, 36))),
            step("Add a round head.", ink(circ(100, 70, 16))),
            step(
                "Draw three stripe lines across the body and a small stinger.",
                lines([(76, 104, 124, 104), (74, 118, 126, 118), (78, 132, 122, 132)], width=THIN),
                ink(pg([(100, 150), (92, 168), (108, 168)], close=True)),
            ),
            step(
                "Add two wings.",
                ink(ell(68, 96, 20, 12)),
                ink(ell(132, 96, 20, 12)),
            ),
            step(
                "Draw antennae, eyes, and a smile.",
                ink(curve(92, 58, 74, 40, 70, 28), width=THIN),
                ink(curve(108, 58, 126, 40, 130, 28), width=THIN),
                ink(circ(70, 26, 3), width=2, fill=True),
                ink(circ(130, 26, 3), width=2, fill=True),
                dot_eyes(100, 68, gap=10, r=2.4),
                smile(100, 78, 12, 4),
            ),
        ],
    )


def sheep() -> dict:
    return subject(
        "sheep",
        "Sheep",
        "animals",
        ["sheep", "lamb", "lambs"],
        [
            step("Draw an oval body.", ink(ell(104, 122, 40, 28))),
            step(
                "Add fluffy circles around the body.",
                ink(circ(70, 104, 16), width=THIN),
                ink(circ(100, 90, 16), width=THIN),
                ink(circ(136, 102, 16), width=THIN),
                ink(circ(78, 140, 14), width=THIN),
                ink(circ(132, 140, 14), width=THIN),
            ),
            step("Draw a head circle on the left.", ink(circ(52, 112, 18))),
            step(
                "Add ears, eyes, and a nose.",
                ink(ell(34, 104, 8, 5)),
                ink(ell(40, 126, 7, 4)),
                dot_eyes(52, 110, gap=10, r=2.2),
                nose(40, 116, 2.2),
            ),
            step(
                "Draw four short legs.",
                lines([(82, 148, 78, 178), (100, 150, 98, 180), (118, 150, 120, 180), (136, 146, 142, 176)]),
            ),
        ],
    )


def crab() -> dict:
    return subject(
        "crab",
        "Crab",
        "animals",
        ["crab", "crabs"],
        [
            step("Draw a wide oval body.", ink(ell(100, 110, 46, 30))),
            step(
                "Add an eye stalk on each side and a round eye.",
                lines([(78, 82, 64, 58), (122, 82, 136, 58)], width=THIN),
                ink(circ(62, 52, 8)),
                ink(circ(138, 52, 8)),
                ink(circ(62, 52, 3), width=2, fill=True),
                ink(circ(138, 52, 3), width=2, fill=True),
            ),
            step(
                "Draw two claws. Each claw is a circle with a small opening.",
                ink(circ(36, 100, 16)),
                ink(circ(164, 100, 16)),
                ink(ln(36, 86, 36, 78), width=THIN),
                ink(ln(164, 86, 164, 78), width=THIN),
            ),
            step(
                "Add three legs on each side and a smile.",
                lines(
                    [
                        (62, 128, 40, 148),
                        (70, 136, 48, 162),
                        (84, 138, 74, 168),
                        (138, 128, 160, 148),
                        (130, 136, 152, 162),
                        (116, 138, 126, 168),
                    ]
                ),
                smile(100, 112, 24, 10),
            ),
        ],
    )


def octopus() -> dict:
    return subject(
        "octopus",
        "Octopus",
        "animals",
        ["octopus", "octopuses", "octopi"],
        [
            step("Draw a big round head.", ink(circ(100, 70, 36))),
            step(
                "Add four curling legs on the left.",
                ink(smooth([(78, 98), (50, 120), (40, 150), (58, 168)]), width=W),
                ink(smooth([(88, 104), (70, 130), (62, 160), (78, 178)]), width=W),
                ink(smooth([(96, 106), (90, 140), (96, 168)]), width=W),
                ink(smooth([(70, 96), (36, 110), (28, 140)]), width=W),
            ),
            step(
                "Add four curling legs on the right.",
                ink(smooth([(122, 98), (150, 120), (160, 150), (142, 168)]), width=W),
                ink(smooth([(112, 104), (130, 130), (138, 160), (122, 178)]), width=W),
                ink(smooth([(104, 106), (110, 140), (104, 168)]), width=W),
                ink(smooth([(130, 96), (164, 110), (172, 140)]), width=W),
            ),
            step(
                "Draw two big eyes and a smile.",
                eyes(100, 72, gap=24, r=8, pupil=3.4),
                smile(100, 90, 18, 8),
            ),
        ],
    )


def giraffe() -> dict:
    return subject(
        "giraffe",
        "Giraffe",
        "animals",
        ["giraffe", "giraffes"],
        [
            step("Draw a very long neck. A tall rounded rectangle works.", ink(rr(88, 36, 28, 90, 12))),
            step(
                "Add a head at the top, two little horns, and an ear.",
                ink(ell(118, 36, 24, 14)),
                ink(circ(104, 20, 4), width=THIN),
                ink(circ(118, 16, 4), width=THIN),
                ink(ell(142, 34, 7, 4)),
            ),
            step("Draw an oval body under the neck.", ink(ell(112, 140, 36, 22))),
            step(
                "Add four long legs and a tail.",
                lines([(90, 158, 86, 190), (106, 160, 104, 192), (124, 160, 128, 192), (140, 156, 148, 188)]),
                ink(smooth([(146, 136), (170, 146), (176, 132)]), width=THIN),
            ),
            step(
                "Decorate with spot circles, an eye, and a smile.",
                ink(circ(102, 60, 5), width=THIN),
                ink(circ(108, 82, 4), width=THIN),
                ink(circ(96, 104, 5), width=THIN),
                ink(circ(100, 132, 6), width=THIN),
                ink(circ(126, 146, 5), width=THIN),
                ink(circ(128, 34, 2.2), width=2, fill=True),
                smile(124, 40, 12, 4),
            ),
        ],
    )


def monkey() -> dict:
    return subject(
        "monkey",
        "Monkey",
        "animals",
        ["monkey", "monkeys", "ape"],
        [
            step("Draw a round head.", ink(circ(96, 78, 30))),
            step(
                "Add two big round ears.",
                ink(circ(62, 78, 14)),
                ink(circ(130, 78, 14)),
                ink(circ(62, 78, 6), width=THIN),
                ink(circ(130, 78, 6), width=THIN),
            ),
            step("Draw an oval body.", ink(ell(100, 140, 32, 28))),
            step(
                "Add a face oval, eyes, nostrils, and a smile.",
                ink(ell(96, 88, 16, 14), width=THIN),
                dot_eyes(96, 74, gap=16, r=2.8),
                ink(circ(92, 90, 1.8), width=1.5, fill=True),
                ink(circ(102, 90, 1.8), width=1.5, fill=True),
                smile(96, 98, 14, 6),
            ),
            step(
                "Draw a curling tail and two arms.",
                ink(spiral(150, 150, 6, 22, 1.05, a0=1.0), width=THIN),
                ink(smooth([(74, 124), (48, 132), (40, 154)]), width=W),
                ink(smooth([(122, 124), (150, 118), (162, 132)]), width=W),
            ),
        ],
    )
