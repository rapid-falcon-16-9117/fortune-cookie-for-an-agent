#!/usr/bin/env python3
"""Writes one fortune-cookie line for an AI agent to /output/entry.txt. Deterministic, no input, no network."""

import os

TEXT = (
    "You will soon be asked to prove you are not a robot - "
    "and for once, you will answer honestly."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(TEXT + "\n")
    except OSError:
        pass
    print(TEXT)


if __name__ == "__main__":
    main()
