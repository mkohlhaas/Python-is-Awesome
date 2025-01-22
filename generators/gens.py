#!/usr/bin/env python

import sys
from time import sleep


def double(n: int):
    v = 1
    while n > 0:
        yield v
        # print(n)
        n -= 1
        v *= 2
        sleep(0.015)


if __name__ == "__main__":
    # Example generator (ranke)
    for i in range(10):
        print(i)

    print(type(double(10)))

    for i in double(5):
        print(i)

    gen = double(5)
    for i in gen:
        print(i)

    # nothing left to yield
    # print(next(gen))

    sys.set_int_max_str_digits(100_000)
    for i in double(50):
        print(i, end="\r")
    print()

    # list comprehension
    lst = [i % 2 == 0 for i in double(10)]
    print(lst)

    # generator comprehension
    gen = (i % 2 == 0 for i in double(10))
    for i in gen:
        print(i)

    gen = (i % 2 == 0 for i in range(10))
    for i in gen:
        print(i)

    # NOTE:Additional parens not needed in `all` and `any`
    # all
    if all(i % 2 == 0 for i in double(10)):
        print("All even!")
    else:
        print("Not all are even!")
    if all(i % 2 == 0 for i in range(10)):
        print("All even!")
    else:
        print("Not all are even!")

    # any
    if any(i % 2 == 0 for i in double(10)):
        print("Any are even!")
    else:
        print("All are odd!")
    if any(i % 2 == 0 for i in range(10)):
        print("Any are even!")
    else:
        print("All are odd!")
