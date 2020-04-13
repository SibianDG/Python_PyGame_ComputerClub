import pygame
import os
pygame.init()

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Blad Steen schaar")

win.fill((255, 255, 255))

fontTitle = pygame.font.SysFont("Calibri, Arial", 30)  # font voor titel
text = fontTitle.render("Schaar-Steen-Papier", True, (0, 0, 0))  # render de zin
win.blit(text, (125, 0))  # toon op scherm

bladFoto = os.getcwd()+'\\blad.png'
win.blit(pygame.image.load('blad.png'), (25, 50))
