#!/usr/bin/env python3

def main():
    szam = 2**1000
    result = 0
    for n in str(szam):
        result += int(n)
    print(result)


if __name__ == "__main__":
    main()
