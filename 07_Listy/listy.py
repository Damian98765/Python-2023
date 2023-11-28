l = [3, 5, 6, 7]
l

l[1]
l[0]
len(l)
l[0:2]
l[1:2]
l[1:]
l[:2]
l[-1]
l[1:-1]
l[-4]
l[1:-1] + l[0:-1]

for i in range(len(l)):
    print(l[i])

for i in l:
    print(i)

l * 4

l.index('3')  # Błąd
l.index(3)

l[1] = 17
l
del l[3]
l
l.append(19)
l
l += ['A', 'B']
l
l.pop()
l

" - ".join(["Ala", "ma", "kota"])
"".join(["Ala", "ma", "kota"])
" ".join(["Ala", "ma", "kota"])
s2 = '.|.'
s2.join(["Ala", "ma", "kota"])

'.' in s2

# zadanie: stwórz pętle pobierającą napisy z wejścia aż do napotkania pustego napisu; wypisz listę posortowaną alfabetycznie wczytanych napisów
l = []
while True:
    napis = input("Podaj napis, a dodam go do listy: ").strip()
    if napis == "":
        break
    l.append(napis)
l.sort()
print(f"Posortowałem Ci tą listę: {l}")

# stwórz pętle pobierającą liczby z wejścia aż do napotkania pustego napisu; wypisz ostatnią parzystą
l = []
while True:
    liczba = input("Podaj liczbę, a dodam ją do listy: ").strip()
    if liczba == "":
        break
    l.append(int(liczba))
l.sort()
for i in range(1, len(l)):
    if l[-1*i]%2 == 0:
        print(f"Ostatnia parzysta liczba to: {l[-1*i]}")
        break