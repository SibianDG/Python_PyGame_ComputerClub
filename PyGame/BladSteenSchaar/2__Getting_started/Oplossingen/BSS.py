import pygame
import random

pygame.init()  # start pygame
win = pygame.display.set_mode((600, 600))  # afmetingen
pygame.display.set_caption("Blad Steen Schaar")  # titel window

win.fill((255, 255, 255))  # achtergrond wit
fontTitle = pygame.font.SysFont("Calibri, Arial", 30)  # font voor titel
text = fontTitle.render("Kies uit blad, steen of schaar", True, (0, 0, 0))  # render de zin
win.blit(text, (125, 0))  # toon op scherm

bladFoto = pygame.image.load('blad.png')
steenFoto = pygame.image.load('steen.png')
schaarFoto = pygame.image.load('schaar.png')

blad = win.blit(bladFoto, (25, 50))
steen = win.blit(steenFoto, (225, 50))
schaar = win.blit(schaarFoto, (400, 50))

fontOnderaan = pygame.font.SysFont("Calibri, Arial", 20)  # font voor van onder. Kleiner
resultaatText = fontOnderaan.render("Start spel", True, (0, 0, 0))  # render de zin
win.blit(resultaatText, (100, 500))  # toon op scherm

run = True
while run:  # pygame basic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()  # achtergrond updaten.

pygame.quit()  # na while, dus na op kruisje geklikt te hebben, stopt het.

