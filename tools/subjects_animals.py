"""Animals, drawn from the side (or the front) with smooth pen lines.

Each picture follows the real animal's shape: the right body outline first,
then the legs, then the features that make it look like itself. Points marked
with a trailing 1 are sharp corners (ear tips, fin tips, hooves).
"""

from shapes import (
    THIN,
    W,
    circ,
    ell,
    ink,
    lines,
    ln,
    mirror,
    pg,
    scallop,
    sp,
    step,
    subject,
    tube,
    tube_bands,
)

LEG = 4.2


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


def dot(x: float, y: float, r: float = 2.8) -> dict:
    return ink(circ(x, y, r), width=2, fill=True)


def leg(x: float, top: float, w: float = 10, bottom: float = 178, hoof: bool = False, lean: float = 0) -> dict:
    """A straight leg with a foot. hoof=True gives a flat hoof band."""
    pts = [(x, top), (x + lean * 0.5, (top + bottom) / 2), (x + lean, bottom - 6)]
    pts += [(x + lean - 2, bottom, 1), (x + lean + w + 2, bottom, 1)]
    pts += [(x + lean + w, bottom - 6), (x + w + lean * 0.5, (top + bottom) / 2), (x + w, top)]
    strokes = [ink(sp(pts), width=LEG)]
    if hoof:
        strokes.append(ink(ln(x + lean, bottom - 7, x + lean + w, bottom - 7), width=2.4))
    return strokes


def leg_pair(x: float, top: float, w: float, shift: float, top_far: float | None = None, bottom: float = 178,
             hoof: bool = False) -> list[dict]:
    """A near leg plus the edge of the far leg peeking out beside it (shift < 0 is to the left)."""
    far_top = top if top_far is None else top_far
    strokes = leg(x, top, w=w, bottom=bottom, hoof=hoof)
    if shift < 0:
        xf = x + shift
        pts = [(xf, far_top), (xf, (far_top + bottom) / 2), (xf, bottom - 6), (xf - 2, bottom, 1), (x - 2, bottom, 1)]
        hoof_line = (xf, x)
    else:
        xf = x + w + shift
        pts = [(xf, far_top), (xf, (far_top + bottom) / 2), (xf, bottom - 6), (xf + 2, bottom, 1),
               (x + w + 2, bottom, 1)]
        hoof_line = (x + w, xf)
    strokes.append(ink(sp(pts), width=LEG))
    if hoof:
        strokes.append(ink(ln(hoof_line[0], bottom - 7, hoof_line[1], bottom - 7), width=2.4))
    return strokes



def cat() -> dict:
    return subject(
        "cat",
        "Cat",
        "animals",
        ["cat", "cats", "kitty", "kitten", "kittens", "kitties", "kat", "catt", "kitteh"],
        [
            step(
                "Draw a round head with two pointy ears on top.",
                ink(sp([(52, 66), (50, 48), (54, 22, 1), (68, 34), (82, 33), (96, 20, 1),
                        (98, 46), (96, 64), (88, 78), (74, 84), (60, 80)], closed=True)),
            ),
            step(
                "Draw the back curving down from the head, and the chest on the front.",
                ink(sp([(96, 64), (112, 84), (124, 116), (130, 148), (124, 172)])),
                ink(sp([(62, 82), (58, 106), (60, 140), (62, 172)])),
            ),
            step(
                "Add the big round back leg, two front legs, and a flat line on the ground.",
                ink(sp([(126, 140), (112, 124), (96, 132), (92, 154), (100, 172)])),
                ink(sp([(78, 112), (78, 140), (80, 170)])),
                ink(sp([(54, 174), (62, 168), (80, 170), (100, 172), (124, 172)])),
            ),
            step(
                "Draw a long, fluffy tail that wraps around in front of the feet.",
                ink(sp([(124, 170), (150, 174), (170, 164), (180, 142), (176, 122, 1),
                        (170, 140), (162, 156), (146, 164), (126, 164)])),
            ),
            step(
                "Finish the face: almond eyes, a small triangle nose, a mouth, and whiskers.",
                ink(sp([(62, 56), (67, 52), (72, 56), (67, 60)], closed=True), width=THIN),
                ink(sp([(80, 56), (85, 52), (90, 56), (85, 60)], closed=True), width=THIN),
                ink(ln(67, 53, 67, 59), width=2.4),
                ink(ln(85, 53, 85, 59), width=2.4),
                ink(pg([(72, 66), (80, 66), (76, 71)], close=True), width=2, fill=True),
                ink(sp([(70, 76), (73, 77), (76, 72), (79, 77), (82, 76)]), width=2.4),
                lines([(64, 70, 40, 64), (64, 74, 40, 76), (88, 70, 112, 64), (88, 74, 112, 76)], width=2),
                ink(sp([(58, 30), (60, 42)]), width=2),
                ink(sp([(93, 28), (91, 42)]), width=2),
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
            step(
                "Draw the head from the side: a round top and a long snout pointing left.",
                ink(sp([(52, 48), (38, 52), (30, 62), (16, 66), (10, 74, 1), (14, 84), (28, 88),
                        (46, 92), (60, 84), (64, 62)], closed=True)),
            ),
            step(
                "Hang a long floppy ear from the top of the head.",
                ink(sp([(48, 52), (60, 56), (66, 72), (60, 88), (52, 84), (48, 66)], closed=True)),
            ),
            step(
                "Draw the back and the tummy. The back is long and nearly flat.",
                ink(sp([(64, 62), (78, 80), (110, 84), (144, 82), (158, 94), (160, 112)])),
                ink(sp([(54, 90), (64, 110), (78, 122), (102, 124), (122, 120)])),
            ),
            step(
                "Add four legs with little paws. The back legs bend like a zigzag.",
                ink(sp([(68, 116), (66, 150), (64, 172), (56, 178, 1), (74, 178, 1), (76, 168), (80, 140), (84, 122)])),
                ink(sp([(90, 124), (92, 150), (92, 172), (86, 178, 1), (102, 178, 1), (102, 166), (102, 140), (102, 124)])),
                ink(sp([(122, 120), (116, 146), (122, 162), (122, 172), (116, 178, 1), (132, 178, 1),
                        (132, 166), (134, 150)])),
                ink(sp([(140, 122), (136, 146), (144, 162), (144, 172), (138, 178, 1), (154, 178, 1),
                        (154, 166), (158, 148), (162, 128), (160, 110)])),
            ),
            step(
                "Draw a tail that curves up, then the eye, the nose, and the mouth.",
                ink(sp([(156, 90), (170, 80), (182, 56, 1), (178, 78), (160, 100)])),
                ink(circ(36, 66, 3), width=2, fill=True),
                ink(ell(13, 74, 4, 3.4), width=2, fill=True),
                ink(sp([(16, 84), (26, 86), (34, 82)]), width=THIN),
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
            step(
                "Draw a long body like a big raindrop lying down. Round nose on the left, thin at the tail on the right.",
                ink(sp([(22, 100), (40, 80), (78, 70), (120, 76), (152, 92), (172, 102, 1),
                        (150, 112), (114, 126), (74, 132), (40, 126), (24, 114)], closed=True)),
            ),
            step(
                "Add the tail fluke at the end: two pointy flaps, one up and one down.",
                ink(sp([(170, 100), (180, 92), (192, 74, 1), (190, 92), (184, 104, 1),
                        (192, 118), (194, 134, 1), (180, 118), (170, 106)])),
            ),
            step(
                "Draw a long curved mouth line from the nose, and a few belly lines under it.",
                ink(sp([(24, 107), (46, 110), (70, 110), (82, 106)]), width=THIN),
                ink(sp([(32, 115), (56, 119), (86, 120)]), width=2.4),
                ink(sp([(42, 121), (64, 125), (92, 125)]), width=2.4),
            ),
            step(
                "Add a long flipper under the body and a small fin on the back near the tail.",
                ink(sp([(74, 122), (88, 138), (104, 154, 1), (100, 136), (92, 124)])),
                ink(sp([(134, 84), (146, 76, 1), (150, 92)]), width=THIN),
            ),
            step(
                "Finish with an eye just above the end of the mouth, and a splashy spout on top of the head.",
                ink(circ(76, 101, 2.8), width=2, fill=True),
                ink(sp([(58, 74), (52, 56), (38, 46)]), width=THIN),
                ink(sp([(58, 74), (58, 52)]), width=THIN),
                ink(sp([(58, 74), (66, 56), (80, 48)]), width=THIN),
                ink(circ(34, 52, 2), width=1.5, fill=True),
                ink(circ(84, 54, 2), width=1.5, fill=True),
                ink(circ(58, 44, 2), width=1.5, fill=True),
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
            step(
                "Draw a round head on the left that flows into a plump body and a long tail.",
                ink(sp([(44, 66), (56, 52), (74, 54), (86, 68), (112, 80), (140, 98), (180, 124, 1),
                        (174, 136, 1), (138, 124), (110, 130), (80, 126), (58, 110), (46, 94), (42, 78)],
                       closed=True)),
            ),
            step(
                "Add a short pointy beak on the front of the head.",
                ink(sp([(45, 66), (26, 73, 1), (44, 78)])),
            ),
            step(
                "Draw a wing on the side of the body with a pointy tip near the tail.",
                ink(sp([(82, 90), (106, 88), (130, 100), (154, 122, 1), (126, 118), (100, 112), (84, 104)],
                       closed=True)),
                ink(sp([(104, 104), (124, 110), (140, 116)]), width=2.4),
            ),
            step(
                "Draw a branch, then two thin legs with toes holding on.",
                ink(sp([(20, 152), (80, 148), (140, 150), (186, 156)])),
                lines([(92, 128, 90, 148), (104, 128, 104, 148)], width=3),
                lines([(90, 148, 82, 152), (104, 148, 96, 152), (90, 148, 96, 153), (104, 148, 110, 153)], width=2.4),
            ),
            step(
                "Finish with a shiny eye and a little line where the beak opens.",
                dot(56, 68, 3),
                ink(ln(30, 73, 44, 72), width=2),
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
            step(
                "Draw an oval body that is pointy at the tail end.",
                ink(sp([(22, 100), (42, 78), (80, 66), (120, 74), (146, 94), (146, 106), (120, 126),
                        (80, 134), (42, 122)], closed=True)),
            ),
            step(
                "Add a tail shaped like a big V at the back.",
                ink(sp([(146, 94), (164, 82), (180, 70, 1), (172, 100), (180, 130, 1), (164, 118), (146, 106)])),
                ink(sp([(156, 96), (168, 100), (156, 104)]), width=2),
            ),
            step(
                "Draw a fin on top, a small fin underneath, and one on its side.",
                ink(sp([(68, 70), (86, 54), (114, 46, 1), (110, 60), (122, 78)])),
                ink(sp([(90, 132), (102, 148, 1), (114, 128)])),
                ink(sp([(70, 106), (86, 98), (96, 114, 1), (78, 114)], closed=True), width=THIN),
            ),
            step(
                "Draw a curved gill line behind the head, a mouth, and a round eye.",
                ink(sp([(54, 80), (62, 100), (55, 121)])),
                ink(sp([(22, 100), (30, 104), (36, 103)]), width=2.4),
                ink(circ(40, 92, 6), width=THIN),
                dot(41, 92, 2.6),
            ),
            step(
                "Finish with a few curved scales on the body.",
                ink(sp([(80, 80), (86, 88), (80, 96)]), width=2.2),
                ink(sp([(96, 78), (102, 86), (96, 94)]), width=2.2),
                ink(sp([(88, 96), (94, 104), (88, 112)]), width=2.2),
                ink(sp([(104, 94), (110, 102), (104, 110)]), width=2.2),
                ink(sp([(96, 112), (102, 120), (96, 128)]), width=2.2),
                ink(sp([(112, 108), (118, 116), (112, 124)]), width=2.2),
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
            step(
                "Draw an oval head that leans forward, with a pointy nose on the left.",
                ink(sp([(30, 90, 1), (36, 74), (52, 64), (72, 66), (82, 80), (78, 96), (62, 104),
                        (44, 102)], closed=True)),
            ),
            step(
                "Add two long ears that point up and lean back.",
                ink(sp([(58, 66), (60, 38), (70, 14, 1), (80, 34), (72, 66)])),
                ink(sp([(72, 66), (84, 42), (102, 24, 1), (100, 46), (82, 74)])),
                ink(sp([(66, 60), (68, 40), (71, 26)]), width=2),
            ),
            step(
                "Draw a round back that curves down, and the chest under the head.",
                ink(sp([(80, 82), (110, 88), (138, 112), (150, 142), (142, 170)])),
                ink(sp([(50, 103), (50, 126), (58, 152), (64, 168)])),
            ),
            step(
                "Add a big back leg with a long foot, a short front leg, and a fluffy tail.",
                ink(sp([(140, 162), (126, 132), (104, 138), (98, 160), (104, 170)])),
                ink(sp([(142, 170), (110, 172), (82, 174), (68, 170), (80, 166), (100, 168)])),
                ink(sp([(66, 132), (66, 152), (62, 170), (52, 172, 1), (60, 166)])),
                ink(scallop(152, 146, 10, 10, n=6, puff=0.25), width=THIN),
            ),
            step(
                "Finish with an eye, a little nose, and whiskers.",
                dot(54, 78, 3.2),
                dot(31, 89, 2),
                lines([(36, 94, 12, 90), (36, 96, 14, 102), (38, 98, 20, 110)], width=2),
            ),
        ],
    )


def horse_body(mane: bool = True) -> list[dict]:
    """Head, neck, body, and legs shared by the horse and the unicorn."""
    return [
        step(
            "Draw the long head and the neck. The face slopes down to a soft nose on the left.",
            ink(sp([(92, 80), (76, 58), (60, 38), (56, 22, 1), (49, 36), (38, 42), (26, 58), (16, 72), (14, 80),
                    (20, 86), (34, 84), (46, 76), (56, 88), (64, 106)])),
        ),
        step(
            "Draw the back and the round rump, then the tummy line underneath.",
            ink(sp([(92, 80), (118, 85), (144, 82), (160, 92), (164, 110), (158, 124)])),
            ink(sp([(64, 106), (70, 120), (96, 126), (124, 122), (140, 122)])),
        ),
        step(
            "Add four long, thin legs with hooves. The back legs bend backward in the middle.",
            leg(70, 118, w=9, hoof=True, lean=-2),
            leg(90, 124, w=9, hoof=True, lean=2),
            ink(sp([(124, 122), (122, 140), (127, 152), (126, 170), (124, 178, 1), (136, 178, 1),
                    (135, 168), (136, 152), (138, 138)]), width=LEG),
            ink(sp([(140, 122), (138, 140), (144, 152), (142, 170), (140, 178, 1), (152, 178, 1),
                    (151, 168), (154, 152), (160, 134), (158, 124)]), width=LEG),
            ink(ln(124, 171, 136, 171), width=2.4),
            ink(ln(141, 171, 152, 171), width=2.4),
        ),
        step(
            "Draw a flowing mane down the neck and a long, wavy tail.",
            ink(sp([(58, 36), (68, 46), (70, 58), (82, 66), (86, 78)]), width=THIN),
            ink(sp([(62, 34), (76, 42), (80, 56), (92, 68)]), width=THIN),
            ink(sp([(162, 94), (178, 104), (182, 128), (176, 150), (182, 162)])),
            ink(sp([(162, 100), (170, 120), (166, 142), (170, 158)]), width=THIN),
        ),
    ]


def horse() -> dict:
    return subject(
        "horse",
        "Horse",
        "animals",
        ["horse", "horses", "pony", "ponies", "hors"],
        horse_body()
        + [
            step(
                "Finish the face: an eye, a nostril, and a mouth line.",
                dot(37, 52, 3),
                ink(sp([(19, 75), (22, 72), (24, 76)]), width=2.4),
                ink(ln(16, 84, 26, 82), width=2.4),
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
            step(
                "Draw a big, long body with a flat back and a square-ish rump on the right.",
                ink(sp([(58, 70), (100, 66), (148, 68), (164, 80), (166, 104), (158, 126), (130, 130),
                        (96, 130), (66, 126), (56, 104)], closed=True)),
            ),
            step(
                "Draw the head on the left. It is wide at the top and has a big nose at the bottom.",
                ink(sp([(58, 64), (42, 58), (26, 64), (20, 84), (18, 102), (24, 112), (40, 114), (52, 106),
                        (60, 88)], closed=True)),
                ink(sp([(20, 96), (32, 94), (44, 100)]), width=THIN),
            ),
            step(
                "Add ears that stick out sideways and two small curved horns.",
                ink(sp([(58, 66), (76, 60, 1), (64, 76)])),
                ink(sp([(44, 60), (44, 48), (52, 42, 1)]), width=THIN),
                ink(sp([(34, 60), (30, 48), (24, 44, 1)]), width=THIN),
            ),
            step(
                "Draw four short straight legs with hooves, a udder, and a thin tail with a tuft.",
                leg(64, 122, w=12, hoof=True),
                leg(84, 128, w=12, hoof=True),
                leg(124, 128, w=12, hoof=True),
                leg(144, 122, w=12, hoof=True),
                ink(sp([(108, 130), (110, 140), (120, 142), (124, 130)]), width=THIN),
                ink(sp([(166, 84), (174, 104), (174, 134)]), width=THIN),
                ink(sp([(174, 132), (170, 144, 1), (176, 140), (180, 146, 1), (176, 132)]), width=THIN),
            ),
            step(
                "Finish with big spots on the body, an eye, and two nostrils.",
                ink(sp([(84, 72), (102, 76), (108, 92), (94, 102), (80, 92)], closed=True), width=THIN),
                ink(sp([(124, 84), (144, 82), (152, 100), (138, 112), (122, 102)], closed=True), width=THIN),
                ink(sp([(70, 104), (82, 108), (80, 120), (68, 118)], closed=True), width=THIN),
                dot(34, 78, 3),
                dot(26, 104, 2),
                dot(36, 106, 2),
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
            step(
                "Draw a big round body like a fat bean.",
                ink(sp([(46, 92), (60, 70), (100, 62), (140, 68), (162, 90), (162, 116), (142, 132),
                        (100, 136), (64, 130), (46, 114)], closed=True)),
            ),
            step(
                "Add a short snout that ends in a flat oval nose on the left.",
                ink(sp([(48, 88), (36, 90)])),
                ink(sp([(48, 114), (36, 112)])),
                ink(ell(32, 101, 6, 11)),
                dot(31, 97, 1.8),
                dot(31, 105, 1.8),
            ),
            step(
                "Draw a floppy triangle ear on the head.",
                ink(sp([(64, 74), (78, 54, 1), (88, 78), (76, 84, 1)])),
            ),
            step(
                "Add four short legs with little hooves.",
                leg(62, 126, w=12, bottom=166, hoof=True),
                leg(80, 132, w=12, bottom=170, hoof=True),
                leg(120, 133, w=12, bottom=170, hoof=True),
                leg(138, 128, w=12, bottom=166, hoof=True),
            ),
            step(
                "Finish with a curly tail, an eye, and a smile.",
                ink(sp([(161, 96), (174, 88), (180, 98), (170, 104), (168, 94), (178, 84)]), width=THIN),
                dot(60, 88, 3),
                ink(sp([(40, 116), (50, 120), (58, 116)]), width=THIN),
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
            step(
                "Draw a body shaped like a boat, with a pointy tail up on the right.",
                ink(sp([(62, 110), (82, 98), (120, 96), (158, 92), (178, 80, 1), (172, 104), (150, 128),
                        (110, 140), (78, 136), (60, 124)], closed=True)),
            ),
            step(
                "Draw a curved neck going up to a round head.",
                ink(sp([(84, 98), (82, 82), (76, 66), (66, 52), (66, 38), (78, 30), (92, 34), (96, 48),
                        (92, 62), (94, 78), (104, 96)])),
            ),
            step(
                "Add a long flat bill on the front of the head.",
                ink(sp([(67, 42), (52, 42), (40, 48, 1), (52, 54), (68, 52)])),
                ink(ln(46, 48, 66, 47), width=2),
            ),
            step(
                "Draw the wing on the side with feather tips at the back.",
                ink(sp([(98, 106), (128, 100), (162, 96), (152, 110, 1), (156, 116), (140, 122, 1), (118, 124),
                        (100, 118)], closed=True)),
            ),
            step(
                "Finish with an eye and two legs with webbed feet.",
                dot(78, 42, 3),
                lines([(104, 139, 102, 160), (120, 137, 122, 160)], width=3),
                ink(pg([(102, 160), (86, 168), (110, 167)], close=True), width=THIN),
                ink(pg([(122, 160), (108, 168), (130, 167)], close=True), width=THIN),
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
            step(
                "Draw a body shaped like a hill, with a bump for the eye and a pointy nose on the left.",
                ink(sp([(22, 114, 1), (30, 100), (44, 90), (50, 76), (64, 72), (74, 84), (104, 88), (140, 104),
                        (160, 128), (152, 150), (120, 158), (80, 152), (48, 138), (28, 124)], closed=True)),
            ),
            step(
                "Draw a big round eye in the bump, and a long smile from the nose.",
                ink(circ(61, 82, 9), width=THIN),
                dot(59, 83, 4),
                ink(sp([(22, 114), (40, 118), (66, 112)]), width=THIN),
                ink(circ(84, 104, 6), width=2.4),
            ),
            step(
                "Draw the big folded back leg like an oval on the side of the body.",
                ink(sp([(106, 124), (130, 112), (156, 128), (152, 150), (122, 154), (104, 140)], closed=True)),
            ),
            step(
                "Add the long back foot on the ground with spread toes, and a front leg.",
                ink(sp([(150, 150), (130, 162), (100, 164), (76, 166)])),
                lines([(80, 166, 66, 160), (80, 166, 64, 168), (80, 166, 70, 176)], width=2.6),
                ink(sp([(56, 132), (54, 150), (48, 166)])),
                ink(sp([(66, 138), (64, 152), (60, 166)])),
                lines([(48, 166, 38, 168), (54, 166, 50, 174), (60, 166, 64, 172)], width=2.6),
            ),
            step(
                "Finish with a few round spots on the back.",
                ink(circ(110, 100, 5), width=2.2),
                ink(circ(128, 108, 4), width=2.2),
                ink(circ(96, 112, 4), width=2.2),
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
            step(
                "Draw a tall rounded shell like half an egg.",
                ink(sp([(36, 122), (48, 90), (82, 66), (122, 66), (156, 88), (170, 122)])),
                ink(sp([(32, 122), (100, 128), (174, 122)])),
            ),
            step(
                "Draw the pattern on the shell: a middle shape with lines going out.",
                ink(sp([(84, 84), (116, 84), (126, 104), (100, 116), (74, 104)], closed=True), width=THIN),
                lines([(84, 84, 76, 70), (116, 84, 124, 70), (126, 104, 154, 106), (74, 104, 46, 106),
                       (100, 116, 100, 127)], width=THIN),
            ),
            step(
                "Add a head on a neck sticking out of the front.",
                ink(sp([(44, 112), (30, 104), (16, 100), (8, 108), (12, 118), (28, 120), (42, 124)])),
            ),
            step(
                "Draw two stubby front and back legs with toes, and a little pointy tail.",
                ink(sp([(48, 124), (46, 140), (42, 150), (60, 150), (64, 140), (64, 126)])),
                ink(sp([(136, 126), (138, 140), (136, 150), (154, 150), (156, 140), (154, 124)])),
                lines([(46, 150, 46, 146), (53, 150, 53, 146), (140, 150, 140, 146), (147, 150, 147, 146)], width=2),
                ink(sp([(168, 116), (186, 126, 1), (170, 126)])),
            ),
            step(
                "Finish with an eye and a smile.",
                dot(18, 106, 2.8),
                ink(sp([(9, 112), (16, 114), (22, 113)]), width=2.2),
            ),
        ],
    )


def butterfly() -> dict:
    fore = [(97, 82), (72, 54), (40, 36), (22, 44), (24, 74), (46, 96), (96, 100)]
    hind = [(96, 104), (64, 104), (38, 122), (40, 150), (62, 160), (86, 142), (98, 116)]
    return subject(
        "butterfly",
        "Butterfly",
        "animals",
        ["butterfly", "butterflies", "buterfly"],
        [
            step(
                "Draw a thin body down the middle and a small round head on top.",
                ink(sp([(100, 70), (105, 80), (104, 112), (101, 138), (99, 138), (96, 112), (95, 80)], closed=True)),
                ink(circ(100, 64, 6)),
            ),
            step(
                "Draw two big top wings that point out to the corners.",
                ink(sp(fore, closed=True)),
                ink(sp(mirror(fore), closed=True)),
            ),
            step(
                "Draw two smaller round wings underneath.",
                ink(sp(hind, closed=True)),
                ink(sp(mirror(hind), closed=True)),
            ),
            step(
                "Add two curly feelers with dots on the ends.",
                ink(sp([(98, 59), (90, 38), (78, 26)]), width=THIN),
                ink(sp([(102, 59), (110, 38), (122, 26)]), width=THIN),
                dot(78, 26, 3),
                dot(122, 26, 3),
            ),
            step(
                "Decorate the wings with circles and lines. Make both sides match.",
                ink(circ(50, 62, 9), width=THIN),
                ink(circ(150, 62, 9), width=THIN),
                ink(circ(64, 132, 7), width=THIN),
                ink(circ(136, 132, 7), width=THIN),
                ink(sp([(94, 90), (60, 82), (34, 64)]), width=2),
                ink(sp([(106, 90), (140, 82), (166, 64)]), width=2),
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
            step(
                "Draw a big rounded back and a round tummy line for the body.",
                ink(sp([(66, 60), (100, 50), (140, 54), (166, 74), (174, 104), (168, 130)])),
                ink(sp([(94, 128), (114, 132), (134, 130)])),
            ),
            step(
                "Draw the head on the left with a long trunk that hangs down and curls at the end.",
                ink(sp([(70, 60), (54, 50), (36, 52), (24, 66), (20, 88), (18, 110), (14, 132), (12, 150),
                        (16, 160, 1), (24, 156), (28, 134), (34, 112), (44, 104), (58, 110)])),
            ),
            step(
                "Add a big floppy ear on the side of the head.",
                ink(sp([(64, 62), (90, 62), (100, 86), (94, 108), (78, 114), (64, 102), (58, 84)], closed=True)),
            ),
            step(
                "Draw thick legs like tree trunks, two in front and two at the back. The far leg peeks out beside the near one. Add toenails.",
                leg_pair(72, 116, w=22, shift=-12, top_far=112),
                leg_pair(134, 130, w=22, shift=12, top_far=126),
                lines([(78, 178, 78, 173), (86, 178, 86, 173), (140, 178, 140, 173), (148, 178, 148, 173)],
                      width=2),
            ),
            step(
                "Finish with an eye, a white tusk under the trunk, and a thin tail.",
                dot(42, 74, 3),
                ink(sp([(34, 106), (40, 118), (54, 122, 1), (46, 110)])),
                ink(sp([(172, 96), (180, 118), (182, 134)]), width=THIN),
                ink(sp([(182, 132), (178, 142, 1), (184, 140), (188, 144, 1), (184, 132)]), width=2.4),
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
            step(
                "Draw a big fluffy mane: a bumpy circle on the left.",
                ink(scallop(50, 74, 36, 36, n=11, puff=0.14)),
            ),
            step(
                "Draw the face inside the mane, with two small round ears on top.",
                ink(sp([(50, 52), (66, 58), (70, 76), (62, 94), (50, 100), (38, 94), (30, 76), (34, 58)],
                       closed=True)),
                ink(sp([(34, 60), (32, 50), (42, 48)]), width=THIN),
                ink(sp([(66, 60), (68, 50), (58, 48)]), width=THIN),
            ),
            step(
                "Draw the long back and the tummy of the body.",
                ink(sp([(84, 62), (112, 72), (150, 72), (166, 86), (167, 112)])),
                ink(sp([(105, 120), (120, 122), (138, 120)])),
            ),
            step(
                "Add strong legs, two in front and two at the back (the far leg peeks out), and a long tail with a fluffy tip.",
                leg_pair(80, 106, w=15, shift=10, top_far=116),
                leg_pair(138, 120, w=15, shift=12, top_far=112),
                ink(sp([(166, 86), (180, 96), (184, 120), (178, 138)]), width=THIN),
                ink(scallop(178, 144, 6, 7, n=5, puff=0.3), width=THIN),
            ),
            step(
                "Finish the face: two eyes, a wide nose, and a mouth.",
                dot(42, 72, 2.8),
                dot(58, 72, 2.8),
                ink(pg([(44, 80), (56, 80), (50, 87)], close=True), width=2, fill=True),
                ink(sp([(50, 87), (50, 91)]), width=2.2),
                ink(sp([(42, 92), (46, 94), (50, 91), (54, 94), (58, 92)]), width=2.2),
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
            step(
                "Draw a body like a teardrop lying down, with the pointy nose on the left.",
                ink(sp([(20, 122, 1), (36, 104), (62, 92), (98, 88), (130, 98), (150, 122), (146, 142),
                        (120, 150), (72, 148), (40, 138)], closed=True)),
            ),
            step(
                "Add a big round ear on the head, with a smaller circle inside.",
                ink(sp([(58, 94), (54, 72), (66, 58), (84, 64), (86, 84), (76, 96)])),
                ink(sp([(62, 90), (60, 74), (68, 66), (80, 70), (80, 84)]), width=2.2),
            ),
            step(
                "Draw small feet under the body.",
                ink(sp([(54, 144), (48, 152), (38, 154, 1), (60, 154), (62, 146)]), width=THIN),
                ink(sp([(116, 150), (108, 158), (98, 160, 1), (124, 160), (128, 148)]), width=THIN),
            ),
            step(
                "Draw a long, thin tail that curves away.",
                ink(sp([(148, 134), (168, 142), (182, 130), (186, 110), (176, 98)])),
            ),
            step(
                "Finish with a shiny eye, a nose, and whiskers.",
                dot(42, 114, 3),
                dot(21, 121, 2.4),
                lines([(26, 124, 6, 116), (26, 126, 6, 128), (28, 128, 10, 138)], width=2),
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
            step(
                "Draw a tall egg-shaped body with two pointy ear tufts on top.",
                ink(sp([(64, 54), (62, 30, 1), (80, 42), (100, 40), (120, 42), (138, 30, 1), (136, 54),
                        (144, 82), (146, 120), (136, 150), (116, 164), (84, 164), (64, 150), (54, 120),
                        (56, 82)], closed=True)),
            ),
            step(
                "Draw a face shape like a wide heart around where the eyes go.",
                ink(sp([(100, 60), (82, 50), (66, 60), (66, 80), (80, 94), (100, 96, 1), (120, 94), (134, 80),
                        (134, 60), (118, 50)], closed=True), width=THIN),
            ),
            step(
                "Add two big round eyes with dark middles, and a small beak pointing down.",
                ink(circ(84, 72, 11), width=THIN),
                ink(circ(116, 72, 11), width=THIN),
                dot(85, 73, 5),
                dot(115, 73, 5),
                ink(sp([(95, 82), (100, 94, 1), (105, 82)], closed=True), width=2.4),
            ),
            step(
                "Draw folded wings on both sides and little V feathers on the chest.",
                ink(sp([(64, 92), (78, 112), (80, 138), (72, 160, 1)])),
                ink(sp([(136, 92), (122, 112), (120, 138), (128, 160, 1)])),
                lines([(92, 112, 96, 116), (96, 116, 100, 112), (104, 112, 108, 116), (108, 116, 112, 112),
                       (90, 128, 94, 132), (94, 132, 98, 128), (102, 128, 106, 132), (106, 132, 110, 128),
                       (96, 144, 100, 148), (100, 148, 104, 144)], width=2),
            ),
            step(
                "Finish with a branch and small curved claws holding on.",
                ink(sp([(26, 168), (100, 168), (178, 164)])),
                ink(sp([(84, 162), (82, 170)]), width=2.4),
                ink(sp([(90, 163), (90, 171)]), width=2.4),
                ink(sp([(110, 163), (110, 171)]), width=2.4),
                ink(sp([(116, 162), (118, 170)]), width=2.4),
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
            step(
                "Draw a tall body like a bowling pin, with a round head on top.",
                ink(sp([(100, 24), (118, 30), (126, 50), (128, 88), (136, 128), (130, 160), (112, 174),
                        (88, 174), (70, 160), (64, 128), (72, 88), (74, 50), (84, 30)], closed=True)),
            ),
            step(
                "Draw the white tummy shape inside, from under the beak to the feet.",
                ink(sp([(86, 50), (80, 80), (78, 120), (84, 156), (100, 168), (116, 156), (122, 120),
                        (118, 80), (110, 54), (98, 48)]), width=THIN),
            ),
            step(
                "Add a flipper on each side, pointing down.",
                ink(sp([(72, 82), (56, 106), (48, 136, 1), (64, 120), (70, 108)])),
                ink(sp([(128, 82), (144, 106), (152, 136, 1), (136, 120), (130, 108)])),
            ),
            step(
                "Draw a pointy beak and an eye.",
                ink(sp([(88, 40), (72, 46, 1), (88, 50)], closed=True), width=THIN),
                dot(95, 38, 3),
            ),
            step(
                "Finish with two flat feet at the bottom.",
                ink(sp([(88, 172), (76, 180, 1), (98, 180, 1), (98, 174)])),
                ink(sp([(104, 174), (104, 180, 1), (124, 180, 1), (112, 172)])),
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
            step(
                "Draw the head from the side, with a short snout on the left and a round ear.",
                ink(sp([(62, 58), (48, 54), (36, 60), (26, 70), (14, 76), (12, 84, 1), (20, 90), (36, 92),
                        (52, 92), (64, 84)])),
                ink(sp([(50, 56), (50, 44), (62, 44), (64, 56)])),
            ),
            step(
                "Draw a big hump on the shoulders, a long back, and a round rump.",
                ink(sp([(62, 58), (84, 48), (116, 56), (146, 62), (164, 80), (168, 100), (164, 114)])),
                ink(sp([(62, 90), (68, 106)])),
                ink(sp([(98, 120), (116, 124), (132, 122)])),
            ),
            step(
                "Add thick legs with big paws: two at the front and two at the back. The far leg peeks out beside the near one.",
                leg_pair(68, 106, w=20, shift=10, top_far=116),
                leg_pair(132, 122, w=20, shift=12, top_far=114),
            ),
            step(
                "Draw little claws on the front paws and a tiny tail.",
                lines([(66, 178, 64, 183), (73, 178, 72, 183), (80, 178, 80, 183)], width=2),
                ink(sp([(168, 88), (176, 92), (171, 100)]), width=THIN),
            ),
            step(
                "Finish with an eye, a big nose, and a mouth.",
                dot(36, 70, 3),
                ink(ell(14, 80, 4, 3.6), width=2, fill=True),
                ink(sp([(20, 90), (28, 88), (34, 90)]), width=THIN),
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
            step(
                "Draw the head from the side: pointy ears and a long, pointy nose.",
                ink(sp([(54, 62), (48, 36, 1), (40, 54), (30, 62), (14, 72), (8, 76, 1), (16, 82), (34, 86),
                        (52, 86), (62, 74), (62, 40, 1), (56, 58)])),
            ),
            step(
                "Draw a slim body: a gently curved back and the tummy.",
                ink(sp([(62, 70), (84, 80), (120, 80), (146, 84), (148, 98), (145, 106)])),
                ink(sp([(52, 86), (62, 100)])),
                ink(sp([(82, 108), (100, 112), (126, 110)])),
            ),
            step(
                "Add slim legs with small paws, two at the front and two at the back.",
                leg_pair(64, 100, w=10, shift=8, top_far=108),
                leg_pair(126, 110, w=11, shift=8, top_far=104),
            ),
            step(
                "Draw a big, bushy tail that sweeps out behind.",
                ink(sp([(144, 84), (166, 74), (186, 84), (194, 106), (188, 128, 1), (170, 116), (148, 102)])),
                ink(sp([(180, 106), (186, 118), (188, 128)]), width=THIN),
            ),
            step(
                "Finish with an eye, a black nose, and the white cheek line.",
                ink(sp([(32, 66), (36, 64), (40, 66)]), width=2.6),
                dot(9, 76, 2.6),
                ink(sp([(16, 82), (30, 78), (44, 82), (52, 86)]), width=2),
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
            step(
                "Draw a long body like a torpedo, with a pointy nose on the left.",
                ink(sp([(14, 100, 1), (36, 86), (80, 76), (130, 84), (166, 98), (172, 102, 1), (150, 110),
                        (110, 120), (70, 124), (40, 118), (22, 108)], closed=True)),
            ),
            step(
                "Add a tall triangle fin on the back. Its back edge curves in.",
                ink(sp([(82, 78), (94, 58), (100, 44, 1), (104, 62), (122, 84)])),
            ),
            step(
                "Draw a tail like a crescent moon: a big top point and a smaller bottom point.",
                ink(sp([(168, 100), (182, 78), (194, 56, 1), (190, 84), (182, 104, 1), (188, 120), (190, 132, 1),
                        (174, 112)])),
            ),
            step(
                "Add a long fin under the front of the body and a small one near the tail.",
                ink(sp([(66, 120), (78, 140), (94, 156, 1), (92, 134), (90, 121)])),
                ink(sp([(130, 114), (138, 126, 1), (144, 112)]), width=THIN),
            ),
            step(
                "Finish with an eye, a mouth, and five gill lines.",
                dot(36, 95, 3),
                ink(sp([(22, 110), (32, 112), (44, 108)]), width=2.4),
                lines([(52, 94, 50, 110), (57, 93, 55, 110), (62, 92, 60, 111), (67, 92, 65, 111),
                       (72, 92, 70, 112)], width=2),
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
            step(
                "Draw a big head with a long jaw, facing left.",
                ink(sp([(56, 44), (40, 38), (22, 42), (10, 52), (10, 66, 1), (26, 70), (42, 74), (56, 70),
                        (62, 56)], closed=True)),
                ink(sp([(12, 62), (28, 64), (48, 66)]), width=THIN),
            ),
            step(
                "Draw the back going down into a long tail with a point, and the tummy underneath.",
                ink(sp([(58, 46), (78, 54), (106, 70), (142, 94), (188, 128, 1), (146, 114), (122, 116)])),
                ink(sp([(54, 70), (60, 96), (76, 116), (96, 124)])),
            ),
            step(
                "Add a huge back leg with a big thigh and a foot with claws.",
                ink(sp([(98, 120), (96, 136), (104, 148), (104, 170), (92, 178, 1), (124, 178, 1), (118, 168),
                        (122, 150), (134, 126), (132, 106)])),
                ink(sp([(84, 124), (86, 148), (82, 170), (74, 176, 1), (96, 176, 1)]), width=THIN),
            ),
            step(
                "Draw two tiny arms on the chest.",
                ink(sp([(62, 88), (74, 96), (78, 106, 1)]), width=THIN),
                ink(sp([(66, 96), (72, 104), (72, 112, 1)]), width=THIN),
            ),
            step(
                "Finish with an eye, a nostril, and some pointy teeth.",
                dot(36, 50, 3),
                dot(14, 50, 1.6),
                lines([(16, 63, 18, 68), (22, 64, 24, 69), (28, 65, 30, 70), (34, 66, 36, 71)], width=2),
            ),
        ],
    )


def snake() -> dict:
    center = [(52, 62), (80, 66), (110, 86), (110, 112), (80, 126), (64, 148), (88, 168), (130, 164), (166, 150),
              (184, 132)]
    return subject(
        "snake",
        "Snake",
        "animals",
        ["snake", "snakes"],
        [
            step(
                "Draw a head shaped like a rounded diamond.",
                ink(sp([(20, 58), (32, 46), (52, 48), (60, 62), (52, 74), (32, 72)], closed=True)),
            ),
            step(
                "Draw a long body that wiggles like an S and gets thinner to a pointy tail.",
                ink(tube(center, 22, 0, closed_start=False, keep=12)),
            ),
            step(
                "Add stripes across the body.",
                [ink(d, width=2.4) for d in tube_bands(center, 22, 0, [0.08, 0.17, 0.26, 0.35, 0.45, 0.55, 0.65, 0.75,
                                                                     0.85])],
            ),
            step(
                "Finish with an eye and a forked tongue.",
                dot(36, 56, 3),
                ink(sp([(20, 60), (11, 62)]), width=2),
                ink(sp([(11, 62), (6, 57)]), width=2),
                ink(sp([(11, 62), (6, 67)]), width=2),
            ),
        ],
    )


def spider() -> dict:
    left = [
        [(90, 76), (72, 46, 1), (58, 18)],
        [(88, 80), (58, 52, 1), (26, 72)],
        [(88, 86), (56, 86, 1), (22, 118)],
        [(90, 92), (66, 114, 1), (46, 168)],
    ]
    return subject(
        "spider",
        "Spider",
        "animals",
        ["spider", "spiders"],
        [
            step("Draw a big oval for the back part of the body.", ink(ell(100, 128, 26, 32))),
            step("Draw a smaller oval on top for the front part.", ink(ell(100, 84, 15, 14))),
            step(
                "Draw four legs on the left. Each leg bends up at the knee, then goes down.",
                [ink(sp(p), width=3.6) for p in left],
            ),
            step(
                "Draw four matching legs on the right side.",
                [ink(sp(mirror(p)), width=3.6) for p in left],
            ),
            step(
                "Finish with tiny eyes, two small fangs, and a pattern on the back.",
                dot(94, 78, 2.4),
                dot(106, 78, 2.4),
                dot(98, 73, 1.6),
                dot(102, 73, 1.6),
                ink(sp([(96, 96), (94, 101, 1)]), width=2.4),
                ink(sp([(104, 96), (106, 101, 1)]), width=2.4),
                ink(sp([(100, 108), (90, 122), (100, 136, 1), (110, 122)], closed=True), width=2.2),
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
            step(
                "Draw a round head, then a round middle, then a big oval tail end.",
                ink(circ(52, 110, 13)),
                ink(circ(82, 106, 18)),
                ink(sp([(98, 98), (120, 86), (152, 90), (172, 106), (180, 118, 1), (162, 130), (130, 138),
                        (104, 126)], closed=True)),
            ),
            step(
                "Draw curved stripes across the tail end and a small stinger.",
                ink(sp([(120, 88), (114, 112), (122, 136)]), width=W),
                ink(sp([(140, 88), (136, 112), (142, 136)]), width=W),
                ink(sp([(160, 96), (156, 114), (160, 130)]), width=W),
                ink(ln(180, 118, 188, 120), width=2.4),
            ),
            step(
                "Add two see-through wings on the back, pointing up.",
                ink(sp([(82, 90), (92, 56), (120, 36), (138, 44), (124, 72), (94, 92)], closed=True), width=THIN),
                ink(sp([(90, 92), (118, 62), (148, 60), (140, 80), (104, 96)], closed=True), width=THIN),
            ),
            step(
                "Draw three thin legs under the middle, bent at the knees.",
                ink(sp([(72, 120), (64, 134, 1), (60, 146)]), width=2.6),
                ink(sp([(82, 124), (80, 138, 1), (74, 150)]), width=2.6),
                ink(sp([(92, 120), (100, 136, 1), (98, 150)]), width=2.6),
            ),
            step(
                "Finish with a big eye and two feelers on the head.",
                ink(ell(48, 106, 4, 6), width=2, fill=True),
                ink(sp([(50, 98), (44, 82), (34, 74)]), width=2.4),
                ink(sp([(56, 98), (56, 82), (50, 70)]), width=2.4),
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
            step("Draw a big fluffy body: a bumpy cloud shape.", ink(scallop(110, 100, 54, 34, n=12, puff=0.08))),
            step(
                "Draw the head on the left, long with a soft nose.",
                ink(sp([(62, 82), (46, 76), (32, 84), (22, 98), (20, 108, 1), (28, 114), (44, 114), (60, 104)])),
            ),
            step(
                "Add an ear that sticks out sideways and fluffy wool on top of the head.",
                ink(sp([(56, 86), (74, 94, 1), (58, 98)])),
                ink(scallop(50, 78, 12, 7, n=5, puff=0.3, a0=180), width=THIN),
            ),
            step(
                "Draw four thin legs with little hooves.",
                leg(72, 128, w=8, hoof=True),
                leg(90, 132, w=8, hoof=True),
                leg(126, 132, w=8, hoof=True),
                leg(144, 128, w=8, hoof=True),
            ),
            step(
                "Finish with an eye, a nose, and a little tail.",
                dot(40, 92, 2.8),
                ink(sp([(22, 106), (26, 109)]), width=2.4),
                ink(scallop(166, 92, 6, 7, n=4, puff=0.3), width=THIN),
            ),
        ],
    )


def crab() -> dict:
    claw = [(46, 70), (34, 52), (36, 34), (52, 28, 1), (46, 42), (54, 48, 1), (60, 38), (60, 56), (52, 70)]
    legs_left = [
        [(54, 110), (30, 104, 1), (16, 124)],
        [(56, 118), (34, 126, 1), (24, 148)],
        [(64, 126), (48, 144, 1), (42, 166)],
    ]
    return subject(
        "crab",
        "Crab",
        "animals",
        ["crab", "crabs"],
        [
            step(
                "Draw a wide shell, a little pointy at each side.",
                ink(sp([(100, 84), (132, 86), (154, 98, 1), (150, 118), (128, 132), (100, 134), (72, 132), (50, 118),
                        (46, 98, 1), (68, 86)], closed=True)),
            ),
            step(
                "Draw two arms with big pincer claws on top.",
                ink(sp([(58, 96), (50, 80), (50, 70)])),
                ink(sp(claw, closed=True)),
                ink(sp(mirror([(58, 96), (50, 80), (50, 70)]))),
                ink(sp(mirror(claw), closed=True)),
            ),
            step(
                "Add three bent legs on each side.",
                [ink(sp(p), width=3.6) for p in legs_left],
                [ink(sp(mirror(p)), width=3.6) for p in legs_left],
            ),
            step(
                "Draw two eyes on short stalks.",
                lines([(90, 86, 88, 70), (110, 86, 112, 70)], width=3),
                ink(circ(88, 66, 4.5), width=2.4),
                ink(circ(112, 66, 4.5), width=2.4),
                dot(88, 66, 2),
                dot(112, 66, 2),
            ),
            step(
                "Finish with a small mouth and a few bumps on the shell.",
                ink(sp([(92, 100), (100, 104), (108, 100)]), width=2.4),
                ink(sp([(76, 112), (100, 120), (124, 112)]), width=2),
            ),
        ],
    )


def octopus() -> dict:
    arms = [
        [(78, 90), (54, 98), (32, 112), (18, 134), (22, 152), (36, 150)],
        [(84, 94), (66, 118), (52, 140), (48, 162), (58, 174), (68, 166)],
        [(94, 96), (88, 124), (84, 150), (88, 172), (100, 178)],
    ]
    return subject(
        "octopus",
        "Octopus",
        "animals",
        ["octopus", "octopuses", "octopi"],
        [
            step(
                "Draw a big round head, a little taller than it is wide.",
                ink(sp([(100, 18), (126, 26), (140, 54), (132, 80), (118, 94), (82, 94), (68, 80), (60, 54),
                        (74, 26)], closed=True)),
            ),
            step(
                "Add two eyes low on the head.",
                ink(ell(84, 78, 7, 6), width=THIN),
                ink(ell(116, 78, 7, 6), width=THIN),
                ink(ln(80, 78, 88, 78), width=2.6),
                ink(ln(112, 78, 120, 78), width=2.6),
            ),
            step(
                "Draw three wavy arms on the left. They get thinner and curl at the ends.",
                [ink(tube(a, 13, 2, closed_start=False, keep=9), width=THIN) for a in arms],
            ),
            step(
                "Draw three matching arms on the right.",
                [ink(tube(mirror(a), 13, 2, closed_start=False, keep=9), width=THIN) for a in arms],
            ),
            step(
                "Finish with little round suckers under the arms.",
                [ink(circ(x, y, 2.2), width=1.8) for x, y in [(44, 112), (30, 128), (64, 126), (56, 146),
                                                                 (156, 112), (170, 128), (136, 126), (144, 146)]],
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
            step(
                "Draw a small head with a long nose, two little horns with knobs, and an ear.",
                ink(sp([(52, 30), (38, 26), (24, 30), (14, 40), (14, 48), (24, 52), (40, 52), (54, 44)], closed=True)),
                lines([(42, 27, 40, 14), (50, 29, 50, 16)], width=3),
                dot(40, 13, 2.8),
                dot(50, 15, 2.8),
                ink(sp([(54, 34), (66, 30, 1), (58, 42)])),
            ),
            step(
                "Draw a very long neck going down and to the right.",
                ink(sp([(40, 52), (54, 82), (72, 110)])),
                ink(sp([(56, 40), (74, 70), (98, 98)])),
                ink(sp([(58, 40), (64, 52), (72, 64), (80, 76), (90, 88)]), width=2),
            ),
            step(
                "Draw a short body that slopes down to the back.",
                ink(sp([(98, 98), (130, 104), (152, 112), (160, 128), (152, 140)])),
                ink(sp([(72, 110), (78, 134), (100, 140), (132, 140)])),
            ),
            step(
                "Add four very long, thin legs and a tail with a tuft.",
                leg(78, 132, w=8, bottom=188, hoof=True),
                leg(96, 138, w=8, bottom=188, hoof=True),
                leg(128, 138, w=8, bottom=188, hoof=True),
                leg(144, 134, w=8, bottom=188, hoof=True),
                ink(sp([(158, 116), (168, 134), (170, 152)]), width=2.4),
                ink(sp([(170, 150), (166, 160, 1), (174, 156)]), width=2.4),
            ),
            step(
                "Finish with an eye and patches all over the neck and body.",
                dot(36, 36, 2.8),
                [ink(sp(p, closed=True), width=2.2) for p in [
                    [(56, 58), (64, 56), (64, 66), (56, 66)],
                    [(62, 76), (72, 72), (74, 84), (66, 86)],
                    [(74, 94), (84, 92), (86, 102), (78, 106)],
                    [(92, 112), (104, 108), (108, 120), (96, 124)],
                    [(114, 112), (128, 112), (128, 126), (116, 128)],
                    [(136, 116), (148, 118), (146, 130), (136, 130)],
                    [(84, 122), (90, 120), (92, 132), (84, 134)],
                ]],
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
            step(
                "Draw a round head with a round ear on each side.",
                ink(sp([(100, 26), (122, 32), (128, 52), (122, 72), (100, 80), (78, 72), (72, 52), (78, 32)],
                       closed=True)),
                ink(sp([(74, 46), (62, 44), (58, 56), (64, 64), (74, 62)])),
                ink(sp([(126, 46), (138, 44), (142, 56), (136, 64), (126, 62)])),
            ),
            step(
                "Draw the face shape inside: two bumps on top for the eyes and a round muzzle.",
                ink(sp([(100, 42), (90, 34), (80, 40), (80, 54), (84, 64), (90, 74), (100, 76), (110, 74), (116, 64),
                        (120, 54), (120, 40), (110, 34)], closed=True), width=THIN),
            ),
            step(
                "Draw a pear-shaped body that is sitting down.",
                ink(sp([(88, 78), (76, 102), (74, 132), (86, 150), (114, 150), (126, 132), (124, 102), (112, 78)])),
            ),
            step(
                "Add long arms resting on the knees, and bent legs with feet.",
                ink(sp([(80, 92), (64, 112), (62, 136), (70, 148)])),
                ink(sp([(120, 92), (136, 112), (138, 136), (130, 148)])),
                ink(sp([(84, 140), (62, 146), (56, 166), (72, 172), (92, 164)])),
                ink(sp([(116, 140), (138, 146), (144, 166), (128, 172), (108, 164)])),
            ),
            step(
                "Finish with eyes, a nose, a big smile, and a long curly tail.",
                dot(92, 50, 3),
                dot(108, 50, 3),
                dot(97, 60, 1.6),
                dot(103, 60, 1.6),
                ink(sp([(90, 66), (100, 70), (110, 66)]), width=2.4),
                ink(sp([(124, 146), (152, 156), (172, 140), (170, 112), (154, 108), (152, 124)])),
            ),
        ],
    )
