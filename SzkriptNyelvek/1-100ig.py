#!/usr/bin/env python3

def get_sumofdigits(s):
    result = 0
    for d in s:
        result += int(d)
    return str(result)


def main():
    strnumbers = "".join([str(n) for n in range(1, 101)])
    print("Számjegyek összege: " + get_sumofdigits(strnumbers))


if __name__ == "__main__":
    main()
