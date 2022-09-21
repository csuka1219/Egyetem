#!/usr/bin/env python3
import sys


def main():
    if len(sys.argv) != 3:
        print("hibás parancssori argumentum szám")
        return
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(f"Eredmény: {a + b}")


if __name__ == "__main__":
    main()
