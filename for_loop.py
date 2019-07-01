X = [1,2,3]

for element in X:   # ten zapis zwraca kolejne ELEMENTY listy
    print(element)

for i in range(len(X)):  # ten zapis działa na indeksach
    print(X[i])


print(list(range(5))) # wypisze [0,1,2,3,4]
print(list(range(2,5))) # wypisze [2,3,4]
print(list(range(len(X)))) # wypisze indeksy dla listy X
