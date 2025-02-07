#!/usr/bin/env python

balance = 934.40

if __name__ == "__main__":
    while True:
        try:
            num = float(input("Deposit: "))
            break
        except ValueError:
            print("Must be a valid amount!")
    balance += num
    print(f"Balance: {balance}")
