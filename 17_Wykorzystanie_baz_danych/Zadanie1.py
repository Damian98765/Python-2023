# Zadanie bazujące na zadaniu z modułu 15: stwórz czytnik plików CSV bez użycia modułu CSV
#  - napisz skrypt który otworzy plik z danymi csv (nazwa podana z CLI)
#  - wypisze jego zawartość oddzielając pola tabulacją `\t`

# Jego treść: Załadować do bazy danych postgres pythonem zawartość pliku foods.csv

import sys
import psycopg2

connect_string = "dbname=my_database user=my_user password=secret host=127.0.0.1"

if __name__ == '__main__':
    file = sys.argv[1]
    with open(file) as f:
        next (f) # jeżeli nie chemy nagłówków
        with psycopg2.connect(connect_string) as connection:
            try:
                cursor = connection.cursor()
                for line in f:
                    lstrip = line.strip().split(",")
                    cursor.execute(f"INSERT INTO fooditem (name, price) VALUES ('{lstrip[1]}', {lstrip[2]});")
                # connection.commit() - nadmiarowe, robi autocommit
            except psycopg2.Error as e:
                print(e)
