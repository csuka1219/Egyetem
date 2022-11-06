#!/usr/bin/env python3

def is_palindrome_dec(n: int) -> bool:
    n2 = n
    n_rev = 0
    while (n2 > 0):
        dig = n2 % 10
        n_rev = n_rev*10+dig
        n2 = n2//10
    if (n == n_rev):
        return True
    return False


def is_palindrome_bin(n: int) -> bool:
    n_bin = bin(n)
    n_bin = n_bin[2:]
    if n_bin == n_bin[::-1]:
        return True
    return False


def main():
    result = 0
    for i in range(1, 1000000):
        if is_palindrome_dec(i) and is_palindrome_bin(i):
            result += i
        i += 1
    print(result)


if __name__ == "__main__":
    main()
