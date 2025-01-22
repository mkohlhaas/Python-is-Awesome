#!/usr/bin/env python

from dataclasses import InitVar, dataclass, field, KW_ONLY
from enum import Enum, auto


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()


# @dataclass
# class Profile1:
#     name: str
#     age: int
#     gender: Gender

#     during run-time:
#     ValueError: mutable default <class 'list'> for field jobs is not allowed: use default_factory
#     Because it would be a shared list for all profile instances!!!
#     jobs: list[str] = []

# You can pass args to dataclass and field


@dataclass
class Profile2:
    name: str
    age: int
    gender: Gender
    jobs: list[str] = field(default_factory=list, repr=False)


@dataclass(frozen=True)
class Profile3:
    name: str
    age: int
    _: KW_ONLY
    gender: Gender


@dataclass
class Responder:
    cache_ttl: int = field(default=300, repr=False)
    disable_cache: InitVar[bool] = False

    def __post_init__(self, disable_cache: bool) -> None:
        if disable_cache:
            self.cache_ttl = 0

    @property
    def cache_disabled(self) -> bool:
        return self.cache_ttl == 0


if __name__ == "__main__":
    # Profile ##############################################

    # profile1 = Profile1("John", 55, Gender.MALE)
    # print(f"{profile1}")
    # print(f"{profile1!r}")
    #
    # profile2 = Profile1("Mike", 35, Gender.MALE)
    # print(f"{profile2}")
    #
    # profile1.jobs.append("developer")
    # print(f"{profile1}")

    profile1 = Profile2("John", 55, Gender.MALE)
    print(f"{profile1}")
    print(f"{profile1!r}")

    profile2 = Profile2("Mike", 35, Gender.MALE)
    print(f"{profile2}")

    profile1.jobs.append("developer")
    profile2.jobs.append("carpenter")
    print(f"{profile1}")
    print(f"{profile2}")

    # Expected 2 positional arguments
    # profile3 = Profile3("John", 55, Gender.MALE)

    profile3 = Profile3("John", 55, gender=Gender.MALE)

    # Attribute "gender" is read-only
    # profile3.gender = Gender.FEMALE

    # Responder ############################################

    r = Responder(disable_cache=True)
    print(r)
    print(r.cache_ttl)
    print(r.cache_disabled)
