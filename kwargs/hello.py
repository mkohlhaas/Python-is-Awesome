#!/usr/bin/env python


# kwargs is a dictionary
# kwargs: dict[str, Unknown]
def func(**kwargs):
    print(kwargs)
    return kwargs["a"] * kwargs["b"] + kwargs["c"]


if __name__ == "__main__":
    print(func(a=1, b=2, c=3))
    print(func(c=3, a=1, b=2))
    print(func(b=2, a=1, c=3))
