D = [1, 1, 3, 4, 5, 4, 2, 3, 4, 5]

# stworz pusta liste pomocnicza
# przejrzyj liste D i dodaj jej elementy do listy pomocniczej, ale tylko jeden raz
# dla kazdej wartosci
# print(1 in D) # sprawdz czy element jest w liscie
# print(1 not in D) # sprawdz czy elementu nie ma w liscie
# wydrukuj liste unikalnych wartosci

# Rozwiazanie z not if

# P = []
# for number in D:
#     if number not in P:
#         P.append(number)
# print(P)

# Rozwiazanie z in

# P = []
# for number in D:
#     if (number in P) is False:
#         P.append(number)
# print(P)

# Rozwiazanie z set()

print(set(D)) # stworz set z listy (to jet rzutowanie)
