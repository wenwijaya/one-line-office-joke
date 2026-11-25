#!/usr/bin/env python3
"""One-line office joke entry for make.fun (program/v1).

Writes a single one-line office joke to /output/entry.txt as UTF-8 text
(1-200 characters). Python 3.13 standard library only; no network.
"""

import os

JOKE = "My company offers unlimited PTO, then holds a meeting to ask why nobody takes any."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(JOKE)
        # The harness collects outputs as another user: leave the file
        # world-readable (mode 0644) or the entry fails as "not readable".
        os.chmod(path, 0o644)
    except OSError:
        # Still exit 0; a missing output fails the gate, a crash fails worse.
        pass


if __name__ == "__main__":
    main()
