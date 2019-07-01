A = [1,2,3,4,5]
B = ['a', 'b', 'c']

A.append(100) # dodaj element na koncu listy
del A[5] # usun element spod podanego indeksu
del A[1]
A.remove(4) # znajdz i usun element z listy
T = [1,2,1]
T.remove(1) # jesli elementow jet wiecej to usuwa pierwszy z lewej
T.insert(1, 'abc') # wsadz na podany indeks podana wartosc
A.extend(B) # doklej liste B na koncu listy A
A.append(B) # append uzyte na liscie tworzy liste zagniezdzona

S = ['a', 'b', 'a', 'c', 'a']
# print(S.count('a')) # zlicza wystapienia zmiennej na liscie
# print(S.index('c')) # sprawdza na jakim indeksie jest podana wartosc

D = [1,2,3,4,5]
D.reverse() # odwroc liste
E = [5,6,4,3,4,7,8,1]
E.sort() # sort

S = []
S.append("Gra o Tron")
S.append("Wiedzmin")
S.append("Muminki")

print(S.pop()) # sciaga ostatni element z listy, lista sie skraca
print(S.pop())
print(S.pop())
