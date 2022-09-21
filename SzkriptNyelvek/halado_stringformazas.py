#!/usr/bin/env python3

def main():

    lang_info = [(1, 'Python', 15.74), (2, 'C', 13.96),
                 (3, 'C++', 11.72), (4, 'Java', 9.76),
                 (5, 'C#', 4.88)]
    print("")
    print("\033[4mMost used programming languages\033[0m")
    print("")
    print('\033[1m'+"{0:<12} {1:^16} {2:>16} \033[0m".format("Place",
                                                             "Language",
                                                             "Ratings"))
    print("-"*46)
    for element in lang_info:
        print("{0:<12} {1:^16} {2:16}".format(element[0], element[1],
                                              element[2]))


if __name__ == "__main__":
    main()
