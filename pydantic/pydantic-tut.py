#!/usr/bin/env python

from pydantic import BaseModel, validator


def to_camel_case(text):
    camel_string = "".join(txt.capitalize() for txt in text.lower().split("_"))
    return text[0].lower() + camel_string[1:]


class Profile(BaseModel):
    name: str
    age: int
    my_jobs: list[str] = []

    class Config:
        validate_assignment = True
        alias_generator = to_camel_case

    @validator("age")
    def age_gt_0(cls, value: int) -> int:
        if value < 0:
            raise ValueError("age must be positive")
        return value


if __name__ == "__main__":
    api_resp = {"name": "Michael", "age": 25, "myJobs": ["Software Engineer"]}
    p = Profile(**api_resp)
    print(p)

    # still works
    api_resp = {"name": "Michael", "age": "25", "myJobs": ["Software Engineer"]}
    p = Profile(**api_resp)
    print(p)
    print(type(p.age))

    # error: Input should be a valid integer, unable to parse string as an integer
    # api_resp = {"name": "Michael", "age": "meme", "myJobs": ["Software Engineer"]}
    # p = Profile(**api_resp)
    # print(p)
    # print(type(p.age))

    # also works
    api_resp = {"name": "Michael", "age": "25", "myJobs": ("Software Engineer",)}
    p = Profile(**api_resp)
    print(p)

    # does not work!!!
    p = Profile(name="Michael", age=23, my_jobs=["Software Engineer"])
    print(p)

    # error: age must be positive
    # api_resp = {"name": "Michael", "age": "-1", "myJobs": ("Software Engineer",)}
    # p = Profile(**api_resp)
    # print(p)

    # errors because of ' validate_assignment = True'
    # p.age = -234
    # print(p)
