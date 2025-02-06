#!/usr/bin/env python


if __name__ == "__main__":
    # Lists are not hashable

    # coords_1: set[list[int]] = set()
    # a = [1, 2]
    # b = [2, 2]
    # coords_1.add(a)  # runtime TypeError: unhashable type: 'list'
    # coords_1.add(a)
    # coords_1.add(a)
    # coords_1.add(b)
    # print(coords_1)

    # Tuples are hashable

    coords_2: set[tuple[int, int]] = set()
    a = (1, 2)
    b = (2, 2)
    coords_2.add(a)
    coords_2.add(a)
    coords_2.add(a)
    coords_2.add(b)
    print(coords_2)

    # Memory Sharing

    # Lists (mutable)
    a = [1, 2]
    b = [1, 2]
    print(id(a))
    print(id(b))
    print(f"The same: {id(a) == id(b)}")

    # Tuples (immutable)
    a = (1, 2)
    b = (1, 2)
    print(id(a))
    print(id(b))
    print(f"The same: {id(a) == id(b)}")

    # Unpacking
    (a, b, c) = (1, 2, 3)
    print(a)
    print(b)
    print(c)

    # Packing
    nums = a, b, c
    print(nums)
