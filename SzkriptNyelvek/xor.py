#!/usr/bin/env python3

def xor(s1, s2):
    if (bool(s1) != bool(s2)):
        return True
    return False


def main():
    print(xor("python", None))
    print(xor("python", "masikpython"))
    print(xor(None, None))


if __name__ == "__main__":
    main()
