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


class MyQueue:
    def __init__(self):
        self.verem = Verem()

    def append(self, value):
        self.verem.betesz(value)

    def is_empty(self):
        return self.verem.meret() == 0

    def size(self):
        return len(self.verem.data)

    def popleft(self):
        verem2 = Verem()
        for i in range(1, self.size()):
            verem2.betesz(self.verem.kivesz())
        result = self.verem.kivesz()
        self.verem = verem2
        return result

    def __str__(self):
        result = []
        for i in range(0, self.size()):
            result.append(self.verem.kivesz())
        for r in result:
            self.verem.betesz(r)
        return str(result)


def main():
    s = MyQueue()
    print(s)
    print(s.is_empty())
    s.append(1)
    s.append(4)
    s.append(5)
    print(s)
    print("méret")
    print(s.size())
    print(s.is_empty())
    x = s.popleft()
    print(x)
    print(s)
    s.popleft()
    s.popleft()
    x = s.popleft()
    print(x)


if __name__ == '__main__':
    main()
