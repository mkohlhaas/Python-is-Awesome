#!/usr/bin/env python


from datetime import datetime


if __name__ == "__main__":
    num_1 = 1_000_000
    num_2 = 2_000
    res = num_1 * num_2
    print(f"{res}")  # 2000000000
    print(f"{res:_}")  # 2_000_000_000
    print(f"{res:,}")  # 2,000,000,000

    # zero filling
    for n in (3, 20, 28):
        print(f"{n:09_b}")

    n = 14310023
    print(f"{n:_b}")  # 1101_1010_0101_1010_1000_0111
    print(f"{n:#_b}")  # 0b1101_1010_0101_1010_1000_0111
    print(f"{n:_x}")  # da_5a87
    print(f"{n:#_x}")  # 0xda_5a87
    print(f"{n:_o}")  # 6645_5207
    print(f"{n:#_o}")  # 0o6645_5207

    s = "Right Alignment"
    print(f"|{s:>20}|")  # |     Right Alignment|

    s = "Left Alignment"
    print(f"|{s:<20}|")  # |Left Alignment      |
    print(f"|{s:20}|")  # left assignment is default

    s = "Center Alignment"
    print(f"|{s:^20}|")  # |  Center Alignment  |

    # Padding
    s = "Right Alignment"
    print(f"|{s:->20}|")  # |-----Right Alignment|
    s = "Left Alignment"
    print(f"|{s:-<20}|")  # |Left Alignment------|
    s = "Center Alignment"
    print(f"|{s:-^20}|")  # |--Center Alignment--|

    # datetime format specifiers
    # e.g. https://www.w3schools.com/python/gloss_python_date_format_codes.asp
    now = datetime.now()
    print(f"{now:%d.%m.%y}")  # 07.02.25
    print(f"{now:%d.%m.%y %H:%M:%S}")  # 07.02.25 18:54:06
    # localized date times
    print(f"{now:%c}")  # Fri Feb  7 18:54:44 2025
    print(f"{now:%I%p}")  # 06PM

    # Floats
    n = 1234.56789
    print(n)  # 1234.56789
    print(f"{n:.2f}")  # 1234.57
    print(f"{n:.0f}")  # 1235
    print(f"{n:,.3f}")  # 1,234.568
    print(f"{n:_.3f}")  # 1_234.568

    # Debugging Tip
    a = 2
    b = 3
    print(f"{a + b = }")  # a + b = 5
    print(f"{bool(a) = }")  # bool(a) = True

    my_str = "My String"
    print(f"{my_str = }")  # my_str = 'My String'
