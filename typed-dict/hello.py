#!/usr/bin/env python

from typing import NotRequired, TypedDict


class ProfileT1(TypedDict):
    name: str
    age: int
    jobs: NotRequired[list[str]]


class ProfileT2(TypedDict, total=False):
    name: str
    age: int
    jobs: list[str]


ProfileT3 = TypedDict(
    "ProfileT3",
    {
        "name": str,
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

    # Type checker complains about "gender" as not defined.
    # Type checker basedpyright set to "strict" in pyproject.toml.
    profile1["gender"] = "Male"
    profile2["gender"] = "Male"
    profile3["gender"] = "Male"
