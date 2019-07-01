# korzystajac z petli while sprawdz czy podany element znajduje sie na liscie
# jesli tak to wypisz informacje ze jest i pod jakim indeksem

#    0    1  2  3  4  5  6   7
Z = [-3, -1, 0, 2, 4, 8, 33, 150]
target = -3

left_idx = 0
right_idx = len(Z) - 1
while left_idx <= right_idx:
    mid_idx = (left_idx + right_idx) // 2
    print(f"left: {left_idx}, right: {right_idx}, mid: {mid_idx}")
    if Z[mid_idx] == target:
        print(f"Liczba {target} znajduje sie pod indeksem {mid_idx}")
        break
    elif Z[mid_idx] < target:
        left_idx = mid_idx + 1
    else: # skoro Z[mid_inx] nie jest rowna ani mniejsza, to jest wieksza od target
        right_idx = mid_idx - 1
else:
    print(f"Nie znaleziono liczby {target}")








# S = [-3, -1, 0, 5, 8, 9, 11, 23, 45, 398, 1000] # posortowana lista
#
# left = 0
# right = len(S) -1
# target = 398
#
# while left <= right:
#     av = (left + right) // 2 # chcemy integer!
#     print(f"left: {left}, right: {right}, av: {av}")
#     if S[av] == target:
#         print(f"Znalazlem! Liczba {target} znajduje sie pod indeksem {av}")
#         break
#     elif S[av] > target:
#         right = av - 1
#     else:
#         left = av + 1
# else:
#     print(f"Liczby {target} nie ma na liscie.")
