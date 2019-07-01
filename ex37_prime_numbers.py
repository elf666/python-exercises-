# sprawdz czy podana liczba jest liczba pierwsza

def check_if_prime(number):
    if number == 1:
        return False
    for d in range(2, number):
        if number % d == 0:
            return False
    return True


print(check_if_prime(1))
print(check_if_prime(4))
print(check_if_prime(5))
print(check_if_prime(9))
print(check_if_prime(101))












#
#
# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True;
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True
# print(test_prime(9))
