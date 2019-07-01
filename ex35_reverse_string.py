# napisz program, ktory bedize odwracal podany string
# np 'osa' na 'aso'

def reverse(string):
    idx = len(string) - 1
    new_str = ''
    while idx >= 0:
        new_str += string[idx] # new_str = new_str + string[idx]
        idx -= 1
    return new_str

print(reverse("ABCDE"))














# def reverse_string(s):
#     new_str = ''
#     right_idx = len(s)-1
#
#     while right_idx >=0:
#         new_str += s[right_idx]
#         right_idx -=1
#     return new_str
#
# print(reverse_string("osa"))
# print(reverse_string("anakonda"))
# print(reverse_string("kajak"))


# a tak mozna szybciej ;)

# def reverse_string(s):
#     return s[::-1]
