#!/usr/bin/env python3

def is_palindrome(s):
    return len(s) < 2 or s[0] == s[-1] and is_palindrome(s[1:-1])


def main():
    if (is_palindrome("gorog")):
        print("Ez a szó palindrom")
    else:
        print("Ez a szó nem palindrom")

    if (is_palindrome("nemgorog")):
        print("Ez a szó palindrom")
    else:
        print("Ez a szó nem palindrom")


if __name__ == "__main__":
    main()
