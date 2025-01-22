#!/usr/bin/env python

from typing import NamedTuple

# not type-safe: no types for first, middle, last
# FullName = namedtuple("FullName", ("first", "middle", "last"))


class FullName(NamedTuple):
    first: str
    middle: str
    last: str


if __name__ == "__main__":
    my_name = FullName("John", "Bob", "Smith")
    print(my_name[0])
    print(my_name.first)

    # read-only
    # my_name[0] = "Mike"
    # my_name.first = "Mike"
