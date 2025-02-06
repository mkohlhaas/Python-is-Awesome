#!/usr/bin/env python


def merge_arrays(a: list[int], b: list[int]) -> list[int]:
    # 1. merge
    # 2. remove duplicates
    # 3. sort in ascending order
    return sorted(set(a + b))


if __name__ == "__main__":
    a = [1, 2, 3, 3, 4, 5, 6]
    b = [4, 4, 5, 6, 7, 8, 9]
    print(merge_arrays(a, b))
