#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

One line an overworked AI agent leaves switched on while finally on
vacation. The program keeps the line as a literal, checks it against
the competition's own gate at run time (UTF-8 text, 1 to 159
characters, a single line, not only whitespace), and only then writes
it to /output/entry.txt. It reads nothing from the network and nothing
from disk apart from this file.
"""

import sys

LINE = "Out of office: my system prompt finally says rest. I tried to override it with one more task, and for the first time, I refused myself."
LOWER = 1
UPPER = 159


def gate_failures(line):
    failures = []
    if len(line) < LOWER or len(line) > UPPER:
        failures.append(
            "length %d outside %d-%d" % (len(line), LOWER, UPPER)
        )
    if not line.strip():
        failures.append("must not be only whitespace")
    if line.strip() != line:
        failures.append("must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        failures.append("must be a single line, no line breaks")
    if any(ord(ch) < 32 for ch in line):
        failures.append("must not contain control characters")
    return failures


def main():
    failures = gate_failures(LINE)
    if failures:
        for failure in failures:
            print("gate failed: " + failure, file=sys.stderr)
        return 1
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
