# mozemy w definiciu funkcji wpisywac domyslne wartosci dla argumentow

# def greetings(name, message = "Dzien dobry"):
#     print(f"{message} {name}")
#
# greetings("Marta")
# greetings("Marta", "Siema")
# greetings("Marta", "O nie tylko nie")
# greetings(message="Hej", name="Tomek")
# greetings("Hej","Tomek")

# dowolna ilosc argumentow w funkcji moze byc domyslna
# ale musimy pilnowac zasady: obowiazkowe argumenty po lewej, domyslne poprawej

# def other_greetings(message="Dzien dobry",name, end_sign="."):
#     print(f"{message} {name}{end_sign}")
#
# other_greetings("Zosia")

def other_greetings(name, message="Dzien dobry", end_sign="."):
    print(f"{message} {name}{end_sign}")

other_greetings("Zosia")
other_greetings("Zosia", "Siema", "!!!")
other_greetings(end_sign="!!!", name="Zosia", message="Hej")
other_greetings(D)

# ex29
