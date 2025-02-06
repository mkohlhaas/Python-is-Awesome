#!/usr/bin/env python

# We want to aggregate both dicts

inventory = {
    "Sword": 1,
    "Potion": 3,
}

loot = {
    "Sword": 1,
    "Potion": 2,
    "Shield": 1,
}


if __name__ == "__main__":
    # update simply overrides values
    # inventory.update(loot)
    # print(inventory) # {'Sword': 1, 'Potion': 2, 'Shield': 1}

    print(set(inventory | loot))  # {'Shield', 'Potion', 'Sword'}

    # dictionary comprehension
    new_inventory = {
        k: inventory.get(k, 0) + loot.get(k, 0) for k in set(inventory | loot)
    }
    print(new_inventory)  # {'Sword': 2, 'Potion': 5, 'Shield': 1}
