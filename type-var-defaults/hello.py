#!/usr/bin/env python

from typing import Generic, NotRequired, ReadOnly, TypeGuard, TypeIs, TypeVar, TypedDict
from warnings import deprecated


class Context: ...


class CustomContext: ...


# T = TypeVar("T")
T = TypeVar("T", default=Context)


# class App[T]:
class App(Generic[T]):
    context: T | None = None


@deprecated("Use `hello()` instead")
def hello_world():
    print("Hello, World!")


def hello(entity: str = "World"):
    print(f"Hello, {entity}!")


class User(TypedDict):
    id: ReadOnly[int]
    age: int
    jobs: NotRequired[list[str]]


class Dog:
    def bark(self):
        print("Woof, woof!")


class Cat:
    def meow(self):
        print("Meow!")


# This is a so-called type predicate function.
# Let the compiler know if `obj` is a dog or not.
# def is_dog(obj: object) -> TypeGuard[Dog]:
def is_dog(obj: object) -> TypeIs[Dog]:
    return isinstance(obj, Dog)


def speak(animal: Cat | Dog):
    if is_dog(animal):
        animal.bark()
    else:
        animal.meow()  # works with TypeIs, but not with TypeGuard


if __name__ == "__main__":
    app1 = App[CustomContext]()
    app1.context
    app2 = App()
    app2.context
    hello_world()
    hello()
    user: User = {"id": 12, "age": 34}
    print(user)
    user["id"] = 13
    print(user)
