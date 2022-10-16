#!/usr/bin/env python3

def main():
    li = [0, 4, 7, 5, 2, 6, 1, 3]
    print("+------------------------+")
    for i in range(7, -1, -1):
        print("|", end="")
        for j in range(8):
            if li[j] == i:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print("|")
    print("+------------------------+")


if __name__ == "__main__":
    main()
