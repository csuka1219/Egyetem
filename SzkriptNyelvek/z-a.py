#!/usr/bin/env python3
import os.path
import sys


def main():
    '''attól függően hogy szimbolikus linkkel vagy rendesen lett futtatva a program, 
    kiírja a képernyőre az angol abécét rendesen vagy vissza fele olvasva'''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    filename = sys.argv[0].split("/")[-1]
    if filename == "a-z.py":
        print(alphabet)
    else:
        print(alphabet[::-1])


if __name__ == "__main__":
    main()
