#!/usr/bin/env python3

def main():
    osszeg = 0
    for x in range(256):
        osszeg += 2**x

    eredmeny = str(osszeg)
    print(f"eredmény: {len(eredmeny)}")


if __name__ == "__main__":
    main()
