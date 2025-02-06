#!/usr/bin/env python


from functools import lru_cache
from time import sleep


# lru = least recently used
@lru_cache
def expensive_func(n: int):
    sleep(1)
    return n


if __name__ == "__main__":
    print("Running expensive functions...")
    print(expensive_func(1))
    print(expensive_func(2))
    print(expensive_func(3))
    print(expensive_func(4))

    print("\nResults are cached:")
    print(expensive_func(1))
    print(expensive_func(2))
    print(expensive_func(3))
    print(expensive_func(4))
