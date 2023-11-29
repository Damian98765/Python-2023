# Zadanie: Pobrać dane z https://restcountries.com/v3.1/name/Poland?fullText=true; Wyświetlić podstawowe informacje (np. il. mieszkańców, waluta itp.)

import sys
import requests
from pprint import pprint

if __name__ == '__main__':
    country = sys.argv[1]
    url = f"https://restcountries.com/v3.1/name/{country}?fullText=true"
    response = requests.request(method="GET", url=url)
    if not response.status_code == 200:
        print("Nie rozpoznano nazwy kraju.\nCzy używasz angielskich nazw?")
        exit(1)
    respJSON = response.json()[0]
    #pprint(respJSON)
    print (f'Wielkość populacji w {country} to: {respJSON["population"]}.\nStolicą tego kraju jest: {respJSON["capital"][0]}.')