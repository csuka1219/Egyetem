#!/usr/bin/env python3
from enum import Enum


# Mély hangrendű magánhangzók: a, á, o, ó, u, ú.

# Magas hangrendű magánhangzók: e, é, i, í, ö, ő, ü, ű.

class Mely(Enum):
    a = "a"
    á = "á"
    o = "o"
    ó = "ó"
    u = "u"
    ú = "ú"


class Magas(Enum):
    e = "e"
    é = "é"
    i = "i"
    í = "í"
    ö = "ö"
    ő = "ő"
    ü = "ü"
    ű = "ű"


class Eredmeny(Enum):
    semmilyen = 0
    magas = 1
    mély = 2
    vegyes = 3


def get_hangrend(s):
    tmp = 0
    for enum in Magas:
        if enum.value in s:
            tmp += 1
            break
    for enum in Mely:
        if enum.value in s:
            tmp += 2
            break
    result = Eredmeny(tmp)
    return result.name


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
    for word in words:
        print(word, "→", get_hangrend(word))


if __name__ == "__main__":
    main()
