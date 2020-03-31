import pygame


def buildGUI():
    pygame.init()  # start pygame
    win = pygame.display.set_mode((600, 600))  # afmetingen
    pygame.display.set_caption("Galgje")  # titel window
    return win  # dit hebben we later nog nodig


def draw(win, letterArray, woord):
    win.fill((255, 255, 255))  # achtergrond wit

    aantalFout = len(letterArray)
    if aantalFout != 0 and aantalFout < 12:
        foto = pygame.image.load(str(aantalFout) + '.png')
        win.blit(foto, (70, 50))

    woordTeTonen = []
    for _ in range(len(woord)):
        woordTeTonen.append("_")
    for letter in letterArray:
        letter = letter.lower()
        if letter in woord:
            for index, value in enumerate(woord):
                if letter == value.lower():
                    if woordTeTonen[index] == "_":
                        woordTeTonen[index] = letter

    woordTeTonen = " ".join(woordTeTonen)

    if aantalFout >= 12:
        woordTeTonen = "GAME OVER"

    fontOnderaan = pygame.font.SysFont("Calibri, Arial", 30)  # font voor van onder. Kleiner
    tekst = fontOnderaan.render(woordTeTonen, True, (0, 0, 0))  # render de zin
    win.blit(tekst, (600 / 2 - tekst.get_rect().width / 2, 500))  # toon op scherm


def speelSpel(win):
    letterArray = []
    woord = "Computerclub"

    run = True
    while run:  # pygame basic
        draw(win, letterArray, woord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            press = pygame.key.get_pressed()
            for i in range(pygame.K_a, pygame.K_z + 1):
                if press[i]:
                    letterIngedrukt = pygame.key.name(i)
                    if letterIngedrukt not in letterArray:
                        letterArray.append(pygame.key.name(i))

        pygame.display.update()  # achtergrond updaten.

    pygame.quit()  # na while, dus na op kruisje geklikt te hebben, stopt het.


speelSpel(buildGUI())
