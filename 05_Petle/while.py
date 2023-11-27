n = 5

while n > 0:
    print(n)
    n -= 1

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    print(f'{n} tak')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')
else:
    print('Koniec')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    print(f'{n} tak')
else:
    print('Koniec')

# Wypisać wszystkie liczby od 1 do 100 które spełniają warunek z poprzedniego zadania (suma jej cyfr dzieli się przez 7 oraz liczba jest parzysta)
i = 1
while i <= 100:
    if ((i % 10 + i // 10) % 7 == 0) and (i % 2 == 0):
        print(i)
    i += 1
