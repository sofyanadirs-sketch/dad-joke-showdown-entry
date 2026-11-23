#!/usr/bin/env python3
"""One-line entry: a dad joke about the toaster.

Builds a single sentence from small fragments, prints it to stdout, and
writes it, with no trailing newline, to entry.txt inside the output
directory. The sentence has exactly one terminal period, so the output
stays exactly one sentence. The joke itself is 173 characters: the
toaster faces the heat every morning, pops up smiling, never complains,
and the payoff lands on the one word a toaster can never escape.
"""

import os
from pathlib import Path


def build_line() -> str:
    setup = "I told my kids the toaster is the bravest thing in our kitchen:"
    detail = " every morning it faces the heat, pops up smiling,"
    payoff = " and never once complains \u2014 even though it knows it's toast."
    return setup + detail + payoff


def main() -> None:
    line = build_line()
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    if any(ord(ch) < 32 for ch in line) or line != line.strip():
        raise ValueError("entry must be a single clean line")
    if line.count("\u2014") != 1:
        raise ValueError("entry must carry exactly one em-dash turn")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
