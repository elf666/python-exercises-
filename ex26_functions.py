# TYLKO IMIONA POLSKIE!
# napisz funkcje ktora jako parametr pobiera imie
# jesli imie jest zenskie (czy konczy sie na 'a') -> wydrukuj "Witam Pania"
# jesli imie jest meskie (nie konczy sie na 'a') -> wydrukuj "Witam Pana"

list_of_names = ['Marta', 'Piotrek', 'Hermenegilda']

def say_proper_hello(name):
    if name[-1] == 'a':
        print("Witam Pania")
    else:
        print("Witam Pana")

for name in list_of_names:
    say_proper_hello(name)
