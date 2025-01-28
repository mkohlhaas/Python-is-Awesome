#!/usr/bin/env python

# every metaclass inherits from type
class Copyable(type):
    def __new__(cls, name, bases, namespace):
        # creating the Copyable class
        obj = super().__new__(cls, name, bases, namespace)

        def copy(self):
            return self.__class__(**self.__dict__)

        obj.copy = copy
        return obj


class Qux(metaclass=Copyable):
    def __init__(self, name, age, jobs=None) -> None:
        self.name = name
        self.age = age
        self.jobs = jobs or []


if __name__ == "__main__":
    q = Qux("Michael", 34, ["Software Engineer"])
    r = q.copy()
    print(q.name, r.name)
    print(q.age, r.age)
    print(q.jobs, r.jobs)

    q.age += 1
    print(q.age, r.age)
