# pobierz od użytkownika info ile ma w skarbonce
# pobierz od użytkownika info ile planuje zarobić
# pobierz od użytkownika info ile kosztują wakacje
# sprawdź czy posiadana suma przewyższy lub wyrowna koszt wakacji
# jesli tak to wydrukuj True

money_had = int(input("Ile masz w skarbonce? "))
money_planned = int(input("Ile planujesz zarobić? "))
holiday_cost = int(input("Ile potrzebujesz na wakacje? "))

print(money_had + money_planned >= holiday_cost)
