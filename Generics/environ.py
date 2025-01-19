from collections.abc import Callable
import os
from typing import TypeVar, cast, final, overload


@final
class EnvVar[T]:
    C = TypeVar("C")

    @overload
    def __init__(
        self: "EnvVar[str|None]",
        name: str,
    ) -> None: ...

    @overload
    def __init__(
        self: "EnvVar[str]",
        name: str,
        *,
        default: str,
    ) -> None: ...

    @overload
    def __init__(
        self: "EnvVar[C]",
        name: str,
        *,
        default: str | None = None,
        converter: Callable[[str | None], C] | None = None,
    ) -> None: ...

    def __init__(
        self,
        name: str,
        *,
        default: str | None = None,
        converter: Callable[[str | None], C] | None = None,
    ) -> None:
        self.name = name
        self.default = default
        self.converter = converter

    @property
    def value(self) -> T:
        value = os.environ.get(self.name, self.default)
        if self.converter:
            return cast(T, self.converter(value))  # convert from C to T
        else:
            return cast(T, value)  # convert from str (or None) to T


def as_int(val: str | None) -> int:
    return int(val) if val else 0


if __name__ == "__main__":
    EnvVar[int]("FOO").value
    EnvVar("FOO").value
    EnvVar("FOO", default="bar").value
    EnvVar("FOO", converter=as_int).value
    EnvVar("FOO", converter=bool).value
