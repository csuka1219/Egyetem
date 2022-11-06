#!/usr/bin/env python3

import math


class Gomb:
    def __init__(self, sugar):
        self.sugar = sugar

    def terfogat(self):
        return (4*self.sugar**3*math.pi)/3

    def felszin(self):
        return 4*self.sugar**2*math.pi

    def __lt__(self, other):
        return self.terfogat() < other.terfogat()

    def __le__(self, other):
        return self.terfogat() <= other.terfogat()

    def __ge__(self, other):
        return self.terfogat() >= other.terfogat()

    def __str__(self):
        return "Térfogat: {0} felszín: {1}".format(round(self.terfogat(), 2), round(self.felszin(), 2))


def main():
    g1 = Gomb(10)
    g2 = Gomb(30)
    print(str(g1))
    print(str(g2))
    print(g1 < g2)
    print(g1 > g2)
    print(g1 <= g2)
    print(g1 >= g2)


if __name__ == '__main__':
    main()
