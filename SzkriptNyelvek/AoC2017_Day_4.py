#!/usr/bin/env python3

def main():
    result = 0
    with open("aoc.txt", "r") as f:
        for sor in f:
            szavak = sor.rstrip('\n').split()
            sor_tuple = set(szavak)
            if len(szavak) == len(sor_tuple):
                result += 1
    print(result)


if __name__ == "__main__":
    main()
