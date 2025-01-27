#!/usr/bin/env python


def add_1(x, y):
    return x + y


add_2 = lambda x, y: x + y

animals = ["dog", "cat", "bird", "aligator", "shark"]

if __name__ == "__main__":
    print(add_1(1, 2))
    print(add_2(1, 2))

    print(sorted(animals))  # ['aligator', 'bird', 'cat', ...]
    print(sorted(animals, key=lambda s: len(s)))  # ['dog', 'cat', 'bird', ...]
    print(sorted(animals, key=len))  # ['dog', 'cat', 'bird', ...]

    filtered_animals = filter(lambda s: len(s) == 3, animals)
    print(list(filtered_animals))  # ['dog', 'cat']
