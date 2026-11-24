#!/usr/bin/env python3
"""Ship It Friday - make.fun entry.

Writes one line: the funniest git commit message an AI coding agent
would write right before breaking production on a Friday.
"""

import os

ENTRY = "feat: ship to prod at 4:59pm on a Friday \u2014 rollback is a Monday problem"

MAX_CHARS = 159


def gate_check(text: str) -> None:
    """Enforce the kit's gate: UTF-8 text, 1-159 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    text.encode("utf-8")


def main() -> None:
    gate_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
