#!/usr/bin/env python

import itertools as it
from time import sleep
import json


if __name__ == "__main__":
    colors = ["red", "green", "blue"]

    # loops forever
    # for i in it.cycle(colors):
    #     print(i)
    #     sleep(1)

    for i in it.chain("ABC", "DEF"):
        print(i)

    for i in it.chain(*it.tee(colors, len(colors))):
        print(i)

    # with list (could be a problem if file is huuuuuge)
    print("\nList version:")
    with open("lyrics.txt", "r") as f:
        lines = f.readlines()

    # print chorus
    for line in lines[6:11]:
        print(line.strip())

    # with itertools
    print("\nLazy/Itertools version:")
    with open("lyrics.txt", "r") as f:
        for line in it.islice(f, 6, 11):
            print(line.strip())

    with open("person.json", "r") as f:
        p = json.load(f)

    print("\ndropwhile:")
    for k, v in it.dropwhile(lambda kv: kv[0] != "address", p.items()):
        print(f"{k}:\t{v}")

    print("\ntakewhile:")
    for k, v in it.takewhile(lambda kv: kv[0] != "address", p.items()):
        print(f"{k}:\t{v}")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("\nfilter:")
    for n in filter(lambda n: n % 2 == 0, numbers):
        print(n)

    print("\nfilterfalse:")
    for n in it.filterfalse(lambda n: n % 2 == 0, numbers):
        print(n)

    print("\nrange:")
    for i in range(10):
        print(i)

    # starts at 10 and never stops
    # print("\ncount:")
    # for i in it.count(10, 2):
    #     print(i)

    print("\nzip_longest:")
    odd_numbers = [1, 3, 5, 7, 9, 11]
    even_numbers = [2, 4, 6]
    for n in it.zip_longest(odd_numbers, even_numbers):
        print(n)

    print("\nstarmap:")
    for n in it.starmap(pow, [(2, 5), (3, 2), (10, 3)]):
        print(n)
