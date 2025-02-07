#!/usr/bin/env python

inventory = ["Gem", "Sword", "Shield", "Health Potion"]


if __name__ == "__main__":
    print(inventory)

    # Putting 'Gem' to the end of the list
    idx = inventory.index("Gem")
    item = inventory.pop(idx)
    inventory.append(item)
    print(inventory)

    # Putting 'Shield' at the beginning of the list
    idx = inventory.index("Shield")
    item = inventory.pop(idx)
    inventory.insert(0, item)
    print(inventory)
