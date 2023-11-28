s = {"a": 1, 'b': 2}
s
s = {1: "a", 2: 'b'}
s

s = {[1]: "a", 2: 'b'}  # Błąd
s = {tuple([1]): "a", 2: 'b'}
s
s = {"a": 1, 'b': 2}
s
s['a']
s['c']  # Błąd
s.get('a')
s.get('c', 0)
s['c'] = 3
s
del s['b']
s

s = {"a": 1, 'b': 2, 'c': 3}

for k in s.keys():
    print(k)

for k in s.values():
    print(k)

for k in s.items():
    print(k)

for k, v in s.items():
    print(k, v)

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_jednosci.get(7, 'tej liczby nie znam')

n = 3
if n == 1:
    print('jeden')
elif n == 2:
    print('dwa')
elif n == 3:
    print('trzy')
elif n == 4:
    print('cztery')
elif n == 5:
    print('pięc')
else:
    print('tej liczby nie znam')

s2 = {'d': 4}
s | s2

s |= {'e': 5}
s

'a' in s

s = {1: "a", 2: 'b', "ala": [3, 4]}

# Zadanie : dla listy napisów pobranej w pętli z wejścia wypisać słownik ilości wystąpień napisów, np. dla ['Ala', 'ma' 'kota', 'kota'] wypisać {'Ala': 1, 'ma': 1, ;'kota': 2}
l = []
d = {}
while True:
    napis = input("Podaj napis, a dodam go do listy: ").strip()
    if napis == "":
        break
    l.append(napis)

# for i in l:
#    if d.get(i, 0) == 0:
#        d[i] = 1 # d |= {i: 1}
#    else:
#        print (i)
#        d[i] += 1

# szybsze rozwiązanie
for i in l:
    d[i] = d.get(i, 0) + 1

print(f"Tak się sprawy mają: {d}")

dokończyć - gotowiec
zbiblioteki
from collections import Counter

c = Counter(lista)

# Zadanie: dla wczytanej liczby z wejścia z zakresu 1-999 wypisać jej postać słowną, np. dla 73 wypisać siedemdziesiąt trzy
jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",9: "dziewięć"}
nascie = {0: "dziesięć", 1: "jedenaście", 2: "dwanaście", 3: "trzynaście", 4: "czternaście", 5: "pietnaście", 6: "szesnaście", 7: "siedemnaście", 8: "osiemnaście", 9: "dziewietnaście"}
dziesiatki = {2: "dwadzieścia", 3: "trzydzieści", 4: "czterdzieści", 5: "pięćdziesiąt", 6: "sześćdziesiąt", 7: "siedemdziesiąt", 8: "osiemdziesiąt", 9: "dziewięćdziesiąt"}
setki = {1: "sto", 2: "dwieście", 3: "trzysta", 4: "czterysta", 5: "pięćset", 6: "sześćset", 7: "siedemset", 8: "osiemset", 9: "dziewięćset"}
tysiace = {1: "tysiąc", 2: "tysiące", 3: "tysiące", 4: "tysiące"}
# liczba = input("Podaj liczbę, a pokaże Ci jej postać słowną: ").strip()
# if liczba > 1000 - wykonać poniższy kod, a później encja tysiace z default "tysięcy"
if liczba > 99:
    print(setki.get(liczba // 100), end=' ')
    liczba%=100
if liczba > 19:
    print(dziesiatki.get(liczba // 10), jednosci.get(liczba % 10))
elif liczba > 9:
    print(nascie.get(liczba % 10))
else:
    print(jednosci.get(liczba % 10))
