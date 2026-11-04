# Drawing book format

Draw With Me does not invent pictures. Every subject is a small list of steps in `Sources/DrawingCore/Resources/drawings.json`. The Mac app and the tests read that file. Nothing is downloaded.

To add a subject, edit the Python helpers in `tools/` (they keep the shapes consistent) and run:

```bash
python3 tools/generate_drawings.py
python3 tools/render_previews.py
```

The pictures are meant to look like real pen-and-ink sketches, not stacks of circles and boxes. `tools/shapes.py` has helpers for that:

- `sp(points)` draws a smooth curve through a list of points. Add a third value, as in `(x, y, 1)`, for a sharp corner.
- `tube(center, w0, w1)` turns a center line into a tapering outline, for tails, trunks, necks, and arms.
- `scallop(...)` draws a bumpy, fluffy edge for clouds, sheep wool, and tree leaves.
- `mirror(points)` flips points across the middle of the page.

Keep each subject to about 5 to 10 steps a child can copy, and make each step's words describe exactly the lines it adds. To look at a few subjects while you work:

```bash
python3 tools/review.py --out=review.png whale cat
python3 tools/review.py --out=steps.png --steps whale
```

You can also edit the JSON by hand. Keep it valid. The next app build copies the file into the app.

## File shape

```json
{
  "formatVersion": 1,
  "subjects": [ ]
}
```

Each subject:

| Field | Meaning |
|---|---|
| `id` | Stable short name, like `cat` or `ice-cream`. Used for progress. |
| `title` | What we show on screen, like `Ice Cream`. |
| `category` | One of `animals`, `fantasy`, `vehicles`, `food`, `nature`, `space`, `buildings`, `everyday`. |
| `words` | Extra ways to ask for it: plurals, nicknames, and common misspellings. `kitty` belongs on the cat. The matcher also tries simple plurals and small typos, so you do not have to list every spelling. |
| `viewBox` | `[minX, minY, width, height]`. Use `[0, 0, 200, 200]`. |
| `steps` | Ordered steps. At least 3. Each step stays on the page; later steps do not erase earlier ones. |

Each step:

| Field | Meaning |
|---|---|
| `instruction` | One or two plain sentences a child can follow. Name the shape: circle, oval, triangle, line, curve. |
| `strokes` | The new lines for this step. |

Each stroke:

| Field | Meaning |
|---|---|
| `d` | An SVG path. See below. |
| `width` | Pen thickness in viewBox units. `4.6` is the normal outline. `3.1` is a thin detail. Optional; the default is `4.6`. |
| `fill` | `true` for a solid dot (eyes, noses). Optional; the default is `false`. |

The app draws older steps in grey and the current step in blue. You do not put colors in the file.

## Paths

`d` uses SVG path commands. The parser accepts `M L H V C S Q T A Z` in upper or lower case. Lower case is relative. Arcs (`A`) and quadratic curves (`Q`, `T`) are turned into cubics. Y grows downward, the same as SVG.

The pictures in this book are written with only `M`, `L`, `C`, and `Z`, so they stay easy to check. A circle is four cubics. Numbers can be separated by spaces or commas.

Example step (a head):

```json
{
  "instruction": "Draw a big circle for the head.",
  "strokes": [
    {
      "d": "M 100 44 C 119 44 134 59 134 78 C 134 97 119 112 100 112 C 81 112 66 97 66 78 C 66 59 81 44 100 44 Z",
      "width": 4.6,
      "fill": false
    }
  ]
}
```

Keep the ink inside the page, roughly 8 to 192 on both axes, so thumbs and the big paper view are not clipped.

## Words to refuse

Rude or unsafe words are not in the JSON. They live in the matcher and get the same gentle "Let's try another one!" as a word we do not know. Do not add those words as nicknames for a real subject.

## Checks

`./build.sh test` loads the whole book. It fails if a path cannot be read, two subjects claim the same word, a category is unknown, a step has no lines, or a drawing wanders off the page.
