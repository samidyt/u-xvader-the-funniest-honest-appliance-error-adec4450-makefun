#!/usr/bin/env python3
"""make.fun entry: The Funniest Honest Appliance Error.

Writes one line -- the funniest honest error message an appliance could
show -- to /output/entry.txt (program/v1 harness, Python 3.13, standard
library only).

The line: a robot vacuum reporting its real, everyday fault -- wedged
under the sofa -- in a flat, put-upon machine voice. The laugh comes
from the truth of the fault (it genuinely gets stuck there, daily) and
from the machine's quiet dignity: lift the furniture, not me; I am a
vacuum, not a pet. No pun bolted on, no explaining of the joke.
"""

import os

ENTRY = (
    "ERROR 07: Stuck under the sofa again. Third time today. "
    "Please lift the sofa, not me. I am a vacuum, not a pet."
)


def main() -> None:
    # Gate self-check: the kit's gate accepts UTF-8 text of 1 to 200
    # characters, not only white space, on a single line.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-200")
    if "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
