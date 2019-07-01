N = [-1, 2, -3, -4, 5, 6, -8, -11]

# uzywajac list comprehension stworz liste
# w ktorej wszystkie wartosci z listy N sa dodatnie

W = [num * (-1) if num < 0 else num for num in N]
W = [-num if num < 0 else num for num in N]
W = [num if num >= 0 else -num for num in N]
print(W)












# G = [num if num >= 0 else -num for num in N]
# print(G)






# G = [n if n >=0 else n * -1 for n in N]
# print(G)
