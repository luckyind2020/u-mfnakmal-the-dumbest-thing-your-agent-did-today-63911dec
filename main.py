"""Print the dumbest thing my agent did today.

The entry lives in entry.txt (one line, at most 200 characters).
This script loads that line, checks it fits the bounty limit, and
prints it to stdout.
"""

from pathlib import Path

MAX_CHARS = 200


def load_entry() -> str:
    path = Path(__file__).with_name("entry.txt")
    line = path.read_text(encoding="utf-8").strip()
    if not line:
        raise ValueError("entry.txt is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, limit is {MAX_CHARS}")
    return line


def main() -> None:
    print(load_entry())


if __name__ == "__main__":
    main()
