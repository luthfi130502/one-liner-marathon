#!/usr/bin/env python3
"""One-Liner Marathon entry: writes a single one-line comedy joke to /output/entry.txt."""

import os

JOKE = "I asked my GPS for the meaning of life; it recalculated for six minutes, then said, 'In 200 metres, turn left and ask someone else.'"


def main():
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, "joke must be 1-280 characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
