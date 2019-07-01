A = [1,2,3,4,5]
B = [5,6,7,8,9,10]
# sprawdz czy istnieje wspolny element dla obu list

for element_a in A:
    for element_b in B:
        if element_a == element_b:
            print(element_b)

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            print(A[i])
