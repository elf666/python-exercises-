# napisz petle for ktora pobiera liste elementow od <0 - 30>
# i wpisuje do nowej listy wszystkie, ktore sa podzielne przez 6


# zrob to samo co powyzej, ale przy uzyciu list comprehension


a = 'bardzo wielka anakonda'
# przy uzyciu slicow a[x:y:z] wypisz:
# 1) samo slowo 'anakonda'
# 2) co trzeci znak stringa
# 3) co druga litere stringa zaczynajac od indeksu=2, konczac (wlacznie) na indeksie=12


# przy uzyciu odpowiednich indeksow i kluczy wypisz True
# T = (1, 2, [1, 2, {'a': 1, 'b': 2, 'c': [1, True, 'aaa']}, 3, 4])


# napisz petle while ktora przeprowadza zaby przez droge
# pobierz ilosc zab przy drodze jako parametr z klawiatury
# uruchom petle w ktorej przenosisz po jednej zabie
# w kazdym obiegu petli wypisz, ze przeniesiono jedna zabe i ile zab zostalo
# wypisz informacje kiedy zostana przeniesione wszystkie zaby


# napisz funkcje, ktora  pobiera slownik
# D = {'ala':20, 'tomek':21, 'ola':34, 'staszek':55, 'grazyna':61}
# i wypisuje pary: imie -> wiek, ale TYLKO DLA KOBIET


# L = [9,8,8,1,3,5,3,6,8,9,3,2,6,7,4,5]
# stworz zbior unikalnych wartosci z listy L
# zamien zbior na liste
# posortuj liste
# wydrukuj te liste
# wszystko w jednej linijce!


W = ['jola33', 'kotek', 'Super_marian', 'Diablo666', 'wojtek69', '1815', 'A1c', 'Acd46746fhghdgdgdgd' ]
# przy uzyciu filter stworz liste zawierajaca hasla
# ktore zawieraja przynajmniej jedna litere i
# przynajmniej jedna cyfre
# i przynajmniej jedna duza litere
# i sa dluzsze lub rowne 6 znakow


# def filter_passwords(password):
#     if len(password) < 6:
#         return False
#     alpha_found = False
#     digit_found = False
#     upper_found = False
#     for c in password:
#         if c.isalpha():
#             alpha_found = True
#         if c.isdigit():
#             digit_found = True
#         if c.isupper():
#             upper_found = True
#         if alpha_found and digit_found and upper_found:
#             return True
#     return False
#
# print(list(filter(filter_passwords,W)))


# napisz funkcje, ktora pobiera nieznana z gory ilosc argumentow typu string
# i zwraca stringa ktory jest suma wszystkich podanych stringow
# (uzyj *args)

# def sum_all_strings(*strings):
#     pass
#
# sum_all_strings()
# sum_all_strings('o')
# sum_all_strings('a', '2', 'abcdd')


# przy uzyciu TDD - Test Driven Development (najpierw testy, potem funkcja)
# napisz testy do funkcji, ktora pobiera stringa i:
# jesli dlugosc stringa jest z przedzialu <0,3> - zwraca "krotki"
# jesli dlugosc stringa jest z przedzialu <4,10> - zwraca "sredni"
# jesli dlugosc stringa jest z przedzialu <11, do nieskonczonosci> - zwraca "dlugi"
# po napisaniu testow, stworz funkcje, ktora przejdzie wszystkie testy (minimum 3)
# uruchom plik przy uzyciu pytest nazwapliku.py, i sprawdz czy testy przechodza
# otrzymacie 3 lub wiecej faili
# dopiero wtedy napiszcie funkcje taka, ktora przejdzie wszystkie testy


# stworz liste zawierajaca liczby w kolejnosci rosnacej
# sprawdz czy podana liczba (parametr z klawiatury lub zmienna) (input)
# znajduje sie na liscie czy nie, uzywajac dwoch metod:
# 1) uzyj do tego petli for
# 2*) uzyj wyszukiwania binary search (indeks lewy, prawy, srodkowy)


# wiecej zadan jakby ktos mial ochote:
# hackerrank, python
# codility (na dole, lessons for developers)
