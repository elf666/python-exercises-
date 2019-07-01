s = "abc123xyz.exe"

# uzywajac slicow wypisz:
print(s[-4:])   # .exe
print(s[6:9])   # xyz
print(s[:9:2])  # znaki od a do z skaczac co 2
print(s[-4])    # wypisz czwarty od konca znak
print(s[2:10])  # wypisz znaki od c do .
print(s[-10:-7])# wypisz 123 uzywajac indeksow ujemnych
print(s[:6])    # od poczatku do 3 nie podajac indekxu 0
print(s[3:])    # od 1 do konca nie podajac indeksu koncowego
print(s[:])     # caly string od poczatku do konca
