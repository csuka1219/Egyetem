#!/usr/bin/env python3

def main():
    result = 0
    with open("table.txt", "r") as f:
        for line in f:
            line = line.rstrip('\n')
            li = [int(x) for x in line.split()]
            result += max(li)-min(li)
    print(result)


if __name__ == "__main__":
    main()
