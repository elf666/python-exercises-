# zdefiniuj zmienne:
# cena wakacji na karaibach 5000
# cena wakacji w mielnie 2500
# cena wakacji w bieszczadach 1000
# cena wyjscia do kina 30
# pobierz ile uzytkownik ma do wydania
# napisz program korzystając z if, elif, else, ktory
# sprawdzi na jakie wakacje cie stac
# jeśli na żadne, to poinformuj o tym

money_for_holiday = int(input("Ile masz na wakacje? "))
karaiby = 5000
mielno = 2500
bieszczady = 1000
kino = 30

if(money_for_holiday >= karaiby):
    print("Jedziemy na karaiby")
elif(money_for_holiday >= mielno):
    print("Jedziemy do mielna")
elif(money_for_holiday >= bieszczady):
    print("Jedziemy w bieszczady")
elif(money_for_holiday >= kino):
    print("Idziemy do kina!")
else:
    print("Idz do pracy")
