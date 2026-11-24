#!/usr/bin/env python3
"""Funniest Autocorrect Fail — entry program.

Writes exactly one line (the autocorrect fail) to /output/entry.txt
and nothing else.
"""

import os

TEXT = (
    "I texted my landlord 'the rent is in the mail' "
    "and autocorrect sent 'the rat is in the mail.' "
    "He's here now."
)


def normalize(text: str) -> str:
    """Collapse accidental repeated spaces and strip surrounding whitespace.

    The entry text is authored as a single clean line; this keeps the
    output byte-exact even if the source literal ever drifts.
    """
    return " ".join(text.split())


def main() -> None:
    text = normalize(TEXT)

    # Guard: the entry must be a single line under 200 characters.
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
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("output mismatch: entry.txt does not equal the entry text")


if __name__ == "__main__":
    main()
