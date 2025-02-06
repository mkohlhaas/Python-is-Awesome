#!/usr/bin/env python

# lists are references
myTuple = ([1, 2], [3])


if __name__ == "__main__":
    print(myTuple)
    myTuple[1].append(4)
    print(myTuple)
