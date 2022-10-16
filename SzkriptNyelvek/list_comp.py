#!/usr/bin/env python3

def egy():
    small = ['auto', 'villamos', 'metro']
    big = [str.upper(s) for s in small]
    print(big)


def ketto():
    small = ['aladar', 'bela', 'cecil']
    capi = [str.capitalize(s) for s in small]
    print(capi)


def harom():
    li = [0 for n in range(10)]
    print(li)


def negy():
    li = [n for n in range(1, 11)]
    li2 = [n*2 for n in li]
    print(li2)


def ot():
    li = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    li2 = [int(s) for s in li]
    print(li2)


def hat():
    s1 = "1234567"
    li = [c for c in s1]
    print(li)


def het():
    s1 = 'The quick brown fox jumps over the lazy dog'
    li = [len(s) for s in s1.split(" ")]
    print(li)


def nyolc():
    s1 = "python is an awesome language"
    li = [s[0] for s in s1.split(" ")]
    print(li)


def tiz():
    li = [n for n in range(0, 10, 2)]
    print(li)


def tizenegy():
    li = [n**2 for n in range(0, 20, 2) if n**2 % 2 == 0]
    print(li)


def tizenketto():
    li = [n**2 for n in range(0, 20, 2) if str(n**2)[-1] == '4']
    print(li)


def tizennegy():
    li = [' apple ', ' banana ', ' kiwi']
    li2 = [s.strip() for s in li]
    print(li2)


def tizenot():
    li = [1, 0, 1, 1, 0, 1, 0, 0]
    s1 = "".join(str(n) for n in li)
    print(s1)


def main():
    egy()
    ketto()
    harom()
    negy()
    ot()
    hat()
    het()
    nyolc()
    tiz()
    tizenegy()
    tizenketto()
    tizennegy()
    tizenot()


if __name__ == "__main__":
    main()
