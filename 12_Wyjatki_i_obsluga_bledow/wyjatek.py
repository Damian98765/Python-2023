l = list(range(5, 10))
print(l)
try:
    i = int(input("podaj indeks "))
    print(f'Pod indeksem {i} jest element {l[i]}')
except IndexError as e:
    print(e)
else:
    print("Koniec")
finally:
    print("Finally")



# Zadanie: wczytaj przy użyciu `input` liczbę; wypisz sumę jej cyfr; jeśli podano błędne wejście, poproś jeszcze raz
liczba = 0
while True:
    try:
        liczba = input("Podaj liczbę naturalną: ")
        liczba = int(liczba)
    except ValueError as e:
        print (f'Wprowadzony tekst "{liczba}" nie jest liczbą!')
    else:
        break

suma = 0
i = liczba
while i > 0:
    suma += i%10
    i //= 10

print (f'Suma cyfr podanej liczby {liczba} wynosi: {suma}')
