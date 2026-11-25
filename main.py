#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes one line -- the error message a kitchen toaster shows its owner --
to /output/entry.txt.

Standard library only: no Pillow, no numpy, no external font or data file,
so it runs the same in the grader sandbox as it does here.

Never deletes the /output folder itself: it only clears the folder's
contents, then writes entry.txt.
"""

import os

LINE = "Error: Crumb tray full. I am now 63% crumbs. Please help me."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
