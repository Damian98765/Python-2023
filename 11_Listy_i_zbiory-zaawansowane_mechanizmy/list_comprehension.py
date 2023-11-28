range(10)

list(range(10))

(x * x for x in range(10))

[x for x in range(10)]

[x * x for x in range(10)]

[x for x in range(10) if x % 2 == 0]

[x * x for x in range(10) if x % 2 == 0]

[(x, y, x * y) for x in range(3) for y in range(4)]

{x for x in range(10)}

{x // 2 for x in range(10)}

{x: x * x for x in range(10) if x % 2 == 0}



# Zadanie: stworzyć list comprehension na podstawie jednej listy z liczbami całkowitymi, ale z elementami o 6 większymi
[x+6 for x in range(10)]


# Zadanie: stworzyć list comprehension tupli składających się z w/w liczb całkowitych i ich reprezentacji jako napis, np. [(1, "1"), (2, "2")]
[(x, str(x)) for x in range (5)]


# Zadanie: biorąc słownik {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# stworzyć list comprehension nazw pojazdów cięższych niż 5000. Nazwy podać dużymi literami (uppercase)
s={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
[x.upper() for x in s.keys() if s[x]>5000]