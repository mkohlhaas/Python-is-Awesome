#!/usr/bin/env python

from functools import cache, cached_property, partial, partialmethod, wraps


def with_greeting(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Hello world!")
        return func(*args, **kwargs)

    return wrapper


@with_greeting
def add_1(x, y):
    """Adds two numbers"""
    print(x + y)


def add_2(x, y):
    """Adds two numbers"""
    return x + y


class Add:
    def add(self, x, y):
        return x + y

    add_two = partialmethod(add, 2)


@cache
def fibonacci(n: int) -> int:
    if n < 0:
        raise ("negative number")

    match n:
        case 0:
            return 0
        case 1 | 2:
            return 1
        case _:
            return fibonacci(n - 1) + fibonacci(n - 2)


class Sample:
    def __init__(self, lst):
        self.long_list = lst

    @cached_property
    def sum(self):
        return sum(self.long_list)


if __name__ == "__main__":
    # wraps
    add_1(2, 5)
    print(add_1.__name__)
    print(add_1.__doc__)

    # partial
    add_two = partial(add_2, 2)
    print(add_two(5))

    # partialmethod
    a = Add()
    print(a.add_two(5))

    # cache
    print(fibonacci(40))

    # cache_property
    obj = Sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(obj.sum)
