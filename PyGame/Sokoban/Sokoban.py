import pygame
import operator

def buildGUI():
    pygame.init()  # start pygame
    win = pygame.display.set_mode((750, 750))  # afmetingen
    pygame.display.set_caption("Sokoban")
    return win  # dit hebben we later nog nodig


def speelSpelGUI(win):
    bord = initBord()
    # speelveldGUIArray = verversAchtergrond(win, speelveld, spelerIndex)  # een array met daarin alle 9 de
    # vierkanten/velden.

    run = True
    while run:  # pygame basic

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if not isSpelKlaar(bord):
            if keys[pygame.K_UP]:
                bord = verplaats(bord, 0)
            if keys[pygame.K_RIGHT]:
                bord = verplaats(bord, 1)
            if keys[pygame.K_DOWN]:
                bord = verplaats(bord, 2)
            if keys[pygame.K_LEFT]:
                print("left")
                bord = verplaats(bord, 3)
            pygame.time.wait(50)
        else:
            pygame.time.wait(5000)
        verversAchtergrond(win, bord)  # achtergrond vernieuwen.
        pygame.display.update()  # achtergrond updaten.

    pygame.quit()


def verversAchtergrond(win, bord):
   win.fill((255, 255, 255))  # mocht de afbeelding te klein zijn, wordt het daarachter wit

   for indexRij, rij in enumerate(bord):
       for indexKol, kol in enumerate(bord):
           if bord[indexRij][indexKol] == "M":
               win.blit(pygame.image.load("speler.png"), (indexKol*75, indexRij*75))
           elif bord[indexRij][indexKol] == " ":
               win.blit(pygame.image.load("floor.png"), (indexKol*75, indexRij*75))
           elif bord[indexRij][indexKol] == "x":
               win.blit(pygame.image.load("emerald.png"), (indexKol*75, indexRij*75))
           elif bord[indexRij][indexKol] == ".":
               win.blit(pygame.image.load("doel.png"), (indexKol*75, indexRij*75))
           elif bord[indexRij][indexKol] == "#":
               win.blit(pygame.image.load("muur.png"), (indexKol*75, indexRij*75))

def initBord():
    bordString = "###########..     ###..      ##### #   ##      # ##   ##x  ##   x  # ## x x#  ###       M###########"
    bord = []
    for index, veld in enumerate(bordString):
        if index % 10 == 0:
            bord.append([])
        bord[int(index / 10)].append(veld)
    printBord(bord)
    return bord

def verplaats(bord, richting):  # 0, 1, 2, 3
    positieMan = (0, 0)
    richtingen = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

    for rijIndex, rij in enumerate(bord):
        for kolIndex, kol in enumerate(rij):
            if kol == "M":
                positieMan = (rijIndex, kolIndex)
    gewenstePositie = tuple(map(operator.add, positieMan, richtingen[richting]))
    if bord[gewenstePositie[0]][gewenstePositie[1]] == " ":
        bord[positieMan[0]][positieMan[1]] = " "
        bord[gewenstePositie[0]][gewenstePositie[1]] = "M"
    if bord[gewenstePositie[0]][gewenstePositie[1]] == "x":
        positieAchterPositie = tuple(map(operator.add, gewenstePositie, richtingen[richting]))
        if bord[positieAchterPositie[0]][positieAchterPositie[1]] == " ":
            bord[positieMan[0]][positieMan[1]] = " "
            bord[gewenstePositie[0]][gewenstePositie[1]] = "M"
            bord[positieAchterPositie[0]][positieAchterPositie[1]] = "x"
    return bord


def isSpelKlaar(bord):
    klaar = True
    for rij in bord:
        for kol in rij:
            if kol == ".":
                klaar = False
                break
    return klaar


def printBord(bord):
    for rij in bord:
        for kol in rij:
            print(kol, end=" ")
        print("")


#while not isSpelKlaar(bord):
#    print(printBord())
#    richting = int(input())
#    verplaats(bord, richting)

speelSpelGUI(buildGUI())
