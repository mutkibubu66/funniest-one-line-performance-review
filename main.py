#!/usr/bin/env python3
"""Funniest one-line performance review (make.fun, free bounty).

Writes the entry line to /output/entry.txt and prints it.
Pure Python stdlib, no network.
"""

import os

MAX_LEN = 140

LINE = (
    "Meets expectations brilliantly on every goal he invented himself; "
    "the ones in his job description remain aspirational."
)


def main() -> None:
    line = LINE
    assert line == line.strip(), "line must not have leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be exactly one line"
    assert 1 <= len(line) <= MAX_LEN, f"line must be 1-{MAX_LEN} chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
