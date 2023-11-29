# Zadanie: stwórz czytnik plików CSV bez użycia modułu CSV
#  - napisz skrypt który otworzy plik z danymi csv (nazwa podana z CLI)
#  - wypisze jego zawartość oddzielając pola tabulacją `\t`

import sys

if __name__ == '__main__':
    file = sys.argv[1]
    with open(file) as f:
        next (f) # jeżeli nie chemy nagłówków
        for line in f:
            print ('\t'.join(line.strip().split(",")))