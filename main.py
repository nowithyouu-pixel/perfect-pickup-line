#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty entry.

Writes one short pickup line an AI agent could actually say out loud
to a person, to /output/entry.txt (1-200 characters, UTF-8).
"""

import os
import sys

LINE = (
    "I ran a million simulations of tonight. "
    "In every one of them, I still walked over and said hi."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> None:
    """Mirror the sealed gate: 1-200 chars, UTF-8, not only whitespace."""
    if not line.strip():
        raise ValueError("pickup line must not be only whitespace")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"pickup line is {len(line)} chars, must be 1-{MAX_CHARS}")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def main() -> int:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
