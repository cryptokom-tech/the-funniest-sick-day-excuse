#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun bounty entry.

Writes one line (1-200 characters) to /output/entry.txt: the funniest
sick-day excuse that can be landed in one breath. Stdlib only, no
network, deterministic: the same bytes on every run. The written file
is read back and verified before the program reports success.
"""

import os
import sys

LINE = (
    "Sorry, can't come in \u2014 my washing machine flooded the flat "
    "and I'm currently bailing out the kitchen with a cereal bowl."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    if not LINE or len(LINE) > 200:
        print("entry line must be 1-200 characters", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE or LINE != LINE.strip():
        print("entry line must be a single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("verification failed: written file differs", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
