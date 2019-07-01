# lista = [wyrazenie for element in list] (lub range)

# A = [1, 2, 3, 4, 5, 6, 7]
# L = [x**2 for x in A]
# print(L)

#mozna tez bezposrednio uzyc range zamiast podawania listy
# K = [x**2 for x in range(1,11)]
# print(K)

# uzycie ifow: lista = [wyrazenie for element in list if element spelnia warunki]

# N = [x for x in range(50) if x % 5 == 0]
# print(N)
# #
# D = [s for s in "ab1d3c5d5t6y7" if s.isdigit()]
# print(D)
#
# # podwojny if - BEZ AND!
#
# P = [num for num in range(50) if num%2 == 0 if num%3 == 0 if num%5 == 0]
# print(P)
# #
# # if else
#
L = ["Even" if x%2 == 0 else "Odd" for x in range(1000) if x%2 == 0 if x%3 == 0 if x%5 == 0]
print(L)
