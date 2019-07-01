s = "abcdefg.txt" # efg
print(s * 3) # mnozenie stringow

print(s[4:7]) # pierwszy element przedzialu jest drukowany, ostatni jest pierwszym
              # niedrukowanym
print(s[0:3]) # abc
print(s[:3])  # jesli zaczynamy od 0 to mozemy go nie pisac
print(s[8:11]) #.txt
print(s[8:])
print(s[:])  # od poczatku do konca
print(s[1:7:2]) # start:stop+1:skok
print(s[-4:])   # tak sie sprawdza rozszerzenia plikow nieznanej dlugosci

s = "abcdefg.txt"
# s[0] = 'A' # nie dziala, nie wolno modyfikowac stringow

print(s.capitalize()) # zmien pierwsza litere na duza
print(s.upper()) # zmien wszystkie litery na duze
print('ABC'.lower()) # zmien wszystkie litery na male
print('gra o tron'.title())
print("abcdefg.txt".replace('txt', 'xyz')) # zamien podciag na inny
print("   aa  a   ".strip()) #lstrip(), rstrip()
print("gra o tron".split()) # dzieli po spacjach, tworzy liste
print("1,3,5,22".split(',')) # dzieli po podanym stringu
print("1\t2\t3".split('\t'))
seq = ("podstrona", "/index")
print("/adres_strony".join(seq))
print("abc.txt".index(".txt"))
print('123'.isdigit()) # sprawdza czy string mozna rzutowac na int
print("ABC".isupper()) # sprawdza czy same duze litery
print("xyz".islower()) # sprawdza czy same male litery
