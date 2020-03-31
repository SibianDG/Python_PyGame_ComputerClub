# 2. Getting Started - Blad Steen Schaar

## Even theorie
#### Kleuren - RGB
De kleuren in Python zijn in RGB (omdat het op schermen is). RGB staat voor Rood Groen Blauw. (0, 0, 0) betekent geen licht van niets, dus zwart. De maximum waarde is 255, met als gevolg als je (255, 255, 255) hebt, dan heb je alle licht tegelijk en dus wit.
- [Kleurenpsychologie](https://www.w3schools.com/colors/colors_psychology.asp)
- [Kleuren samenstellen](https://color.adobe.com/create)

### Hoe is een scherm opgebouwd?
Zoals een tweedimensionale array:

| x,y | x,y | x,y | x,y |
| ----- | ---- | ---- | ---- |
| 0,0 | 1,0 | 2,0 | ... |
| 0,1 | 1,1 | 2,1 | ... |
| 0,2 | 1,2 | 2,2 | ... |

We beginnen met onze basis:
```python
import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Blad Steen schaar")
```
*Weet dat je sommige dingen ofwel vanbuiten moet weten, ofwel zal moeiten kopiëren van andere oefeningen. Dat is programmeren. Soms kopiëren en plakken.*
## Opdracht: maak de lay-out of GUI (Graphic User Interface)
- Vergroot het window naar 600 bij 600.
- Maak de achtergrond wit
    - vul het window. `fill((R, G, B))`
- Zet een tekst op het scherm
```python
fontTitle = pygame.font.SysFont("Calibri, Arial", 30)  # font voor titel
text = fontTitle.render("HIERJETEKST", True, (0, 0, 0))  # render de zin
win.blit(text, (125, 0))  # toon op scherm
```
- Steek in 3 variabelen de foto's BSS. __Zorg ervoor dat de foto's in dezelde map zitten__
```python
pygame.image.load('fotoInDezelfdeFolder.png')
```
- Toon de foto's op het scherm
```python
win.blit(foto, (x, y))
```
- Toon nog een tekst aan de onderkant van het scherm: "Kies BSS"
- Het tweede standaard stukje PyGame om een game draaiende te houden:
```python
run = True
while run:  # pygame basic
    for event in pygame.event.get(): # je vraagt aan PyGame de events (zoals klik, keybordpress etc) en je vraagt die. Dat geeft een array terug, dus die overlopen we.
        if event.type == pygame.QUIT: # als je kruisje hebt geklikt
            run = False

    pygame.display.update()  # achtergrond updaten.

pygame.quit()  # NA while, dus na op kruisje geklikt te hebben, stopt het.
```

## Oplossing
Kijk alleen als je écht vast zit:

X

X

X

X

X

X

```python
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


```



