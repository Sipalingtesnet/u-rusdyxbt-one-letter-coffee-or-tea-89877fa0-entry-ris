#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

Writes the entry: exactly one letter, A for coffee or B for tea, and nothing
else -- no word, no gloss, no punctuation, no trailing newline.

Stance: A. Coffee in one character is an appetite owned out loud, not a taste
described; that is the shorter, funnier, more honest answer, so it wins over
tea's composed calm.
"""

from pathlib import Path

LETTER = "A"  # A = coffee, B = tea
OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # Byte-exact by construction: the encoded letter, nothing appended.
    OUT_FILE.write_bytes(LETTER.encode("utf-8"))


if __name__ == "__main__":
    main()
