# stworz zmienna globalna pi = 3.14
# napisz funkcje ktora pobiera promien okregu i oblicza jego pole
# korzystajac ze wzoru: pole = pi * r**2

# napisz funkcje ktora pobiera promien okregu i oblicza jego obwod
# korzystajac ze wzoru: obwod = 2 * pi * r

# oblicz pole i obwod dla kol o promieniu r=3 i r=5
pi = 3.14

def pole_kola(r):
    return pi * r**2

def obwod_kola(r):
    return 2 * pi * r

print(pole_kola(2))
print(pole_kola(5))
print(pole_kola(10))
print(obwod_kola(2))
print(obwod_kola(3))
print(obwod_kola(5))

# pi = 3.14

# def area_of_circle(r):
#     return pi * r**2
#
# def circumference_of_cicle(r):
#     return 2 * pi * r
#
# print(f"dla kola o r=3 pole wynosi: {area_of_circle(3)} a obwod: {circumference_of_cicle(3)}")
# print(f"dla kola o r=5 pole wynosi: {area_of_circle(5)} a obwod: {circumference_of_cicle(5)}")

print(1.2 - 1.0) # pythonowe floaty nie sa najlepsze...
