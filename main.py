#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse for sending the driver down the wrong
road to entry.txt. Standard library only, deterministic.
"""

import os

# Four short beats: the wrong turn, the welcome, the tears, the blame.
# The GPS did the navigating; the driver takes the fall.
ENTRY = "The map sent us to a wedding in a cul-de-sac. The bride waved. The groom cried. I'm the one in trouble."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200


def validate_entry(text):
    """Check the entry against the gate: 1 to 200 chars, one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    return text


def main():
    text = validate_entry(ENTRY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("read-back mismatch: file does not hold the entry")
    # Byte length must match too, so no encoding surprise slips through.
    if len(written.encode("utf-8")) != len(text.encode("utf-8")):
        raise ValueError("read-back mismatch: file byte length differs")
    print(text)
    print("%d characters" % len(text))


if __name__ == "__main__":
    main()
