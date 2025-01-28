#!/usr/bin/env python

from typing import NotRequired, ReadOnly, TypedDict


# only jobs is not required
class ProfileT1(TypedDict):
    name: ReadOnly[str]
    age: int
    jobs: NotRequired[list[str]]


# not all fields are required
class ProfileT2(TypedDict, total=False):
    name: ReadOnly[str]
    age: int
    jobs: list[str]


# alternative, newer syntax
ProfileT3 = TypedDict(
    "ProfileT3",
    {
        "name": ReadOnly[str],
        "age": int,
        "jobs": list[str],
    },
)

Point2D = TypedDict(
    "Point2D",
    {
        "x": int,
        "y": int,
    },
)


if __name__ == "__main__":
    profile1: ProfileT1 = {
        "name": "John",
        "age": 66,
        # "jobs": ["driver", "carpenter"],
        # "gender": "Male",
    }

    profile2: ProfileT2 = {
        "name": "John",
        # "age": 66,
        # "jobs": ["driver", "carpenter"],
        # "gender": "Male",
    }

    profile3: ProfileT3 = {
        "name": "John",
        "age": 66,
        "jobs": ["driver", "carpenter"],
        # "gender": "Male",
    }

    profile1["name"] = "Michael"
    profile2["name"] = "Michael"
    profile3["name"] = "Michael"

    profile1["gender"] = "Male"
    profile2["gender"] = "Male"
    profile3["gender"] = "Male"
