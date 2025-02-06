#!/usr/bin/env python

# we want to find the most frequent item in a list

if __name__ == "__main__":
    lst = [1, 2, 1, 3, 4, 1, 2, 4, 1]
    most = max(lst)
    # not what we want
    print(f"Max value: {most}")  # 4

    print(f"Frequency of 1: {lst.count(1)}")  # 4
    print(f"Frequency of 2: {lst.count(2)}")  # 2
    print(f"Frequency of 3: {lst.count(3)}")  # 1
    print(f"Frequency of 3: {lst.count(4)}")  # 2

    # using key function
    most_frequent = max(lst, key=lst.count)
    print(f"Most frequent number: {most_frequent}")  # 1

    # optimised version
    print(set(lst))
    most_frequent = max(set(lst), key=lst.count)
    print(f"Most frequent number: {most_frequent}")  # 1
