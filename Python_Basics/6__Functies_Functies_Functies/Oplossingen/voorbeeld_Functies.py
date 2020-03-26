def zegEensHallo(aantalKeer):
    for _ in range(aantalKeer):  # _ betekent dat je de variabele niet gebruikt.
        print("Hallo")


def watIsJeNaam():
    print("Wat is je naam")
    return input()  # return geeft een waarde terug waar de functie is opgeroepen


def zegEensHalloMetNaam(naam, aantalKeer):
    for index in range(aantalKeer):
        if index == 0:
            print("Dag", naam)
        else:
            print("Hallo")


zegEensHallo(5)
naam = watIsJeNaam()
zegEensHalloMetNaam(naam, 5)
# zegEensHalloMetNaam(watIsJeNaam(), 5)

