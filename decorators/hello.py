#!/usr/bin/env python


from time import sleep, time
from typing import Callable


# structure of a decorator
def decorator(func: Callable[[], None]):
    def wrapper():
        ...
        func()
        ...

    return wrapper


def my_decorator(func: Callable[[], None]):
    def wrapper():
        start = time()
        print(f"Running: {func.__name__}")
        func()
        print(f"Completed in {round(time() - start)} seconds.\n")

    return wrapper


@my_decorator
def do_this():
    print("Doing this!")
    sleep(2)


@my_decorator
def do_that():
    print("Doing that!")
    sleep(3)


if __name__ == "__main__":
    do_this()
    do_that()
