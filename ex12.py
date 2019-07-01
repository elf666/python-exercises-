# usun z listy U wartosci spod indeksow: drugiego, trzeciego i piatego
# mozna uzyc listy pomocniczej
# wydrukuj liste U

U = [3,5,7,3,4,55,6]
to_be_deleted = []

to_be_deleted.append(U[2])
to_be_deleted.append(U[3])
to_be_deleted.append(U[5])

for element in to_be_deleted:
    U.remove(element)

print(U)
