# uzywajac list comprehension i range
# stworz liste zawierajaca co druga liczbe z zakresu <0 do 20>
# podniesiona o 5

L = [x + 5 for x in range(0,21) if x%2 == 0]
L = [x + 5 for x in range(0,21,2)]
print(L)











# R = [num + 5 for num in range(0,21,2)]
# print(R)
