from dataclasses import dataclass


@dataclass
class Fruit: ...


@dataclass
class Apple(Fruit):
    name: str = "apple"


@dataclass
class Orange(Fruit):
    name: str = "orange"


# old way to do it:
# T = TypeVar("T")
# class Box(Generic[T]):
# ...


class Box[T]:
    def __init__(self) -> None:
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def remove(self, item: T) -> None:
        self.items.remove(item)


class OrangeBox(Box[Orange]): ...


if __name__ == "__main__":
    apple_box = Box[Apple]()
    apple_box.add(Apple())
    # apple_box.add(Orange())

    orange_box = Box[Orange]()
    orange_box = OrangeBox()
    orange_box.add(Orange())
    # orange_box.add(Apple())
