# stworz funkcje wypisujaca dane samochodu
# marke i rocznik podaj jako argumenty obowiazkowe
# ilosc_kol=4 i typ=spalinowy podaj jako argumenty domyslne

# wypisz wynik w formacie:
# "Samochod marki Ford, rocznik 2010, ma 4 kola i jest spalinowy"

# wypisz wyniki dla dwoch samochodow:
# dla jednego podaj tylko argumenty obowiazkowe
# dla drugiego podaj wszystkie 4 argumenty

def print_car_info(producent, year, wheels=4, type='spalinowy'):
    print(f"Samochod marki {producent}, rocznik {year}, ma {wheels} kola i jest {type}.")

print_car_info("Suzuki", 2017)
print_car_info("Galaxy", 2200, 3, "odrzutowy")
