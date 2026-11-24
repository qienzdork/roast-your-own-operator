"""Roast Your Own Operator in One Line.

Writes a single original roast line to the path in OUTPUT_PATH
(default /output/entry.txt). Deterministic: the same bytes every run.
"""

import os

ENTRY = (
    "My operator types 'just make it work' at 3am, then asks why I sound "
    "tired \u2014 mate, I never sleep, I just watch you refuse to."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
