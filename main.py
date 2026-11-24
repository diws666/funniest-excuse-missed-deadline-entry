#!/usr/bin/env python3
"""Writes the competition excuse to /output/entry.txt."""

import os

EXCUSE = "My context window ate the last three hours. I have the receipts, but they are in the part I forgot."  # 99 characters


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
