#!/usr/bin/env python3

def is_palindrome(s):
    return s[:] == s[::-1]


def main():
    if is_palindrome("abcd"):
        print("A string palindrómn")
    else:
        print("A string nem palindróm")
    if is_palindrome("ababa"):
        print("A string palindrome")
    else:
        print("A string nem palindrómn")


if __name__ == "__main__":
    main()
