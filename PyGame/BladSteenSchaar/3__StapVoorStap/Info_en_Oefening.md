# 3. Stap voor Stap - Blad Steen Schaar
We beginnnen met de code van puntje 2:
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

## Stappenplan 1
- Laten we eerst alles eens in functies steken dat het wat overzichtelijker wordt.
    - buildGUI(): geeft het gemaakte window terug
    - draw(win): tekent alles op window
    - speelSpel(win): hier runt het programma + event afhandeling.
- Laat het spel starten
### Oplossing 1:
```python
import pygame
import random

def buildGUI():
    pygame.init()  # start pygame
    win = pygame.display.set_mode((600, 600))  # afmetingen
    pygame.display.set_caption("Blad Steen Schaar")  # titel window
    return win  # dit hebben we later nog nodig

def draw(win):
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
def speelSpel(win):
    run = True
    while run:  # pygame basic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()  # achtergrond updaten.

    pygame.quit()  # na while, dus na op kruisje geklikt te hebben, stopt het.

speelSpel(buildGUI())
```

## Stappenplan 2
- Functie maken bewerkingen `bewerkingen(keuzeGetal)`
    - array met keuzes
    - we willen de keuze van de computer terug geven en ook het resultaat van de bewerkingen. 0 verloren, 1 gewonnen, 2 gelijk.
    - laat de computer een keuze maak uit de 3 via `random.randint(min, maxInbegrepen)`
    - voeg de keuze toe aan de resultatenarray
    - voer de bewerkingen uit en voeg getal toe aan array

### Oplossingen 2:
```python
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
```

## Stappenplan 3
- Om te beginnen moeten in speelSpel iets hebben dat zegt dat we nog niet begonnen zijn. Ik kies voor
    - Ik kies voor `resultaat = ["", 3]`
- draw moet een beetje aangepast worden:
    - een extra parameter `resultaat`. Die array.
    - i.p.v. 3 variabelen voor BSS, laten we dat in een array steken.
    - afhandeling van tekst
        - `gewonnen = resultaat[1]  # gewonnen, verloren, gelijk of nog beginnen`
        - `keuzeComputer = resultaat[0]`
        - verder instellen m.b.v. fontOnderaan en resultaatText
    - geef de array terug met daarin de 3 foto's
- in speelSpel
    - telkens bij het runnen moet hij alles opnieuw tekenen => Voor mocht er tekst veranderen. Mocht je niet opnieuw tekenen, dan zou alles gewoon boven elkaar komen.
    - die array met foto's vul je op door `keuzeFoto = draw(win, resultaat) `
```python
            if event.type == pygame.MOUSEBUTTONUP:  # als er op muis geklikt is
                position = pygame.mouse.get_pos()  # geef positie muis
                # TODO
```
- Overloop elke foto (uit de array) met een __index__.
- controleer ofdat de muis op de foto staat met `.collidepoint(position)`
- resultaat verandert naar de uitkomst van de functie `bewerkingen`

### Oplossing 3

X

X

X

X

X

X

X


```python
import pygame
import random


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
                 win.blit(pygame.image.load('schaar.png'), (400, 50))]

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

```

Hopelijk is het een beetje gelukt! Programmeren is stap per stap opbouwen. Proberen, mislukken en opnieuw proberen. Nu heb je al eens een volledig spel gemaakt, dus wat houdt je nog tegen om zelf iets te proberen? 
