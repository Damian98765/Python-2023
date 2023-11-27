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

# wczytaj przy użyciu input() liczbę; wypisz sumę jej cyfr
# moje rozwizanie
suma = 0
liczba = input("Podaj liczbę")
for cyfra in liczba:
    suma += int(cyfra)
print(f"Suma liczby {liczba} wynosi: {suma}.")

# rozwizanie prowadzcego
suma = 0
liczba = int(input("Podaj liczbę"))
while liczba > 0:
    suma += liczba % 10
    liczba //= 10
print(suma)
