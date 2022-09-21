#!/usr/bin/env python3

def szam_fordito(n):
    temp = str(n)
    temp = temp[::-1]
    n = int(temp)
    return n


def main():
    szam1 = 21321
    szam2 = 12345
    szam3 = 7346
    print(f"{szam1} ---> {szam_fordito(szam1)}")
    print(f"{szam2} ---> {szam_fordito(szam2)}")
    print(f"{szam3} ---> {szam_fordito(szam3)}")


if __name__ == "__main__":
    main()
