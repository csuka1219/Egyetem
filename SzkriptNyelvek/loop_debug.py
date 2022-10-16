#!/usr/bin/env python3

def loop(number, debug=False):
    '''kiírja a pozitív egész számokat a megadott paraméterig, debug verzióban jelzi a ciklus elejét és végét'''
    if (debug):
        print("# ciklus kezdete:")

    for i in range(1, number+1):
        print(i, end=" ")

    print()
    if (debug):
        print("# ciklus vege")


def main():
    loop(5)
    loop(5, True)


if __name__ == "__main__":
    main()
