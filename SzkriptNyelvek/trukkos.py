#!/usr/bin/env python3
from audioop import reverse


TEXT = """
01111001 
01101111
01110101
01110100
01110101
00101110
01100010
01100101
00101111
01100100
01010001
01110111
00110100
01110111
00111001
01010111
01100111
01011000
01100011
01010001
"""


def main():
    for item in TEXT.split():
        res = 0
        item = item[::-1]
        for i in range(8):
            if int(item[i]) == 1:
                res += 2**i

        print(chr(res), end="")
    print()


if __name__ == "__main__":
    main()
