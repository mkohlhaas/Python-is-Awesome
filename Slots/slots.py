#!/usr/bin/env python


from enum import Enum, auto


class Profile:
    __slots__: tuple[str, str] = ("name", "age")

    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()


if __name__ == "__main__":
    profile = Profile("John", 44)

    # At run-time because of slots!
    # AttributeError: 'Profile' object has no attribute 'gender' and no __dict__ for setting new attributes
    # profile.gender = Gender.MALE
    # print(profile.gender)

    # Has no dictionary because of slots:
    # print(profile.__dict__)

    # But is has slots_
    print(profile.__slots__)
