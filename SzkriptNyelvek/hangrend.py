#!/usr/bin/env python3

def gethangrend(s):
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'

    result = 0
    for c in MELY_MGHK:
        if (c in s):
            result += 1
            break
    for c in MAGAS_MGHK:
        if (c in s):
            result += 2
            break
    return result


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pff"]
    for w in words:
        result = gethangrend(w)
        if (result == 0):
            print(w + " -> semmilyen")
        elif (result == 1):
            print(w + " -> mély")
        elif (result == 2):
            print(w + " -> magas")
        else:
            print(w + " -> vegyes")


if __name__ == "__main__":
    main()
