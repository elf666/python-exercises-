A = ['a', 'A']
B = ['b', 'B']

# wypisz wszystkie kombinacje elementow powyzszych list
# czyli: ab, aB, Ab, AB

for a in A:
    for b in B:
        print(a+b)


X = [1,2,3]
Y = [3,4,5]
Z = [6,7,8]
for x in X:
    for y in Y:
        for z in Z:
            print(str(x)+str(y)+str(z))
