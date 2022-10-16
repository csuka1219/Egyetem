#!/usr/bin/env python3

def diamond(n):
    if (n % 2 == 0):
        print("A megadott szám nem páratlan!")
        return
    for i in range(n):
        print(" "*(n-i), "*"*(i*2+1))
    for i in range(n-2, -1, -1):
        print(" "*(n-i), "*"*(i*2+1))


def main():
    diamond(4)
    diamond(5)
    diamond(7)


if __name__ == "__main__":
    main()
