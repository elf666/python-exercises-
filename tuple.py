T = (1, 'a', True, [1, (22,33)])
U = ('xyz', 789)
print(T[-1][1][0])

# T.append(5) # nie wolno
# T[0] = 100 # nie wolno

Z = T + U # dodawanie dwoch tupli do siebie

klient = (765432, "Jan", "Kowalski", 'jan@o2.pl', 35)

id = klient[0]
name = klient[1]

id, name, surname, email, age = klient # tuple unpack - rozpakowywanie

print(id, name, surname, email, age)
