present = [1, 2, 4, 7, 9, 11, 14, 17, 20] # w klasie jest 20 uczniow

# dzien wagarowicza
# w klasie mamy 20 uczniow ale przyszli tylko ci, ktorych numery z dziennika
# sa na podanej liscie
# Stworz slownik zawierajacy informacje o KAZDYM uczniu <1 - 20> z adnotacja
# "obecny" albo "nieobecny"
obecnosc = {}

for num in range(1,21):
    if num in present:
        obecnosc[num] = 'obecny'
    else:
        obecnosc[num] = 'nieobecny'
print(obecnosc)


P = {num:'obecny' if num in present else 'nieobecny' for num in range(1,21)}
print(P)






# R = dict() # R = {}
# for student in range(1,21):
#     if student in present:
#         R[student] = 'obecny'
#     else:
#         R[student] = 'nieobecny'
# print(R)
#
# # dict comprehension
# R = {s:'obecny' if s in present else 'nieobecny' for s in range(1,21)}
# print(R)
#
#
#
#
#
#
#
# # students = {}
# # for n in range(1,21):
# #     if n in L:
# #         students[n] = "obecny"
# #     else:
# #         students[n] = "nieobecny"
# # print(students)
# #
# #
# # students = {n:"obecny" if n in L else "nieobecny" for n in range(1,21)}
# # print(students)
