L  = ['abc', '13', 'xyz', 'z', '1', 'aba', 'aa', '1221', 'kajak']

# znajdz elementy listy ktore sa dluzsze lub rowne  2
# ORAZ
# ich pierwszy i ostatni znak sa takie same
# indeksy elementow spelniajacych kryteria dodaj do listy pomocniczej
# wydrukuj liste pomocnicza

P = []
for i in range(len(L)):
    if len(L[i]) >= 2 and L[i][0] == L[i][-1]:
        P.append(i)
print(P)
