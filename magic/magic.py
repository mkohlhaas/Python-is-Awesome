#!/usr/bin/env python


from typing import Self


class Human:
    def __init__(self, name, age, jobs=None):
        self.name = name
        self.age = age
        self.jobs = jobs

    def __init_subclass__(cls, meme=None):
        print(meme)

    def __str__(self) -> str:
        return f"{self.name}, {self.age}"

    def __repr__(self) -> str:
        return f"Human(name={self.name!r}, age={self.age!r})"

    def __int__(self):
        return self.age

    def __hash__(self) -> int:
        return hash(self.name) + hash(self.age)

    def __add__(self, other: Self) -> Self:
        return type(self)(
            self.name + "-" + other.name, round((self.age + other.age) / 2)
        )

    def __sub__(self, other: Self) -> Self:
        return type(self)(
            other.name + "-" + self.name, round((self.age + other.age) / 2)
        )

    # ...+= ...
    def __iadd__(self, other: Self) -> Self:
        return type(self)(
            self.name + "-" + other.name, round((self.age + other.age) / 2)
        )

    def __eq__(self, other: Self) -> bool:
        return self.name == other.name

    def __lt__(self, other: Self) -> bool:
        return self.name < other.name

    def __contains__(self, param):
        return True if param in self.__dict__.keys() else False

    def __getitem__(self, index):
        return self.jobs[index] if self.jobs else None

    def __getattr__(self, name: str):
        return self.jobs if name == "jobs" else None


class Test(Human, meme="Michael Kohlhaas"): ...


if __name__ == "__main__":
    print(Human("Michael", 55))
    print(repr(Human("Michael", 55)))
    print(int(Human("Michael", 55)))
    print(hash(Human("Michael", 55)))
    michael1 = Human("Michael", 25)
    andy = Human("Andy", 52)
    print(michael1 + andy)
    print(michael1 - andy)

    michael1 += andy
    print(michael1)
    print(michael1 == andy)
    print(michael1 != andy)

    michael1 = Human("Michael", 25)
    michael2 = Human("Michael", 52)
    print(michael1 == michael2)
    print(michael1 != michael2)

    print(michael1 < michael2)
    print(michael2 < michael1)
    print(andy < michael1)
    print(michael1 > andy)

    print("name" in michael1)
    print("last_name" in michael1)

    david = Human("David", 21, jobs=["programmer"])
    print(david[0])
    print(michael1[0])

    print(michael1.jobs)
    print(david.jobs)
    print(david.job)
