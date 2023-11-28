nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_nastki = {11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "piętnaście",
                16: "szesnaście", 17: "siedemnaście", 18: "osiemnaście", 19: "dziewietnaście"}
nazwy_dziesiatki = {0: "", 10: "dziesięć", 20: "dwadzieścia", 30: "trzydzieści", 40: "czterdzieści", 50: "pięćdziesiąt",
                    60: "sześćdziesiąt", 70: "siedemdziesiąt", 80: "osiemdziesiąt", 90: "dziewięćdziesiąt"}
nazwy_setki = {0: "", 100: "sto", 200: "dwieście", 300: "trzysta", 400: "czterysta", 500: "pięćset", 600: "sześćset",
               700: "siedemset", 800: "osiemset", 900: "dziewięćset"}


def _sklej(lista):
    return " ".join([x[1] for x in lista])


def dodaj_jednostke(lista, jednostki):
    print(f'Lista przy dodawaniu jednostek {lista}')
    if len(lista) == 1 and lista[0][0] == 1:
        lista = [(1, jednostki[0])]

    elif lista[-1][0] >= 2 and lista[-1][0] <= 4:
        lista.append((0, jednostki[1]))
    else:
        lista.append((0, jednostki[2]))
    return lista


def slownie_do999(n, jednostki=["", "", ""]):
    lista = _slownie_do999(n)
    lista = dodaj_jednostke(lista, jednostki)
    return _sklej(lista)


def slownie(n):
    jednosci = n % 1000
    tysiace = (n // 1000) % 1000
    miliony = n // 1_000_000 % 1000
    miliardy = n // 1_000_000_000 % 1000

    lista = [slownie_do999(miliardy, jednostki=["miliard", "miliardy", "miliardów"]),
             slownie_do999(miliony, jednostki=["milion", "miliony", "milionów"]),
             slownie_do999(tysiace, jednostki=["tysiąc", "tysiące", "tysięcy"]),
             slownie_do999(jednosci)]

    return " ".join(lista)

# niekompletne - nie wszystko skopiowałem z czatu...