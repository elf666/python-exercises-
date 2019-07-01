# pobierz z klawiatury ile masz ciasteczek
# dopoki ciasteczka sie nie skoncza wypisuj: "zjadlem jedno ciasteczko", i ile zostalo
# jak sie skoncza wypisz "skonczyly sie"

num_of_cookies = int(input("Podaj ile masz ciasteczek "))

while num_of_cookies > 0:
    num_of_cookies -= 1
    print(f"Zjadlem ciasteczko. Zostalo jeszcze {num_of_cookies}")
print("Wszystkie zjedzone :(")
