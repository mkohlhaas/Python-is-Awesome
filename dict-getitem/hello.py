#!/usr/bin/env python

inventory = [
    "Axe",
    "Great Sword",
    "Stick",
]

# acts as a look-up table
rarity = {
    "Great Sword": 98,
    "Golden Bow": 97,
    "Iron Sword": 80,
    "Axe": 34,
    "Stick": 1,
}

if __name__ == "__main__":
    inv_sorted = sorted(
        inventory,
        key=rarity.__getitem__,
        reverse=True,
    )
    print(inv_sorted)
