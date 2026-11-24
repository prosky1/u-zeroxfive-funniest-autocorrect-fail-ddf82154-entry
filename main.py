#!/usr/bin/env python3
"""Funniest Autocorrect Fail — entry program.

Writes exactly one line (the autocorrect fail) to /output/entry.txt
and nothing else. The entry text is 74 characters and contains an
em-dash (U+2014), so the file is written and read back as UTF-8 to
keep the output byte-identical.
"""

import os

TEXT = "Please welcome our new intestine, Dave — his desk is next to the bathroom."


def main() -> None:
    text = TEXT

    # Guard: the entry must be a single line under 200 characters.
    if len(text) != 74:
        raise SystemExit(f"entry length changed: expected 74 characters, got {len(text)}")
    if len(text) >= 200:
        raise SystemExit(f"entry too long: {len(text)} characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text != text.strip():
        raise SystemExit("entry has leading or trailing whitespace")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

    # Verify the file holds exactly the intended text, nothing else.
    with open("/output/entry.txt", "rb") as f:
        written_bytes = f.read()
    if written_bytes != text.encode("utf-8"):
        raise SystemExit("output mismatch: entry.txt bytes do not equal the entry text")


if __name__ == "__main__":
    main()
