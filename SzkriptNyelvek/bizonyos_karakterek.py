#!/usr/bin/env python3

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    '''egy ciklussal végig megy a text paraméter karakterein sorban, majd vissza adja azoknak a karaktereknek a sztingjét ami megtalálható a chars sztringben'''
    result = ""
    result = [result.join(c) for c in text if c in chars]
    result = "".join(result)
    if (result == ""):
        return "\"\""
    return result


def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
    main()
