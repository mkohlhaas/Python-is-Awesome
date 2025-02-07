#!/usr/bin/env python

inputs = ["John", "Smith", "United States", "blue", 29]

if __name__ == "__main__":
    first, last, country, haircolor, age = inputs
    print(first, last, country, haircolor, age)

    first, last, *country_haircolor, age = inputs
    print(country_haircolor)  # ['United States', 'blue']

    # * is just the (un)packing operator (here with a wildcard '_')
    first, last, *_, age = inputs
    print(f"{first} {last} is {age} years old.")

    # this will throw an error during runtime
    # first, last, _, age = inputs
    # print(f"{first} {last} is {age} years old.")
