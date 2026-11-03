"""Animals. Each picture is built from circles, ovals, triangles, and a few curves."""

from shapes import (
    THIN,
    W,
    arc,
    circ,
    cloud_outline,
    curve,
    dot_eyes,
    ell,
    eyes,
    flame,
    ink,
    leaf,
    lines,
    ln,
    Path,
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
            step("Draw a long oval for the body.", ink(ell(104, 122, 42, 22))),
            step(
                "Add four straight legs, and a short hoof line at each foot.",
                lines([(76, 140, 72, 176), (96, 142, 94, 178), (122, 142, 126, 178), (140, 138, 148, 174)]),
                lines([(66, 176, 80, 176), (86, 178, 102, 178), (118, 178, 136, 178), (140, 174, 156, 174)], width=THIN),
            ),
            step(
                "Draw a neck that meets the body, then an oval head and one ear.",
                ink(pg([(126, 108), (150, 74), (164, 64), (156, 86), (136, 120)], close=True)),
                ink(ell(178, 64, 18, 12)),
                ink(pg([(168, 56), (164, 34), (184, 52)], close=True)),
            ),
            step(
                "Add a short mane above the neck, plus an eye.",
                lines([(150, 66, 140, 52), (142, 78, 130, 64), (134, 92, 122, 80)], width=THIN),
                ink(circ(184, 62, 2.4), width=2, fill=True),
            ),
            step(
                "Finish with a curved tail on the left.",
                ink(smooth([(64, 110), (40, 118), (32, 146), (48, 162)]), width=W),
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
            step("Draw a large oval body.", ink(ell(122, 118, 40, 30))),
            step("Add a round head on the left, touching the body.", ink(circ(70, 112, 24))),
            step(
                "Draw one big ear on top of the head.",
                ink(ell(62, 82, 16, 20)),
            ),
            step(
                "Add a trunk that starts at the bottom of the head and curls.",
                ink(smooth([(64, 126), (46, 146), (36, 168), (56, 178)]), width=W),
            ),
            step(
                "Draw four legs, an eye, and a thin tail.",
                lines([(96, 144, 92, 180), (114, 146, 112, 182), (136, 146, 140, 182), (154, 142, 160, 176)]),
                ink(circ(78, 106, 2.6), width=2, fill=True),
                ink(smooth([(158, 104), (178, 112), (172, 132)]), width=THIN),
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
            step("Draw an oval body.", ink(ell(116, 128, 34, 20))),
            step(
                "Add a head that touches the body, a pointy snout, and two ears.",
                ink(circ(76, 112, 18)),
                ink(pg([(62, 108), (36, 116), (64, 122)], close=True)),
                ink(pg([(64, 98), (58, 66), (80, 94)], close=True)),
                ink(pg([(84, 96), (98, 62), (96, 100)], close=True)),
            ),
            step(
                "Draw a bushy tail behind the body, with a pointed tip.",
                ink(ell(164, 110, 22, 13)),
                ink(pg([(182, 104), (196, 110), (182, 118)], close=True)),
            ),
            step(
                "Add four short legs.",
                lines([(96, 146, 92, 176), (112, 148, 110, 178), (130, 148, 134, 178), (146, 144, 152, 172)]),
            ),
            step(
                "Finish the face with an eye, a nose, and a smile.",
                ink(circ(70, 108, 2.4), width=2, fill=True),
                nose(40, 116, 2.2),
                smile(72, 118, 12, 4),
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
            step("Draw a fat oval body.", ink(ell(112, 120, 48, 28))),
            step("Add a big rounded head on the right.", ink(rr(140, 96, 46, 48, 14))),
            step(
                "Draw a narrow tail and a flat oval fluke.",
                ink(pg([(66, 110), (32, 114), (32, 128), (66, 124)], close=True)),
                ink(ell(20, 120, 16, 7)),
            ),
            step(
                "Add a spout: a short line and a small cloud.",
                ink(ln(156, 96, 156, 70), width=THIN),
                ink(cloud_outline(156, 52, 36, 22), width=THIN),
            ),
            step(
                "Draw an eye, a smile, and one oval flipper.",
                ink(circ(168, 114, 2.6), width=2, fill=True),
                smile(160, 128, 16, 6),
                ink(ell(118, 146, 14, 7)),
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
            step("Draw an oval body.", ink(ell(118, 122, 34, 24))),
            step(
                "Add a big head that touches the body, and a long snout.",
                ink(ell(68, 90, 26, 20)),
                ink(pg([(46, 86), (14, 100), (48, 108)], close=True)),
            ),
            step(
                "Draw a tail that gets thinner toward the tip.",
                ink(pg([(148, 108), (188, 98), (186, 116), (148, 132)], close=True)),
            ),
            step(
                "Add two strong legs with flat feet.",
                ink(pg([(104, 142), (96, 172), (116, 172), (118, 146)], close=True)),
                ink(pg([(128, 144), (126, 174), (148, 174), (142, 146)], close=True)),
            ),
            step(
                "Draw a tiny arm in front of the body, an eye, and a smile.",
                ink(smooth([(90, 112), (74, 126), (64, 116)]), width=THIN),
                ink(circ(58, 84, 2.6), width=2, fill=True),
                smile(62, 98, 16, 6),
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
                "Draw a long S for the body. Keep the two edges the same distance apart.",
                ink(_snake_body()),
            ),
            step(
                "Add a forked tongue at the head.",
                lines([(36, 56, 18, 46), (36, 56, 20, 64)], width=THIN),
            ),
            step(
                "Draw an eye on the head.",
                ink(circ(52, 54, 2.4), width=2, fill=True),
            ),
            step(
                "Add a small smile on the head.",
                smile(56, 62, 10, 4),
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
            step(
                "Draw one bumpy cloud shape for the wool.",
                ink(cloud_outline(118, 118, 96, 72)),
            ),
            step("Add a round head that touches the wool.", ink(circ(68, 122, 16))),
            step(
                "Draw two small ears on the head.",
                ink(ell(54, 112, 7, 4)),
                ink(ell(56, 134, 7, 4)),
            ),
            step(
                "Add eyes and a nose.",
                dot_eyes(68, 120, gap=10, r=2.2),
                nose(56, 128, 2.2),
            ),
            step(
                "Draw four short legs under the wool.",
                lines([(96, 150, 92, 178), (112, 152, 110, 180), (132, 152, 136, 180), (148, 148, 154, 176)]),
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
            step("Draw an oval body, low on the page.", ink(ell(112, 146, 32, 18))),
            step(
                "Add a long neck. A tall rounded rectangle sits on the body.",
                ink(rr(100, 44, 20, 104, 8)),
            ),
            step(
                "Draw the head, two little horns, and one ear.",
                ink(ell(124, 40, 24, 13)),
                ink(ln(112, 30, 110, 16), width=THIN),
                ink(circ(110, 14, 3.2), width=THIN),
                ink(ln(126, 28, 130, 14), width=THIN),
                ink(circ(130, 12, 3.2), width=THIN),
                ink(ell(146, 42, 8, 5)),
            ),
            step(
                "Add four long legs and a short tail.",
                lines([(96, 162, 92, 186), (110, 164, 108, 188), (126, 164, 130, 188), (140, 160, 146, 184)]),
                ink(smooth([(142, 140), (164, 148), (170, 136)]), width=THIN),
            ),
            step(
                "Put three spots on the body only, then an eye and a smile.",
                ink(circ(104, 140, 4), width=THIN),
                ink(circ(122, 148, 3.5), width=THIN),
                ink(circ(112, 136, 3), width=THIN),
                ink(circ(132, 38, 2.2), width=2, fill=True),
                smile(128, 46, 12, 4),
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


def _snake_body() -> str:
    p = Path()
    p.M(36, 50)
    p.C(90, 28, 168, 36, 166, 96)
    p.C(164, 140, 100, 150, 130, 172)
    p.L(116, 184)
    p.C(78, 164, 146, 152, 148, 96)
    p.C(150, 52, 80, 46, 36, 64)
    p.Z()
    return p.text()

