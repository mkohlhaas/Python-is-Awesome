#!/usr/bin/env python


from typing import override


class Fruit:
    def grow(self):
        print("I have grown!")

    def eat(self):
        print("Enjoy your meal!")


class Banana(Fruit):
    # if you rename function name in base class will throw a type error
    @override
    def eat(self):
        print("Enjoy your potassium!")


if __name__ == "__main__":
    b = Banana()
    b.eat()
