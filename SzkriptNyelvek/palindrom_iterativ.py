#!/usr/bin/env python3

def is_palindrome(s):
    i = 0
    s_length = len(s)
    while i < s_length:
        if (s[i] != s[s_length - 1]):
            return False
        s_length -= 1
        i += 1
    return True


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
