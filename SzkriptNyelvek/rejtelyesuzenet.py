#!/usr/bin/env python3

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""
# "K → M, O → Q, E → G".


def main():

    result = ""
    diff = ord("M")-ord("K")
    for c in TEXT:
        charascii = ord(c)
        if charascii > 120 or (charascii > 88 and charascii < 97):
            charascii -= 26
        if charascii < 63 or (charascii > 90 and charascii < 96-diff) or charascii > 122:
            charascii -= diff
        result += chr(charascii+diff)

    print(result)


if __name__ == "__main__":
    main()
