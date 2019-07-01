# napisz funkcje, ktora sprawdza czy podany string jest palindromem
# palindrom - slowo, ktore czytane od przodu i od tylu brzmi tak samo
# 'kajak' - palindrom
# 'ala' - palindrom
# 'python' - nie palindrom

def check_if_palindrome(word):
    return word == word[::-1]


def check_if_palindrome(s):
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            print("Not palindrome!")
            break
        left += 1
        right -= 1
    else:
        print("Is palindrome!")


print(check_if_palindrome('ala'))
print(check_if_palindrome('kajak'))
print(check_if_palindrome('python'))

















# def check_if_palindrome(s):
#     left = 0
#     right = len(s) -1
#     while left <= right:
#         if s[left] != s[right]:
#             print("Not palindrome!")
#             break
#         left += 1
#         right -= 1
#     else:
#         print("Is palindrome!")
#
# check_if_palindrome("kajak")
# check_if_palindrome("anakonda")
