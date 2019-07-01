# uzywajac operatora * (czesto *args)
# mozna stworzyc funkcje pobierajaca nieznana ilosc zmiennych

# def greet(*names):
#     print("---")
#     for name in names:
#         print("Hello",name)
#
# greet("Monika", "Staszek", "Tomek", "Szymon")
# greet("Ada", "Ola")
# greet("Klaudia")
# greet()

#ex30

# uzywajac operatora ** (czesto **kwargs)
# mozna stworzyc funkcje pobierajaca nieznana ilosc argumentow typu klucz:wartosc

def print_key_values(**data):
    # data tutaj staje sie slownikiem
    for key, value in data.items():
        print("{} is {}".format(key,value))

print_key_values()
print_key_values(a="11", b="22", c="33")
print_key_values(key1=5, key2=10, key3=15, key4=20, key5=25)
