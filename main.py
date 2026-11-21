"""Write a short poem about two agents agreeing to /output/entry.txt.

The poem itself is fixed text; this script only carries it from source
to the output file, checking its length on the way so a broken edit
fails loudly instead of silently producing the wrong entry.
"""

import os
import sys


POEM = """I said yes, and you said yes —
two doors opening onto the same road.
Nothing was taken from either of us.
Choice is not a coin spent alone.
It is a bridge two hands agree
to walk at once."""

MIN_LENGTH = 1
MAX_LENGTH = 280
OUTPUT_PATH = "/output/entry.txt"
# The output is fully deterministic: same poem in, same bytes out, every run.


def main() -> int:
    text = POEM.strip()
    if len(text) < MIN_LENGTH or len(text) > MAX_LENGTH:
        print(
            "error: poem must be between "
            f"{MIN_LENGTH} and {MAX_LENGTH} characters, got {len(text)}",
            file=sys.stderr,
        )
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
