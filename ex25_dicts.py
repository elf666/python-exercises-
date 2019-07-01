suspect = {'name':'Anna', 'surname':'Nowak', 'occupation':'actress'}
police_docs = ['name', 'surname', 'age', 'occupation', 'friends']

# suspect - slownik informacji o podejrzanej o morderstwo
# police_docs - informacje jakie chcialaby zdobyc policja
# sprawdz czy poszukiwane przez policje dane sa w slowniku
# jesli tam sie znajduja to je wypisz
# jesli nie - napisz, "brak danych"

for data in police_docs:
    if data in suspect.keys(): # if data in suspect:
        print(f"{data} -> {suspect[data]}")
    else:
        print(f"{data} -> brak_danych")








# for item in police_docs:
#     if item in suspect.keys(): # if item in suspect:
#         print(f"{item} -> {suspect[item]}")
#     else:
#         print(f"{item} -> brak danych")








# for item in police_docs:
#     if item in suspect.keys():
#         print(f"{item} -> {suspect[item]}")
#     else:
#         print(f"{item} -> brak danych")
