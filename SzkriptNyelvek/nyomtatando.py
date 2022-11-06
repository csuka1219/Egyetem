#!/usr/bin/env python3
from typing import List


def get_pages(s: str) -> List[int]:
    result = []
    splitted_s = s.split(",")
    for item in splitted_s:
        if len(item) == 1:
            result.append(int(item))
            continue
        interval = item.split("-")
        result.extend(list(range(int(interval[0]), int(interval[1])+1)))
    return sorted(result)


def main():
    # 1-4,7,9,11-15
    print(get_pages("1-4,9,7,11-15"))


if __name__ == "__main__":
    main()
