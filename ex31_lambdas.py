# uzywajac lambdy i funkcji filter
# stworz liste wszystkich wielkich liter, jakie znajduja sie w podanym stringu

s = 'Wszyscy Ogladaja Gre O Tron'

#S = ['W', 'O', 'G', 'O', 'T']

def check_if_upper(letter):
    return letter.isupper()

L = list(filter(lambda letter:letter.isupper(),s))
K = list(filter(check_if_upper,s))
print(L)
print(K)















# S = list(filter(lambda letter: letter.isupper(), s))
# print(S)
