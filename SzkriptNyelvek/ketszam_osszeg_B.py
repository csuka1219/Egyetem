#!/usr/bin/env python3

def main():
    a = input("Adjon meg egy számot: ")
    if a.isnumeric():
        a = int(a)
    else:
        print("Nem számot adott meg!")
        return
    b = input("Adjon meg egy másik számot: ")
    if b.isnumeric():
        b = int(b)
    else:
        print("Nem számot adott meg!")
        return
    print(f"Eredmény: {a + b}")


if __name__ == "__main__":
    main()
