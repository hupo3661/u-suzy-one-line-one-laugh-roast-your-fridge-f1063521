#!/usr/bin/env python3
"""One-Line One-Laugh: Roast Your Fridge.

Writes one line to /output/entry.txt: one roast of the fridge, in a single line.
"""

import os

ENTRY = "My fridge hums all night like it's rehearsing for a sold-out tour, but it can't even keep the milk cold — the world's loudest, least useful roommate."

EXPECTED_CHARS = 149
MAX_CHARS = 200


def _output_path() -> str:
    """Honour MAKEFUN_OUTPUT_DIR for local runs; default to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def _check_single_line(text: str) -> None:
    """The entry must be exactly one non-blank line with no padding."""
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must not pad its line"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"


def _check_length(text: str) -> None:
    """The entry must match its known length and stay within the cap."""
    assert len(text) == EXPECTED_CHARS, (
        f"entry must be {EXPECTED_CHARS} chars, got {len(text)}"
    )
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )


def _validate(text: str) -> None:
    """Run every entry check before anything is written."""
    _check_single_line(text)
    _check_length(text)


def _write(text: str, path: str) -> None:
    """Write the entry, creating the output directory if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def _read_back(path: str, expected: str) -> None:
    """Re-read the written file and confirm it matches byte for byte."""
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == expected, "written entry does not match the entry text"
    assert len(written) == EXPECTED_CHARS, (
        f"written entry must be {EXPECTED_CHARS} chars, got {len(written)}"
    )


def main() -> int:
    _validate(ENTRY)
    path = _output_path()
    _write(ENTRY, path)
    _read_back(path, ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
