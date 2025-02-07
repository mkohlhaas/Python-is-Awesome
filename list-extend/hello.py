#!/usr/bin/env python

inventory = [
    "Crimson Sword",
    "Great Helm",
    "Leather Boots",
]

chest = [
    "Health Potion",
    "Mana Potion",
    "Map of Riches",
]

if __name__ == "__main__":
    print(inventory)
    print(chest)
    print(inventory + chest)
    inventory += chest
    print(inventory)
    inventory.extend(chest)
    print(inventory)
