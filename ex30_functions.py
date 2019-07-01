# stworz funkcje pobierająca nieznana z gory ilosc liczb
# ktora zsumuje wszystkie pobrane liczby i zwroci wynik


def zsumuj(*liczby):
    # suma = 0
    # for liczba in liczby:
    #     suma = suma + liczba # suma += liczba -> suma = suma + liczba
    # return suma
    return sum(liczby)


print(zsumuj())
print(zsumuj(1,2))
print(zsumuj(1,25,4,36,7,8))










# def add(*nums):
#     num_sum = 0
#
#     for num in nums:
#         num_sum += num
#
#     return num_sum
#
# print(add())
# print(add(1))
# print(add(1,2,3))
# print(add(1, 2.2, 3.3, 4.4, 5))
