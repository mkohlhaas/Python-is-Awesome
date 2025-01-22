#!/usr/bin/env python

from typing import NotRequired, TypedDict, Unpack


class Kwargs(TypedDict):
    name: str
    age: NotRequired[int]


# standard Python<=3.11 style
def profile1(**kwargs: str | int):
    for k, v in kwargs.items():
        print(f"{k}: {v}")


def profile2(**kwargs: Unpack[Kwargs]):
    for k, v in kwargs.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    profile1(name="John", age=34)
    profile2(name="John", age=34)

    profile1(name="John")
    profile2(name="John")  # with age not NotRequired will throw an error

    profile1(name="John", age="34")
    # profile2(name="John", age="34")

    # profile1(name="John", age=34, jobs=["carpenter", "programmer"])
    # profile2(name="John", age=34, jobs=["carpenter", "programmer"])
