#!/usr/bin/env python

# Task: Remove file extensions!

import os
import pathlib


full_files = [
    "info.txt",
    "image.png",
    "script.c",
    "image2.jpg",
    "info.3.txt",
]

if __name__ == "__main__":
    # string manipulation
    for file in full_files:
        print(".".join(file.split(".")[:-1]))

    # os
    print()
    for file in full_files:
        print(os.path.splitext(file)[0])

    # pathlib
    print()
    for file in full_files:
        print(pathlib.Path(file).stem)
