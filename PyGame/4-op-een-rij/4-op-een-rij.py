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
    board = []
    for x in range(AANTAL_RIJEN):
        board.append([])
        for y in range(AANTAL_KOLOMEN):
            board[x].append(0)
    return board


def plaatsStuk(board, rij, kol, stuk):
    # de referentie is genoeg. Je moet het niet terug geven
    board[rij][kol] = stuk


def controleerPlaatsLeeg(board, col):
    # zolang dat op de bovenste lijn een 0 is, is er iets vrij.
    return board[AANTAL_RIJEN - 1][col] == 0


def geefVolgendeVrijeRij(board, col):
    for r in range(AANTAL_RIJEN):
        if board[r][col] == 0:
            return r


def isGewonnen(board, stuk):
    # horizontaal
    for c in range(AANTAL_KOLOMEN - 3):
        for r in range(AANTAL_RIJEN):
            if board[r][c] == stuk and board[r][c + 1] == stuk and board[r][c + 2] == stuk and board[r][c + 3] == stuk:
                return True

    # verticaal
    for c in range(AANTAL_KOLOMEN):
        for r in range(AANTAL_RIJEN - 3):
            if board[r][c] == stuk and board[r + 1][c] == stuk and board[r + 2][c] == stuk and board[r + 3][c] == stuk:
                return True

    # Hoofdiagonaal
    for c in range(AANTAL_KOLOMEN - 3):
        for r in range(AANTAL_RIJEN - 3):
            if board[r][c] == stuk and board[r + 1][c + 1] == stuk and board[r + 2][c + 2] == stuk and board[r + 3][c + 3] == stuk:
                return True

    # nevendiagonaal
    for c in range(AANTAL_KOLOMEN - 3):
        for r in range(3, AANTAL_RIJEN):
            if board[r][c] == stuk and board[r - 1][c + 1] == stuk and board[r - 2][c + 2] == stuk and board[r - 3][c + 3] == stuk:
                    return True


def tekenBord(board):
    for c in range(AANTAL_KOLOMEN):
        for r in range(AANTAL_RIJEN):
            pygame.draw.rect(screen, BLAUW, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, ZWART, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(AANTAL_KOLOMEN):
        for r in range(AANTAL_RIJEN):
            if board[r][c] == 1:
                pygame.draw.circle(screen, ROOD, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, GEEL, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


def inputSpeler(speler):
    posx = event.pos[0]
    col = int(math.floor(posx / SQUARESIZE))

    if controleerPlaatsLeeg(board, col):
        row = geefVolgendeVrijeRij(board, col)
        plaatsStuk(board, row, col, speler+1)

        if isGewonnen(board, 2):
            label = myfont.render(f"Player {speler+1} wins!!", 1, GEEL)
            screen.blit(label, (40, 10))
            gameOver = True


board = maakBord()
gameOver = False
turn = 0

pygame.init()

SQUARESIZE = 100

width = AANTAL_KOLOMEN * SQUARESIZE
height = (AANTAL_RIJEN + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
tekenBord(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            gameOver = True
            break

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, ZWART, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, ROOD, (posx, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, GEEL, (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, ZWART, (0, 0, width, SQUARESIZE))
            # print(event.pos)
            # Ask for Player 1 Input
            if turn == 0:
                inputSpeler(0)
            # # Ask for Player 2 Input
            else:
                inputSpeler(1)

            tekenBord(board)

            turn += 1
            turn = turn % 2

            if gameOver:
                pygame.time.wait(3000)

