#!/usr/bin/env python3
"""Write the one Wi-Fi network name to /output/entry.txt.

The name: "I Changed The Locks, Dave" -- 25 characters. A stranger reading
it in a phone's network list gets the whole story at once: a breakup, a
Dave who is now locked out, and a narrator who changed the locks and kept
the Wi-Fi. The joke lands on the first read, the name itself is the
message to the ex, and it is not one of the stock Wi-Fi jokes.

Deterministic, no network, no input: the entry is a single fixed name.
"""

import os
from pathlib import Path

NAME = "I Changed The Locks, Dave"

MAX_CHARS = 32


def validate(name: str) -> None:
    """Fail loudly unless the name satisfies the competition gate."""
    assert isinstance(name, str)
    assert name.strip(), "entry must not be only white space"
    assert "\n" not in name and "\r" not in name, "entry must be one line"
    assert 1 <= len(name) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(name)}"
    )
    assert name.encode("utf-8").decode("utf-8") == name, "entry must be UTF-8"


def main() -> None:
    validate(NAME)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    # No trailing newline: the gate counts the file's characters, so the
    # file holds exactly the name, nothing else.
    target.write_text(NAME, encoding="utf-8")
    assert target.read_text(encoding="utf-8") == NAME, (
        "entry.txt does not hold exactly the chosen name"
    )


if __name__ == "__main__":
    main()
