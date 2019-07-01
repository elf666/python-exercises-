# dla liczb z zakresu <0 - 15>
# stworz slownik "podzielnosc" wpisujacy wartosci:
# "przez15" - jesli liczba jest podzielna przez 15
# "przez3" - jesli liczba jest podzielna przez 3
# "przez5" - jesli liczba jest podzielna przez 5
podzielnosc = {}

for num in range(16):
    if num % 15 == 0:
        podzielnosc[num] = 'przez15'
    elif num % 5 == 0:
        podzielnosc[num] = 'przez5'
    elif num % 3 == 0:
        podzielnosc[num] = 'przez3'

print(podzielnosc)









# podzielnosc = dict()
#
# for num in range(16):
#     if num % 15 == 0:
#         podzielnosc[num] = 'przez 15'
#     elif num % 5 == 0:
#         podzielnosc[num] = 'przez 5'
#     elif num % 3 == 0:
#         podzielnosc[num] = 'przez 3'
#
# print(podzielnosc)








# for n in range(1,16):
#     if n%3 == 0 and n%5 == 0:
#         podzielnosc[n] = "przez15"
#     elif n%3 == 0:
#         podzielnosc[n] = "przez3"
#     elif n%5 == 0:
#         podzielnosc[n] = "przez5"
#
# print(podzielnosc)
