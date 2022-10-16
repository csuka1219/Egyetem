#!/usr/bin/env python3



TEXT = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""


def main():
    # áéíóöőúüűÁÉÍÓÖŐÚÜŰ
    d = {'á': 'a',
         'é': 'e', 'í': 'i', 'ó': 'o', 'ö': 'o', 'ő': 'o', 'ú': 'u', 'ü': 'u', 'ű': 'u'}
    tmp = d.copy()
    for k, v in tmp.items():
        d[k.upper()] = v.upper()
    result = TEXT
    for k, v in d.items():
        result = result.replace(k, v)
    print(result)


if __name__ == "__main__":
    main()
