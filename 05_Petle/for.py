for i in range(12):
    print(i)

for i in range(3, 12):
    print(i)

for i in range(3, 12, 2):
    print(i)

for c in "Ala ma kota":
    print(c)

for i in range(10):
    print(i)
else:
    print("Koniec")

for i in range(10):
    print(i)
    if i > 6:
        break
else:
    print("Koniec")

#wczytaj przy użyciu input() liczbę; wypisz sumę jej cyfr
suma = 0
liczba = input("podaj liczbę")
for i in liczba:
    suma += int (i)
print (suma)
