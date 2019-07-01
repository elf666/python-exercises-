# # funkcja jest obiektem
# # da sie wywolywac na niej metody
# # da sie ja przekazac jako argument dla innej funkcji
#
def fun1():
    '''Jestem funkcja 1'''

def fun2():
    '''Jestem funkcja 2'''
#
# print(fun1.__doc__)
# print(fun1)
# print(fun1.__code__)
# print(fun1.__sizeof__)
# print(dir(fun1))

def print_fun_doc(fun):
    print(fun.__doc__)

print_fun_doc(fun1)
print_fun_doc(fun2)
