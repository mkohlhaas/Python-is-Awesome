#!/usr/bin/env python

from collections import defaultdict

if __name__ == "__main__":
    str_items: defaultdict[str, list[str]] = defaultdict(list)
    str_items["John"].append("views")
    print(str_items)

    int1_items: defaultdict[str, int] = defaultdict(int)
    int1_items["John"] += 1
    print(int1_items)

    int2_items: defaultdict[str, int] = defaultdict(lambda: 7)
    int2_items["John"] += 1
    print(int2_items)
