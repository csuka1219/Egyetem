#!/usr/bin/env python3

class Verem():
    def __init__(self):
        self.data = []

    def betesz(self, value):
        self.data.append(value)

    def kivesz(self):
        if self.ures():
            return None
        return self.data.pop()

    def meret(self):
        return len(self.data)

    def ures(self):
        return len(self.data) == 0

    def __str__(self):
        return str(self.data)[:-1]


class Sor:
    def __init__(self):
        self.data = []

    def ures(self):
        return self.meret() == 0

    def betesz(self, value):
        self.data.append(value)

    def meret(self):
        return len(self.data)

    def popleft(self):
        if self.ures():
            return None
        return self.data.pop()

    def __str__(self):
        return str(self.data[::-1])


def main():
    print("Verem:")
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret())  # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)

    print("_"*20)

    print("Sor:")
    s = Sor()
    print(s)
    print(s.ures())
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)
    print("méret")
    print(s.meret())
    print(s.ures())
    x = s.popleft()
    print(x)
    print(s)
    s.popleft()
    s.popleft()
    x = s.popleft()
    print(x)


if __name__ == '__main__':
    main()
