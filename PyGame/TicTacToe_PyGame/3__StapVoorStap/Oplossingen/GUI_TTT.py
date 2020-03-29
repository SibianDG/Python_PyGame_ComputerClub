import pygame
import math  # om meer wiskunde functies te hebben


def buildGUI():
    pygame.init()  # start pygame
    win = pygame.display.set_mode((1000, 550))  # afmetingen
    pygame.display.set_caption("Tic-Tac-Toe")
    return win  # dit hebben we later nog nodig


def speelSpelGUI(win):
    spelerIndex = 0
    speelveld = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    speelveldGUIArray = verversAchtergrond(win, speelveld, spelerIndex)  # een array met daarin alle 9 de
    # vierkanten/velden.

    run = True
    while run:  # pygame basic

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if not isSpelKlaar(speelveld):
                if event.type == pygame.MOUSEBUTTONUP:  # als je geklikt HEBT
                    position = pygame.mouse.get_pos()  # krijg positie van de muis.
                    for veldIndex in range(len(speelveldGUIArray)):  # over elk vierkant lopen
                        if speelveldGUIArray[veldIndex].collidepoint(
                                position):  # en controleren of het daarop geklikt is
                            speelveld, spelerIndex = plaatsSymbool(spelerIndex, speelveld,
                                                                   veldIndex)  # krijgt 2 waarden terug
                verversAchtergrond(win, speelveld, spelerIndex)  # achtergrond vernieuwen.
            pygame.display.update()  # achtergrond updaten.

    pygame.quit()


def verversAchtergrond(win, speelveld, spelerIndex, eindeSpel=False, iemandGewonnen=False):
    win.fill((255, 255, 255))  # mocht de afbeelding te klein zijn, wordt het daarachter wit
    backgroundImage = pygame.image.load('CCBG.png')  # afbeelding laden
    win.blit(backgroundImage, (0, 0))  # afbeelding instellen

    positiesVelden = [[250, 25], [425, 25], [600, 25],
                      [250, 200], [425, 200], [600, 200],
                      [250, 375], [425, 375], [600, 375]]  # array met de x, y begin plaats voor de vierkanten/velden
    # => minder schrijven later

    positiesVeldenMannetje = [[262, 37], [437, 37], [612, 37],
                              [262, 212], [437, 212], [612, 212],
                              [262, 387], [437, 387], [612, 387]]  # array met de x, y begin plaats voor de
    # zetten/foto's => minder schrijven later
    speelveldGUIArray = []  # een array met daarin alle 9 de  vierkanten/velden.

    for x in range(9):
        positiesVelden[x].append(150)  # breedte toevoegen aan het vierkant/veld
        positiesVelden[x].append(150)  # hoogte toevoegen aan het vierkant/veld
        speelveldGUIArray.append(pygame.draw.rect(win, (255, 255, 255), tuple(
            positiesVelden[x])))  # rechthoek tekenen én bijhouden in array. We hebben ze later nog nodig.

    for rij in range(len(speelveld)):
        for kol in range(len(speelveld[rij])):
            if speelveld[rij][kol] == "O":  # kijken naar speelveld: als het O is dan:
                win.blit(pygame.image.load("F.png"), positiesVeldenMannetje[rij * 3 + kol])  # afbeelding voor O
                # toevoegen. Formule om van 2-dimensionale array naar een 1 dmiensionale te gaan. 3 = lengte van rij.
            elif speelveld[rij][kol] == "X":
                win.blit(pygame.image.load("T.png"), positiesVeldenMannetje[rij * 3 + kol])

    return speelveldGUIArray  # terug geven


def plaatsSymbool(spelerIndex, speelveld, veldIndex):
    plaats = int(veldIndex)
    if speelveld[math.floor(plaats / 3)][plaats % 3] == " ":
        if spelerIndex == 0:
            speelveld[math.floor(plaats / 3)][plaats % 3] = "O"
        else:
            speelveld[math.floor(plaats / 3)][plaats % 3] = "X"
        spelerIndex = veranderSpeler(spelerIndex)
    return speelveld, spelerIndex


def veranderSpeler(spelerIndex):
    return (spelerIndex + 1) % 2


def isSpelKlaar(speelveld):
    # horizontaal
    for rij in speelveld:
        if rij[0] == "O" and rij[1] == "X" and rij[2] == "O":
            return True

    # verticaal
    for x in range(3):
        if speelveld[0][x] == "O" and speelveld[1][x] == "X" and speelveld[2][x] == "O":
            return True
    # hoofdDiagonaal
    if speelveld[0][0] == "O" and speelveld[1][1] == "X" and speelveld[2][2] == "O":
        return True
    # nevenDiagonaal
    if speelveld[0][2] == "O" and speelveld[1][1] == "X" and speelveld[2][0] == "O":
        return True

    # gelijk stand
    gelijk = True
    for rij in speelveld:
        for kol in rij:
            if kol == " ":
                gelijk = False
    if gelijk:
        return True

    return False


speelSpelGUI(buildGUI())

