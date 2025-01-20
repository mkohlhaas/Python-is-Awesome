#!/usr/bin/env python

from collections.abc import Iterable, Iterator
from typing import override

# from typing import TypeVar
# T_co = TypeVar("T_co", covariant=True)


# T is covariant by default
class ImmutableList[T]:
    def __init__(self, items: Iterable[T]):
        self.items: Iterable[T] = items

    def __iter__(self) -> Iterator[T]:
        return iter(self.items)


# replaces the TypeVar bound parameter
class ImmutableEmployeeList[T: "Employee"]:
    def __init__(self, items: Iterable[T]):
        self.items: Iterable[T] = items

    def __iter__(self) -> Iterator[T]:
        return iter(self.items)


class Employee:
    def __init__(self, name: str):
        self.name: str = name

    @override
    def __repr__(self) -> str:
        return f"Employee({self.name!r})"


class Manager(Employee):
    @override
    def __repr__(self) -> str:
        return f"Manager({self.name!r})"


# also works with functions
def first[T](seq: Iterable[T]) -> T | None:
    try:
        return list(seq)[0]
    except IndexError:
        return None


# type is bound covariantly to Employee
def first_employee[T: "Employee"](seq: Iterable[T]) -> T | None:
    try:
        return list(seq)[0]
    except IndexError:
        return None


if __name__ == "__main__":
    people = ImmutableList([Employee("John"), Manager("Jane")])
    for p in people:
        print(p)

    # Also works:
    people = ImmutableList([Employee("John"), Manager("Jane"), 42])
    for p in people:
        print(p)

    # Throws typing error
    # for p in people:
    #     print(p.name)

    people = ImmutableEmployeeList([Employee("John"), Manager("Jane")])
    print(f"First item: {first(people)}")
    print(f"First item: {first([1,2,3])}")
    print(f"First employee: {first_employee(people)}")
    # print(f"First employee: {first_employee([1,2,3])}")
    for p in people:
        print(p)

    # doesn't work anymore
    # people = ImmutableEmployeeList([Employee("John"), Manager("Jane"), 42])
    # for p in people:
    #     print(p)
