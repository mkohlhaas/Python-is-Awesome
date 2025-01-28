#!/usr/bin/env python

# import

# `type` as a Function
# type(object)                    -> the object's type
# type(name, bases, dict, **kwds) -> a new type

# `type` as a Class
# type = base class of all metaclasses

# Classes
class Foo1: ...


Foo2 = type("Foo1", (), {})


# Sub-Classing
class Bar1(Foo1): ...


Bar2 = type("Bar2", (Foo2,), {})


# With Instance Vars
class Baz1(Bar1):
    def __init__(self) -> None:
        self.number = 100


Baz2 = type("Baz2", (Bar2,), {"number": 100})

if __name__ == "__main__":
    t1 = type(5)
    t2 = type(t1)
    t3 = type(t2)
    # ...
    print(t1)  # <class 'int'>
    print(t2)  # <class 'type'>
    print(t3)  # <class 'type'>
    # ...
