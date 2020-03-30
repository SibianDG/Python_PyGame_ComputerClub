from random import randint

# blad steen schaar
speler_naam = input("Wat is je naam?   ").title()

print(f"Hallo {speler_naam}, laten we een spelletje blad steen schaar spelen \n Succes!")
# input van de speler, omzetten lowercase voor vergelijken

while True:

    speler_keuze = input("Maak een keuze: Blad / Steen / Schaar   ").lower()
    print(f"{speler_naam}, Je hebt gekozen voor {speler_keuze}")
    # lijst aanmaken voor keuzes, computer random waarde toekennen
    keuzes = ["blad", "steen", "schaar"]
    computer_keuze = keuzes[randint(0, 2)]
    print(f"De computer heeft gekozen voor {computer_keuze}")

    # spel door laten spelen

    if speler_keuze == computer_keuze:
        print("Gelijke stand")
    elif speler_keuze == keuzes[0]:
        if computer_keuze == keuzes[2]:
            print(f"{speler_naam}, Je hebt verloreren {keuzes[2]} wint van {keuzes[0]} ")
        else:
            print(f"{speler_naam}, Je hebt gewonnen {keuzes[0]} wint van {keuzes[1]} ")

    elif speler_keuze == keuzes[1]:
        if computer_keuze == keuzes[0]:
            print(f"{speler_naam}, Je hebt verloreren {keuzes[0]} wint van {keuzes[1]} ")
        else:
            print(f"{speler_naam}, Je hebt gewonnen {keuzes[1]} wint van {keuzes[2]} ")

    elif speler_keuze == keuzes[2]:
        if computer_keuze == keuzes[1]:
            print(f"{speler_naam}, Je hebt verloreren {keuzes[1]} wint van {keuzes[2]} ")
        else:
            print(f"{speler_naam}, Je hebt gewonnen {keuzes[2]} wint van {keuzes[0]} ")

    antwoord = input("Wil je nog een spel spelen? (Y/N)").lower()

    if antwoord == "n":
        break

# we print thanks for playing 
print("\nThanks for playing")
