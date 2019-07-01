# pobierz liczbe n
# jesli jest nieparzysta wypisz "Jest nieparzysta"
# jeśli jest podzielna przez 6 wypisz "Jest podzielna przez 6"
# jeśli jest podzielna przez 8 i przez 10 wypisz "Podzielna przez 80"
# we wszystkich innych wypadkach wypisz "nie chce się dzielić"

n = int(input("Podaj liczbę: "))
if(n == 0):
    print("Nie sprawdzam zer")
    quit()

if(n % 2 != 0):
    print("Liczba nieparzysta")
elif(n % 6 == 0):
    print("Liczba jest podzielna przez 6")
elif(n % 8 == 0 and n % 10 == 0):
    print("Liczba jest podzielna przez 80")
else:
    print("Liczba nie chce sie dzielic")
