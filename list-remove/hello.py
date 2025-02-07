#!/usr/bin/env python


if __name__ == "__main__":
    x = [1, 2, 3, 2, 1]
    # removes first occurrence of value
    x.remove(2)
    print(x)  # [1, 3, 2, 1]
    print(sum(x))  # 7
