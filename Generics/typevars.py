#!/usr/bin/env python

from typing import TypeVar


# T = TypeVar("T")
T = TypeVar("T", bound=int)


def echo(val: T) -> T:
    return val


if __name__ == "__main__":
    _ = echo(2)
    _ = echo(True)
    # _ = echo("I am string.")
