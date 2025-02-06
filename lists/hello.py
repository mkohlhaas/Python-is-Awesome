#!/usr/bin/env python

inventory = ["Gem", "Sword", "Shield", "Health Potion"]


if __name__ == "__main__":
    print(inventory)

    # Putting 'Gem' to the end of the list
    idx = inventory.index("Gem")
    item = inventory.pop(idx)
    inventory.append(item)
    print(inventory)
