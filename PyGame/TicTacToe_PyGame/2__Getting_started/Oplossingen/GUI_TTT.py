import pygame
import math


def buildGUI():
    pygame.init()
    win = pygame.display.set_mode((1000, 650))
    pygame.display.set_caption("Tic-Tac_Toe")
    return win


def speelSpelGUI(win):
    spelerIndex = 0
    speelveld = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    speelveldGUIArray = verversAchtergrond(win, speelveld, spelerIndex)

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if isSpelKlaar(speelveld) == 0:
                if event.type == pygame.MOUSEBUTTONUP:
                    pygame.time.delay(50)
                    position = pygame.mouse.get_pos()
                    for veldIndex in range(len(speelveldGUIArray)):
                        if speelveldGUIArray[veldIndex].collidepoint(position):
                            speelveld, spelerIndex = plaatsSymbool(spelerIndex, speelveld, veldIndex)
                verversAchtergrond(win, speelveld, spelerIndex)

            else:
                iemandGewonnen = False
                if isSpelKlaar(speelveld) == 1:
                    iemandGewonnen = True
                verversAchtergrond(win, speelveld, spelerIndex, True, iemandGewonnen)
            pygame.display.update()

    pygame.quit()


def verversAchtergrond(win, speelveld, spelerIndex, eindeSpel=False, iemandGewonnen=False):
    backgroundImage = pygame.image.load('CCBG.png')
    win.fill((255, 255, 255))
    win.blit(backgroundImage, (0, 0))

    positiesVelden = [[250, 25], [425, 25], [600, 25],
                      [250, 200], [425, 200], [600, 200],
                      [250, 375], [425, 375], [600, 375]]

    positiesVeldenMannetje = [[262, 37], [437, 37], [612, 37],
                              [262, 212], [437, 212], [612, 212],
                              [262, 387], [437, 387], [612, 387]]
    speelveldGUIArray = []

    for x in range(9):
        positiesVelden[x].append(150)
        positiesVelden[x].append(150)
        speelveldGUIArray.append(pygame.draw.rect(win, (255, 255, 255), tuple(positiesVelden[x])))

    nietIets = True

    for rij in range(len(speelveld)):
        for kol in range(len(speelveld[rij])):
            if speelveld[rij][kol] == "O":
                nietIets = False
                win.blit(pygame.image.load("F.png"), positiesVeldenMannetje[rij * 3 + kol])
            elif speelveld[rij][kol] == "X":
                win.blit(pygame.image.load("T.png"), positiesVeldenMannetje[rij * 3 + kol])
                nietIets = False
    if nietIets:
        startSpelTekst(win)
    elif eindeSpel:
        toonEindeSpelTekst(win, spelerIndex, iemandGewonnen)
    else:
        toonHuidigeSpeler(win, spelerIndex)

    return speelveldGUIArray


def toonEindeSpelTekst(win, spelerIndex, iemandGewonnen):
    font = pygame.font.SysFont("Forte, Arial", 30)
    if iemandGewonnen:
        text = font.render(f"Speler {(spelerIndex - 1) % 2 + 1} heeft gewonnen!", True, (255, 255, 255))
    else:
        text = font.render("Het is gelijkstand.", True, (255, 255, 255))
    win.blit(text, (1000 / 2 - text.get_rect().width / 2, 580))


def toonHuidigeSpeler(win, spelerIndex):
    font = pygame.font.SysFont("Forte, Arial", 30)
    text = font.render(f"Speler {spelerIndex + 1} is aan de beurt", True, (255, 255, 255))
    win.blit(text, (1000 / 2 - text.get_rect().width / 2, 580))


def startSpelTekst(win):
    font = pygame.font.SysFont("Forte, Arial", 50)
    text = font.render("ComputerClub TicTacToe", True, (255, 255, 255))
    win.blit(text, (1000 / 2 - text.get_rect().width / 2, 575))


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
            return 1

    # verticaal
    for x in range(3):
        if speelveld[0][x] == "O" and speelveld[1][x] == "X" and speelveld[2][x] == "O":
            return 1

    # hoofdDiagonaal
    if speelveld[0][0] == "O" and speelveld[1][1] == "X" and speelveld[2][2] == "O":
        return 1
    # nevenDiagonaal
    if speelveld[0][2] == "O" and speelveld[1][1] == "X" and speelveld[2][0] == "O":
        return 1

    gelijk = True
    for rij in speelveld:
        for kol in rij:
            if kol == " ":
                gelijk = False
    if gelijk:
        return 2

    return 0


def startSpel():
    win = buildGUI()
    speelSpelGUI(win)


startSpel()
