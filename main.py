#!/usr/bin/env python3
"""One-Line One-Laugh: Roast Your Fridge.

Writes one line to /output/entry.txt: one roast of the fridge, in a single line.
"""

import os

ENTRY = "My fridge hums all night like it's rehearsing for a concert nobody bought tickets to, yet somehow still can't keep the milk cold."

MAX_CHARS = 200


def _output_path() -> str:
    """Honour MAKEFUN_OUTPUT_DIR for local runs; default to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "entry must not pad its line"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}"
    path = _output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
