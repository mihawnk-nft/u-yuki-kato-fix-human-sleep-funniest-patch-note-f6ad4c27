#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — make.fun entry (program/v1, pure stdlib).

Writes a single funny patch-note line about human sleep being fixed to
/output/entry.txt. One line, under the 160-character cap.
"""

import os

LINE = (
    "Fixed a bug where sleep crashed at 3 AM because the brain insisted "
    "on replaying every embarrassing thing you have ever said."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def verify(line: str) -> str:
    """Gate check: 1-160 characters of UTF-8 text, not only white space."""
    line = line.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if len(line) > 160:
        raise SystemExit(f"entry line is {len(line)} characters, over the 160 limit")
    return line


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-160 characters,
    # not only white space. The line below is 124 characters.
    line = verify(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
