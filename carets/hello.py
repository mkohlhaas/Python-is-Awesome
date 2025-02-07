#!/usr/bin/env python

# ^ (caret) is XOR-Operator - not exponentiation

if __name__ == "__main__":
    x = "b001"
    y = [x.find("0")]
    print(y)  # [1]
    z = len(y) ^ 2  # b01 xor b10 = b11 (3)
    print(z)  # 3
