#!/usr/bin/env python


from time import time


num_items = 30_000_000

if __name__ == "__main__":
    # Dynamic Storage
    start = time()
    lst_1 = []
    for n in range(num_items):
        lst_1.append(n)
    print(f"{time() -start} seconds.")

    # Pre-Allocation
    start = time()
    lst_2 = [0] * num_items
    for n in range(num_items):
        lst_2[n] = n
    print(f"{time() -start} seconds.")
