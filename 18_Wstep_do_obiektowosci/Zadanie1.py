# Zadanie bazujące na zadaniu z modułu 15: stwórz czytnik plików CSV bez użycia modułu CSV
#  - napisz skrypt który otworzy plik z danymi csv (nazwa podana z CLI)
#  - wypisze jego zawartość oddzielając pola tabulacją `\t`

# Jego treść: Stworzyć klasę FoodItem z polami id, price item - specjalnymi metodami __init__ i __repr__, stworzyć listę FoodItem na podstawie pliku CSV

import sys

class FoodItem():
    def __init__(self, id, price, item):
        self.id = id
        self.price = price
        self.item = item

    def __repr__(self):
        return f'FoodItem("{self.id}", "{self.price}", "{self.item}")'

listFI= []
if __name__ == '__main__':
    file = sys.argv[1]
    with open(file) as f:
        next (f) # jeżeli nie chemy nagłówków
        for line in f:
            line_strip = line.strip().split(",")
            listFI.append(FoodItem (line_strip[0], line_strip[1], line_strip[2]))

print (listFI)