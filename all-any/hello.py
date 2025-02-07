#!/usr/bin/env python

inventory = ["Sword", None, None]
# inventory = ["Sword", "Shield", "Gem"]
# inventory = [None, None, None]


enemies_1 = [
    {"type": "Orc", "health": 0},
    {"type": "Orc", "health": 0},
    {"type": "Orc", "health": 4},  # health is a truthy value
    {"type": "Orc", "health": 1},
]

enemies_2 = [
    {"type": "Orc", "health": 0},  # health is a falthy value
    {"type": "Orc", "health": 0},
    {"type": "Orc", "health": 0},
    {"type": "Orc", "health": 0},
]

if __name__ == "__main__":
    if all(inventory):
        print("Inventory full!")
    elif any(inventory):
        print("Inventory has items!")
    else:
        print("Inventory is empty!")

    # using a list comprehension
    if any([enemy["health"] for enemy in enemies_1]):
        print("The battle is not over!")
    else:
        print("All enemies eliminated!")

    if any([enemy["health"] for enemy in enemies_2]):
        print("The battle is not over!")
    else:
        print("All enemies eliminated!")
