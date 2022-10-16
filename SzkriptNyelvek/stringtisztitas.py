#!/usr/bin/env python3

def clearstring(s):
    return " ".join(s.split()).replace(" ", "")


def main():
    print(clearstring("192.20.246.138:\n 6666"))
    print(clearstring("206.130.99.82:\n8080"))


if __name__ == "__main__":
    main()
