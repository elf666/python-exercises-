# zmienna zdefiniowana wewnatrz funkcji (lokalna) jest dostepna tylko wewnatrz funkcji
# zmienna zdefiniowana wewnatrz funkcji istnieje tylko tak dlugo jak istnieje funkcja

def my_func():
	x = 10 # zmienna lokalna
	print("Value inside function:",x)

# my_func()
# print(x) # nie dziala

# x = 20 # zmienna globalna
# my_func()
# print("Value outside function:",x)

# zmienne zdefiniowane na zewnatrz funkcji (globalne) sa dostepne wewnatrz funkcji

# g = 'jestem globalna'
#
# def print_variables():
#     loc = "jestem lokalna"
#     print(loc,g)
#
# print_variables()

# nie mozemy modyfikowac zmiennych globalnych z wnetrz funkcji
# beda one traktowane jak zmienne lokalne

# g = "jestem globalna"
#
# def try_to_modify_global():
# 	g = 'zmienilam sie'
# 	print(g)
#
# try_to_modify_global()
# print(g)

# jesli chcemy zeby zmienna globalna dalo sie modyfikowac z wnetrza funkcji
# musimy ja zadeklarowac wewnatrz funkcji przy uzyciu slowa kluczowego 'global'

g = "jestem globalna"

def modify_global():
    global g # informacja, ze chce dzialac na zmiennej globalnej
    g = "zmienilam sie"

modify_global()
print(g)
#
# # ex28
