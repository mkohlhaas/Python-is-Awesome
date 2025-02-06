#!/usr/bin/env python

inventory = ["Sword", None, None]
# inventory = ["Sword", "Shield", "Gem"]
# inventory = [None, None, None]


if __name__ == "__main__":
    if all(inventory):
        print("Inventory full!")
    elif any(inventory):
        print("Inventory has items!")
    else:
        print("Inventory is empty!")
