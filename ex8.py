B = [-1, 1, 4, -5, 6, -6, 10, -11]
# osobne petle, # jedna petla

# stworz zmienna do przechowywania sumy
# oblicz sume wszystkich dodatnich elementow listy
# wypisz wynik
# s = 0
# for number in B:
#     if number > 0:
#         s += number # s = s + number
# print(f"Suma dodatnich wynosi {s}")
#
# s = 0 # zerujemy sume do uzycia w drugiej petli
# for number in B:
#     if number%2 == 1:
#         s += number
# print(f"Suma nieparzystych wynosi {s}")

# stworz nowa zmienna albo wyzeruj poprzednia
# oblicz sume wszystkich nieparzystych elementow listy
# wypisz wynik


# for i in range(len(B)): # alternatywne rozwiazanie na indeksach
#     if B[i] > 0:
#         s += 0


# Znajdz obie sumy w jednej petli
# s_gt_zero = 0
# s_odd = 0
#
# for element in B:
#     if element > 0:
#         s_gt_zero += element
#     if element%2 == 1:
#         s_odd += element
# print(f"Suma wiekszych od zera to {s_gt_zero} a suma nieparzystych to {s_odd}")

# utrudnienie: dodaj znalezione elementy do listy pomocniczej

# gt_zero = []
# odds = []
#
# for element in B:
#     if element > 0:
#         gt_zero.append(element)
#     if element%2 == 1:
#         odds.append(element)
#
# print(f"Lista wiekszych od zera {gt_zero}, suma: {sum(gt_zero)}")
# print(f"Lista nieparzystych {odds}, suma: {sum(odds)}")
