#!/usr/bin/env python3

def main():
    result = sum([n**2 for n in range(1, 11)])
    print("négyzetösszeg: "+str(result))
    result = sum([n for n in range(1, 11)])**2
    print("összeg négyzete: "+str(result))


if __name__ == "__main__":
    main()
