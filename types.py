import math  # import ZAWSZE na poczatku pliku
# typy podstawowe: str, int, float, boolean

name = "M"
number1 = 5
number2 = 3.14
pi_as_int = int(number2)
is_true = False

print(5 + 10) # result: 15
print(5.0 + 10) # result: 15.0
print(8 / 2)    # result: 4.0
print(5 / 2)    # result: 2.5
print(round(5 / 2)) # round - zaokrąglenie matematyczne (0.5 w dół, 0.51 w gorę)
print(round(3.1415345678, 4)) # zaokrąglenie do podanego miejsca po przecinku
print(7 // 4) # floor division - zostawia tylko czesc calkowita
print(7 % 4)  # modulo division - zostawia tylko resztę z dzielenia

print(5 * 3.0) # mnożenie, result: 15
print(2 ** 3)  # potęgowanie
print(math.sqrt(49)) # wynik pierwiastkowania jest floatem



# print(int(3.14)) # rzutowanie float na int
# print(float(5))  # rzutowanie int na float
# print(int(True))  # rzutowanie bool na int
# print(int(False)) # rzutowanie bool na int
# print(str(5))     # rzutowanie int na stringa
# print(int('10'))  # rzutowanie str na inta

# print(type(name))
# print(type(number1))
# print(type(number2))
# print(type(is_true))
