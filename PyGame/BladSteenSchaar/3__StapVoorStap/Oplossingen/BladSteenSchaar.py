import pygame
import random
import os


def buildGUI():
    pygame.init()  # start pygame
    win = pygame.display.set_mode((600, 600))  # afmetingen
    pygame.display.set_caption("Blad Steen Schaar")  # titel window
    return win  # dit hebben we later nog nodig


def draw(win, resultaat):
    win.fill((255, 255, 255))  # achtergrond wit
    fontTitle = pygame.font.SysFont("Calibri, Arial", 30)  # font voor titel
    text = fontTitle.render("Kies uit blad, steen of schaar", True, (0, 0, 0))  # render de zin
    win.blit(text, (125, 0))  # toon op scherm

    keuzeFoto = [win.blit(pygame.image.load('blad.png'), (25, 50)), win.blit(pygame.image.load('steen.png'), (225, 50)),
                 # toon op scherm blit(iets). Wat tonen? iets -> image
                 win.blit(pygame.image.load(os.getcwd()+'\schaar.png'), (400, 50))]

    gewonnen = resultaat[1]  # gewonnen, verloren, gelijk of nog beginnen
    keuzeComputer = resultaat[0]  # keuze computer
    if gewonnen == 3:  # als spel moet beginnen
        zin = "Speel een spel"
    else:  # als er al gespeeld is
        zin = f"Computer koos {keuzeComputer}. "
        if gewonnen == 0:
            zin += "Computer heeft gewonnen"
        if gewonnen == 1:
            zin += "U heeft gewonnen"
        if gewonnen == 2:
            zin += "Gelijkstand."

    fontOnderaan = pygame.font.SysFont("Calibri, Arial", 20)  # font voor van onder. Kleiner
    resultaatText = fontOnderaan.render(zin, True, (0, 0, 0))  # render de zin
    win.blit(resultaatText, (100, 500))  # toon op scherm
    return keuzeFoto


def speelSpel(win):
    print(os.getcwd())
    resultaat = ["", 3]  # om te beginnen
    run = True
    while run:  # pygame basic
        keuzeFoto = draw(win, resultaat)  # window meegeven en wie er gewonnen heeft en wat de computer gekozen heeft.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:  # als er op muis geklikt is
                position = pygame.mouse.get_pos()  # geef positie muis
                for index in range(len(keuzeFoto)):  # blad, steen, schaar na
                    if keuzeFoto[index].collidepoint(position):  # ofdat de muis op een van de 3 geklikt heeft
                        resultaat = bewerkingen(index)  # berekening doen met de index.

        pygame.display.update()  # achtergrond updaten.

    pygame.quit()  # na while, dus na op kruisje geklikt te hebben, stopt het.


def bewerkingen(keuzeGetal):
    keuzes = ["blad", "steen", "schaar"]
    resultaat = []  # array om computerKeuze en Gewonnen in te steken

    keuze = keuzes[keuzeGetal]  # keuzeGetal is de index in de array. 0: blad, 1: steen, 2: schaar
    computerKeuze = keuzes[random.randint(0, 2)]  # random 0, 1 of 2
    resultaat.append(computerKeuze)  # keuze computer aan resultaat toevoegen.
    if keuze == computerKeuze:
        resultaat.append(2)
    elif keuze == "blad":
        if computerKeuze == "steen":
            resultaat.append(1)
        else:
            resultaat.append(0)
    elif keuze == "steen":
        if computerKeuze == "blad":
            resultaat.append(1)
        else:
            resultaat.append(0)
    elif keuze == "schaar":
        if computerKeuze == "blad":
            resultaat.append(1)
        else:
            resultaat.append(0)
    return resultaat


speelSpel(buildGUI())
