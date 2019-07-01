# napisz funkcje ktora pobiera dowolna liczbe i zwraca jej wartoc bezwzgledna
# (eng. absolute value)
# czyli: pobieramy jeden parametr
#        zwracamy (return) jeden parametr
# przetestuj dla kilku liczb dodatnich i ujemnych
# nie uzywaj printa w funkcji!

def return_absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number

print(return_absolute_value(5))
print(return_absolute_value(-10))
print(return_absolute_value(-3.14))
print(return_absolute_value(0))

# absolute = return_absolute_value(5)
#
# print(absolute)









# def return_absolute_value(number):
#     if number >= 0:
#         return number
#     else:
#         return -number
#
# print(return_absolute_value(5))
# print(return_absolute_value(-10))
# print(return_absolute_value(0))
# print(return_absolute_value(3.14))
# print(return_absolute_value(-2.64))
#
#
#
#
#
#
#
#
#
#
#
# # def create_absolute_value_of_number(n):
# #     if n >=0:
# #         return n
# #     else:
# #         return -n
# #
# # print(create_absolute_value_of_number(5))
# # print(create_absolute_value_of_number(-5))
# # print(create_absolute_value_of_number(0))
# # print(create_absolute_value_of_number(-10.5))
