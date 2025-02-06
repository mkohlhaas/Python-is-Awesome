#!/usr/bin/env python

links = [
    "www.youtube.com",
    "www.google.com",
    "www.wikipedia.org",
]

# we want to remove "www." from links

if __name__ == "__main__":
    for link in links:
        print(link.lstrip("www."))  # wrong: ikipedia.org
        print(link.lstrip("w."))  # the same (remove 'w' and '.' from left of link)

        print(link.removeprefix("www."))  # this is what you want
