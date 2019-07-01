A = [2,5,7,9,11,13]
# pobierz z klawiatury mnoznik (int)
# przemnoz kazdy element z listy o podany mnoznik i wydrukuj go
mnoznik = int(input("Podaj mnoznik: "))

for element in A:
    print(element * mnoznik)

for i in range(len(A)):
    print(A[i] * mnoznik)
