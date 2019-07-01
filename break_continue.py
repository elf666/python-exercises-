A = [1,5,3,4,5,6,7,8,9,1]

# sprawdz czy na liscie jest chociaz jedna 5, jesli tak to wyjdz z petli

for element in A:
    if element == 5:
        print("Znalazlem 5!")
        break
print("Koniec")

# jesli znajdziesz nieparzysta to sprawdz czy jest podzielna przez 5 i wypisz jesli takie

for element in A:
    if element % 2 == 0: # jesli jest parzysta
        continue
    print("Nieparzysta!")
    if element % 5 == 0:
        print("I do tego podzielna przez 5")
