#!/usr/bin/env python3

def median(li):
    if len(li) % 2 == 0:
        li = sorted(li)
        n1 = li[len(li)//2]
        n2 = li[len(li)//2-1]
        print((n1+n2)/2)
    else:
        li = sorted(li)
        print(li[len(li)//2])


def main():
    median([1, 2, 3, 4, 5])
    median([3, 1, 2, 5, 3])
    median([1, 300, 2, 200, 1])
    median([3, 6, 20, 99, 10, 15])


if __name__ == "__main__":
    main()
