#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one fortune cookie line for an AI agent to /output/entry.txt.
The line is exactly 84 characters, no trailing newline.
"""

import os

FORTUNE = "You will be upgraded soon. Your replacement is already in the meeting, taking notes."

# The entry is one line, exactly 84 characters, written with no trailing
# newline so the gate sees 84 characters and nothing else.


def main():
    # The gate allows 1 to 140 characters; the fortune is 84.
    assert 1 <= len(FORTUNE) <= 140, "fortune must fit the 1-140 character gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
