#!/usr/bin/env python3

def normalize(s):
    return s.lower().replace(" ", "")


def is_anagramma(s1, s2):
    s1 = normalize(s1)
    s2 = normalize(s2)
    if sorted(s1) == sorted(s2):
        return True
    return False


def main():
    print(is_anagramma("listen", "silent"))
    print(is_anagramma("A gentleman", "Elegant man"))
    print(is_anagramma("nemjopelda", "masikszo"))


if __name__ == "__main__":
    main()
