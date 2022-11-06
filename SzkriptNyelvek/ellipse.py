#!/usr/bin/env python3

import math


class Ellipse:
    def __init__(self, A, B, C):
        self.sugarA = A
        self.sugarB = B
        self.sugarC = C

    #4/3 * π * A * B * C
    def terfogat(self):
        return 4/3*math.pi*self.sugarA*self.sugarB*self.sugarC
    # a √((a² + c²)/2)

    def felszin(self):
        return self.sugarA*math.sqrt((self.sugarA**2+self.sugarC**2)/2)

    def __str__(self):
        return "Térfogat: {0} felszín: {1}".format(round(self.terfogat(), 2), round(self.felszin(), 2))


def main():
    e1 = Ellipse(10, 20, 30)
    e2 = Ellipse(30, 20, 10)
    print(str(e1))
    print(str(e2))


if __name__ == '__main__':
    main()
