A = [1, 2, 3]
B = [1, 3.14, 'ab', True, ['c', 'd']] # lista moze przechowywac rozne typy danych
                                      # w tym inne listy
# print(A[1]) # odwolywanie sie do elementu listy
# print(A[1:]) # mozna uzywac slicow aby uzyskac fragment listy

M = [[1, 3, 4], [5, 6, 3], [2, 4, 6]] # lista dwuwymiarowa (macierz dwuwymiarowa 3x3)

A[0] = 10
# B[2][0] = 'A' # tak sie nie da

N = A # tak sie nie tworzy kopii lity, to jest druga zmienna wskazujaca na te sama liste
M = A[:] # tak sie tworzy KOPIE listy A.
print(A, M)
M[0] = 'abc'
print(A, M)
