#!/usr/bin/env python3

import math


def distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0])**2)+((p1[1] - p2[1])**2))


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

#############################################################################


if __name__ == "__main__":
    main()
