#!/usr/bin/env python3

def main():
    with open("string1.py", "r") as f, open("string1_clean.py", "w") as to:
        for sor in f:
            if len(sor.split()) == 0:
                continue
            if sor[0] != '#':
                to.write(sor)
    with open("string1_clean.py", "r") as f, open("string1_clean2.py", "w") as to:
        for sor in f:
            if len(sor.split()) == 0:
                continue
            elso_szo = sor.split()[0]
            if elso_szo[0] != '#':
                to.write(sor)


if __name__ == "__main__":
    main()
