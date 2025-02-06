#!/usr/bin/env python

from dataclasses import dataclass, field

# def append_to_list(item, lst=[]):
#     lst.append(item)
#     return lst


def append_to_list(item: int, lst: list[int] | None = None):
    if not lst:
        lst = []
    lst.append(item)
    return lst


@dataclass()
class Profile:
    name: str
    age: int
    jobs: list[str] = field(default_factory=list)


# class Profile:
#     def __init__(self, name: str, age: int, jobs: list[str] | None = None) -> None:
#         self.name: str = name
#         self.age: int = age
#         self.jobs: list[str] | None = jobs


if __name__ == "__main__":
    print(append_to_list(1))
    print(append_to_list(2))
    print(append_to_list(3))

    p1 = Profile("Michael", 36)
    # p1 = Profile("Michael", 36, ["Youtuber"])
    p2 = Profile("Andreas", 54)
    if not p1.jobs:
        p1.jobs = []
    p1.jobs.append("Software Engineer")
    print(f"{p1.jobs =}")
    print(f"{p2.jobs =}")
