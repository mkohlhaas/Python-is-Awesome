#!/usr/bin/env python

from collections.abc import Generator
from random import random
from time import sleep

names = [
    "Daniel",
    "Mike",
    "William",
]

if __name__ == "__main__":
    # list compprehension (snippet: lc)
    evens1: list[int] = [i for i in range(100) if i % 2 == 0]
    print(evens1)

    # snippet lcie, (see also lci)
    print([i**3 if i % 2 == 0 else i**2 for i in range(10)])

    # set compprehension (snippet: sc)
    evens2: set[int] = {i for i in range(100) if i % 2 == 0}
    print(evens2)

    # generator comprehension
    evens3: Generator[int, None, None] = (i for i in range(100) if i % 2 == 0)
    for i in evens3:
        print(i, end="\r")
        sleep(0.05)
    print()

    evens4: tuple[Generator[int, None, None]] = ((i for i in range(100) if i % 2 == 0),)
    # unpacking the generator => creates a tuple of 50 ints!!!
    evens5: tuple[int, ...] = (*(i for i in range(100) if i % 2 == 0),)
    print(evens5)

    # number1: int = (1)
    number1: int = 1  # parens automatically removed from the formatter
    number2: tuple[int] = (1,)

    # dictionary compprehension (snippet: dc)
    numbers = [1, 2, 3, 4, 5]
    words = ["one", "two", "three", "four", "five"]
    dict_num_words = {number: word for number, word in zip(numbers, words)}
    print(dict_num_words)

    print({i: i**2 for i in range(20) if i % 2 == 0})

    # using a double list comprehension
    # readibilaty suffers
    results = [value for _ in numbers for value in [random()] if value > 0]
    print(results)

    # The same with the *Walrus Operator*.
    # Especially helpful for expensive operations which `random` is not.
    # https://realpython.com/python-walrus-operator/#list-comprehensions
    results = [value for _ in numbers if (value := random()) > 0]
    print(results)

    # another easy example for dictionary comprehensions
    print({name: len(name) for name in names})
