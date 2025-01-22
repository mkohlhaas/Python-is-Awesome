#!/usr/bin/env python


from dataclasses import dataclass, field
from typing import Annotated, Any, override


@dataclass()
class Profile:
    name: str
    age: Annotated[int, lambda x: x > 0, lambda x: x < 100]
    jobs: list[str] = field(default_factory=list)

    @override
    def __setattr__(self, name: str, value: Any, /) -> None:
        if field := self.__dataclass_fields__.get(name):
            super().__setattr__(name, value)
            if metadata := getattr(field.type, "__metadata__", None):
                assert metadata[0](
                    value
                ), f"Invalid value passed to {name!r} field: {value!r} too small."
                assert metadata[1](
                    value
                ), f"Invalid value passed to {name!r} field: {value!r} too big."


if __name__ == "__main__":
    p = Profile("John", 35)
    p.age = -35
