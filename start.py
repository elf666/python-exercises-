print("Hello World!") # print - drukuje podane dane
print('Druga')  # pojedynczy cudzyslow jest akceptowany
print(5) # wydrukuj integer (liczba całkowita)
print(3.14) # wydrukuj float (liczba zmiennoprzecinkowa)
print(True) # wydrukuj boolean (bool) zmienna logiczna
print(False)

name = "Marta"
surname = "P."
age = 30

print("Mam na imie " + name + " " + surname + " " + "i mam " + str(age) + " lat")
print("Mam na imie", name, surname, "i mam", age, "lat")
print("Mam na imie {A} {B} i mam {C} lat".format(B=surname, A=name, C=age))
print(f"Mam na imie {name} {surname} i mam {age} lat")
