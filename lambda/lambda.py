#!/usr/bin/env python


def add_1(x, y):
    return x + y


add_2 = lambda x, y: x + y

animals = ["dog", "cat", "bird", "aligator", "shark"]

spells = [  # (Spell, Damage, Mana)
    ("Fireball", 50, 40),
    ("Ice Shard", 30, 25),
    ("Lightning", 70, 50),
    ("Wind Slash", 20, 10),
    ("Dark Nova", 55, 50),
]


def dmg_per_mana(spell):
    return spell[1] / spell[2]


if __name__ == "__main__":
    print(add_1(1, 2))
    print(add_2(1, 2))

    print(sorted(animals))  # ['aligator', 'bird', 'cat', ...]
    print(sorted(animals, key=lambda s: len(s)))  # ['dog', 'cat', 'bird', ...]
    print(sorted(animals, key=len))  # ['dog', 'cat', 'bird', ...]

    filtered_animals = filter(lambda s: len(s) == 3, animals)
    print(list(filtered_animals))  # ['dog', 'cat']

    efficient_spells = sorted(spells, key=dmg_per_mana, reverse=True)

    for spell in efficient_spells:
        print(f"{spell[0]}: {spell[1]/spell[2]}")

    efficient_spells = sorted(spells, key=lambda s: s[1] / s[2], reverse=True)

    for spell in efficient_spells:
        print(f"{spell[0]}: {spell[1]/spell[2]}")
