#!/usr/bin/env python

# Task: Remove duplicates in a list but keeping order!

if __name__ == "__main__":
    old = ["a", "b", "a", "c", "b", "a"]

    # does not keep order
    new = list(set(old))  # ['b', 'a', 'c']
    print(new)

    # keeps order but very explicit
    new = []
    for item in old:
        if item not in new:
            new.append(item)
    print(new)  # ['a', 'b', 'c']

    # dict keeps order
    new = dict.fromkeys(old)
    print(new)
    new = list(new.keys())
    print(new)

    # as one-lines
    print(list(dict.fromkeys(old).keys()))  # ['a', 'b', 'c']
