#!/usr/bin/env python

from collections import deque

if __name__ == "__main__":
    numbers: deque[int] = deque([], maxlen=5)
    for i in range(10):
        numbers.append(i)
        print(numbers)
    numbers.appendleft(4)
    print(numbers)

    n = numbers.popleft()
    print(n)
