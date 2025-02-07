#!/usr/bin/env python


items = [
    "Mystic Sword",
    "Wooden Shield",
    "Rock",
]

rarity = [
    99,
    56,
    5,
]

weight = [
    1.30,
    1.10,
    0.01,
]

if __name__ == "__main__":
    # Zipping
    inventory = zip(items, rarity, weight)

    # Unzipping with the unpacking operator
    i, r, w = zip(*inventory)
    print(i, r, w, sep="\n")
