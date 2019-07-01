# my_dict = {} # inicjalizowanie slownika
# my_dict = dict()

#slownik {klucz:wartosc, inny_klucz:inna_wartosc}
# my_dict['a'] = 'anakonda'
# my_dict['b'] = 'bee'
# my_dict['b'] = 'bear' # mozna nadpisac wartosc pod juz istniejacym kluczem
#
# print(my_dict)

# my_dict = {1: 'apple', 2: 'plum'} # kluczami moga byc int
#
# my_other_dict = {'name': 'John', 'numbers': [2, 4, 3]} # ale nie musza
#
# my_dict = dict([(1,'apple'), (2,'plum')]) # dict(sekwencja danych w parach np tuple)
#
# my_dict = dict([[1,'apple'], [2,'plum']]) # lub zagniezdzona lista
# print(my_dict)
# #
# tworzenie slownika ze zdefiniowanymi kluczami i podanymi (identycznymi) wartosciami
# customer = {}.fromkeys(['id','name', 'surname', 'email'], None)
# print(customer)
# #
# odczyt elementow slownika
# print(my_dict[1]) # aby dostac sie do elementu slownika odwolujemy sie do klucza
# print(my_other_dict['numbers'], my_other_dict['name'])
# #
# # #ex_21
# #
# modyfikacje slownika
# my_dict['nowy_klucz'] = 'nowa_wartosc' # dodanie elementu do slownika
# my_dict['nowy_klucz'] = 'berry' # modyfikowanie wartosci dla danego klucza
# print(my_dict)
# print(my_dict["name"]) # jesli klucz nie istnieje dostajemy KeyError
#
# #
# # ex_22
#
# usuwanie elementow ze slownika

D = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49}
print(D)
# print(D.pop(7)) # usuwa element pod podanym kluczem, zwraca jego wartosc
# print(D)
# usunieta_wartosc = D.pop(5)
# print(usunieta_wartosc)
# print(D)
# # # #
# del D[1] # usuwa klucz i wartosc dla tego klucza
# print(D)
# # #
# print(D.popitem()) # usuwa losowy element , zwraca klucz i wartosc jako tuple
# key, value = D.popitem() # usuniete = D.popitem()
# print(D)
# #
# #
# # sprawdzanie kluczy i wartosci
print(list(D.keys())) # zwraca wszystkie klucze
print(list(D.values())) # zwraca wszystkie wartosci
# #
print(3 in D.keys())    # WAZNE sprawdzenie czy dany klucz istnieje w slowniku
print('a' in D.values()) # sprawdzenie czy dana wartosc istnieje w slowniku
# #
# dict comprehension
N = {x:x+5 for x in range(10)}
print(N)
#
#
S = {key:None for key in ['name', 'surname', 'age']}
print(S)
#
# # for loop
for key in N:  # ale pamietajmy: slownik nie trzyma kolejnosci!
    print(key) # for na slowniku domyslnie wypisze klucze

for key in N:     # petla wypisujaca wartosci slownika
    print(N[key])
# #
for v in N.values():  # petla wypisujaca wartosci slownika
    print(v)
