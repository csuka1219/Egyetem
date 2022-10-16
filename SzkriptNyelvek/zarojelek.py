#!/usr/bin/env python3

def test(s):
    d = {'(': ')', '{': '}', '[': ']'}
    li = []
    for c in s:
        if c in d.keys():
            li.append(c)
        elif c in d.values():
            if d[li[-1]] == c:
                del li[-1]
    print(len(li) == 0)


def main():
    test("((5+3)*2+1)")
    test("{[(3+1)+2]+}")
    test("(3+{1-1)}")
    test("[1+1]+(2*2)-{3/3}")
    test("(({[(((1)-2)+3)-3]/3}-3)")


if __name__ == "__main__":
    main()
