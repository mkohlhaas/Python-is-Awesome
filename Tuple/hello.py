#!/usr/bin/env python

from typing import override


class Parent:
    def capitalise(self, text: str):
        return text.upper()


class Child(Parent):
    @override
    # def capitalise(self, text: str):
    # not allowed (violates the Liskov Substitution Principle(LSP)):
    def capitalise(self, text: int):
        return str(text).upper()


if __name__ == "__main__":
    one_1: tuple[str, str, str] = ("one", "two", "three")
    # basedpyright doesn't accept this:
    one_2: tuple[str, ...] = ("one", 2, 3.0)

    child = Child()
    print(child.capitalise(1))
    print(child.capitalise("one"))
