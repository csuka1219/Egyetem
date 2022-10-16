#!/usr/bin/env python3

def main():
    '''kiírja az ezernél kisebb 3-mal és 5-tel osztható számok összegét'''
    print("Megoldás: ",
          sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]))


if __name__ == "__main__":
    main()
