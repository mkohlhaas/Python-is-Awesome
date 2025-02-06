#!/usr/bin/env python

inventory = [
    "Sword",
    "Shield",
    "Potion of Invisibility",
    "Map",
]


if __name__ == "__main__":
    print(list(enumerate(inventory)))

    for index, item in enumerate(inventory):
        # print(index, item)
        print(f"{index}: {item}")
