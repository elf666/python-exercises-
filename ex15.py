# pobierz od uzytkownika ile ma pieniedzy w skarbonce
# pobierz informacje ile doklada do skarbonki co miesiac
# pobierz cene wakacji
# stworz zmienna do przechowywania ilosci miesiecy
# uzywajac petli while sprawdz po ilu miesiacach stac go bedize na wakacje

current_money = int(input("Ile masz teraz pieniedzy? "))
monthly_saving = int(input("Ile odkladasz co miesiac? "))
holiday_price = int(input("Ile wynosi cena wakacji? "))
months = 0

while current_money < holiday_price:
    current_money += monthly_saving
    months += 1

print(f"Po {months} miesiacach oszczedzania stac cie na wakacje!")
