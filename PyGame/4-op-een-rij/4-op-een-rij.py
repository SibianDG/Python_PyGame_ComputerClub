import pygame
import math

# kleuren in vars steken
BLAUW = (0, 0, 255)
ZWART = (0, 0, 0)
ROOD = (255, 0, 0)
GEEL = (255, 255, 0)

AANTAL_RIJEN = 6
AANTAL_KOLOMEN = 7


def maakBord():
    bord = []
    for x in range(AANTAL_RIJEN):
        bord.append([])
        for y in range(AANTAL_KOLOMEN):
            bord[x].append(0)
    return bord


def plaatsStuk(bord, rij, kol, stuk):
    # de referentie is genoeg. Je moet het niet terug geven
    bord[rij][kol] = stuk


def controleerPlaatsLeeg(bord, kol):
    # zolang dat op de bovenste lijn een 0 is, is er iets vrij.
    return bord[AANTAL_RIJEN - 1][kol] == 0


def geefVolgendeVrijeRij(bord, col):
    for r in range(AANTAL_RIJEN):
        if bord[r][col] == 0:
            return r


def isGewonnen(bord, stuk):
    # horizontaal
    for c in range(AANTAL_KOLOMEN - 3):
        for r in range(AANTAL_RIJEN):
            if bord[r][c] == stuk and bord[r][c + 1] == stuk and bord[r][c + 2] == stuk and bord[r][c + 3] == stuk:
                return True

    # verticaal
    for c in range(AANTAL_KOLOMEN):
        for r in range(AANTAL_RIJEN - 3):
            if bord[r][c] == stuk and bord[r + 1][c] == stuk and bord[r + 2][c] == stuk and bord[r + 3][c] == stuk:
                return True

    # Hoofdiagonaal
    for c in range(AANTAL_KOLOMEN - 3):
        for r in range(AANTAL_RIJEN - 3):
            if bord[r][c] == stuk and bord[r + 1][c + 1] == stuk and bord[r + 2][c + 2] == stuk and bord[r + 3][
                c + 3] == stuk:
                return True

    # nevendiagonaal
    for c in range(AANTAL_KOLOMEN - 3):
        for r in range(3, AANTAL_RIJEN):
            if bord[r][c] == stuk and bord[r - 1][c + 1] == stuk and bord[r - 2][c + 2] == stuk and bord[r - 3][
                c + 3] == stuk:
                return True


def tekenBord(bord):
    for c in range(AANTAL_KOLOMEN):
        for r in range(AANTAL_RIJEN):
            pygame.draw.rect(scherm, BLAUW, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(scherm, ZWART, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), STRAAL)

    for c in range(AANTAL_KOLOMEN):
        for r in range(AANTAL_RIJEN):
            if bord[r][c] == 1:
                pygame.draw.circle(scherm, ROOD, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), STRAAL)
            elif bord[r][c] == 2:
                pygame.draw.circle(scherm, GEEL, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), STRAAL)
    pygame.display.update()


def inputSpeler(speler, gameOver):
    positieX = event.pos[0]
    kol = int(math.floor(positieX / SQUARESIZE))

    if controleerPlaatsLeeg(bord, kol):
        row = geefVolgendeVrijeRij(bord, kol)
        plaatsStuk(bord, row, kol, speler)

        if speler == 1:
            kleur = ROOD
        else:
            kleur = GEEL

        if isGewonnen(bord, speler):
            label = myfont.render(f"Player {speler} wins!!", 1, kleur)
            scherm.blit(label, (40, 10))
            gameOver = True
    return gameOver


bord = maakBord()
gameOver = False
speler = 0

pygame.init()

SQUARESIZE = 100

width = AANTAL_KOLOMEN * SQUARESIZE
height = (AANTAL_RIJEN + 1) * SQUARESIZE

schermGrootte = (width, height)

STRAAL = int(SQUARESIZE / 2 - 5)

scherm = pygame.display.set_mode(schermGrootte)
tekenBord(bord)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            gameOver = True
            break

        if event.type == pygame.MOUSEMOTION:
            # maakt de de ruimte vanboven weer zwart zodat je geen 2 cirkel boven elkaar krijgt.
            pygame.draw.rect(scherm, ZWART, (0, 0, width, SQUARESIZE))

            # krijg positie. x = index 0, y = index 1
            positieX = event.pos[0]
            # telkens bij het verplaatsen van de muis, toon hij een cirkel vanboven waar de muis is
            if speler == 0:
                pygame.draw.circle(scherm, ROOD, (positieX, int(SQUARESIZE / 2)), STRAAL)
            else:
                pygame.draw.circle(scherm, GEEL, (positieX, int(SQUARESIZE / 2)), STRAAL)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # maakt de de ruimte vanboven weer zwart
            pygame.draw.rect(scherm, ZWART, (0, 0, width, SQUARESIZE))
            # Player1
            if speler == 0:
                gameOver = inputSpeler(speler + 1, gameOver)
            # Player 2
            else:
                gameOver = inputSpeler(speler + 1, gameOver)

            tekenBord(bord)

            speler = (speler + 1) % 2

            if gameOver:
                pygame.time.wait(3000)

