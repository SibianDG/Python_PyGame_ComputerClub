# Galgje
We beginnnen met de standaard code voor een PyGame met functies direct:
```python
import pygame


def buildGUI():
    pygame.init()  # start pygame
    win = pygame.display.set_mode((600, 600))  # afmetingen
    pygame.display.set_caption("Galgje")  # titel window
    return win  # dit hebben we later nog nodig


def draw(win):
    win.fill((255, 255, 255))  # achtergrond wit


def speelSpel(win):
    run = True
    while run:  # pygame basic
        draw(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()  # achtergrond updaten.

    pygame.quit()  # na while, dus na op kruisje geklikt te hebben, stopt het.


speelSpel(buildGUI())
```

## Stappenplan 1
We gaan eens het domein, de logica in de functie van speelSpel zelf doen. Het is voor dit spel eens makkelijker. (denk ik).
Oke, wat hebben we nodig in galgje?
- Een te raden woord. -> variabele.
- Een lijst met alle ingedrukte letters. -> Lege lijst.
- Weten welke letter je net hebt ingetyped.
    - Ik wil geen 26 if'kes. -> `press = pygame.key.get_pressed()`
        - Geeft een `True` op welke knop die geduwd heeft. Het is een array met zoveel keer False en 1x True.
    - For loop over het alfabet.
        - *TIP: a heeft een letterwaarde en z ook. Als je van a-z loopt...*
        - TIP2: van `pygame.K_a` tot `pygame.K_z + 1`
    - Check ofdat die letter ingedrukt is.
    - Krijg de letter: `pygame.key.name(i)`
    - Als de letter nog niet in de array zit, dan voeg je die toe aan de lijst.
- Draw aanpassen
    - in een variable kijken hoeveel er fout zijn.
    - Als het aantal fout niet 0 is en lager dan 12. (In galgje mag je max 11 fout hebben.)
        - Dan: `foto = pygame.image.load(str(aantalFout) + '.png')` `win.blit(foto, (70, 50))`
    - De String maken wat je moet tonen. Begin: "_ _ _". Controleren of de lijst van letters, letters bevat die in het woord zitten en invullen.
    - Makkelijk om van lijst/array naar string te gaan: `" ".join(woordTeTonen)`
    - Controleren of je misschien niet moet zeggen: "GEWONNEN" of " GAME OVER".
    - Tekst tonen
    
    ```python
    fontOnderaan = pygame.font.SysFont("Calibri, Arial", 30)  # font voor van onder. Kleiner
    tekst = fontOnderaan.render(woordTeTonen, True, (0, 0, 0))  # render de zin
    win.blit(tekst, (600 / 2 - tekst.get_rect().width / 2, 500))  # toon op scherm
    ```
### Oplossing:
Een mogelijk oplossing vind je [hier](./Oplossing/Galgje.py) of hieronder.

X

X

X

X

X

X

X

X

X

X

X

X


```python
import pygame


def buildGUI():
    pygame.init()  # start pygame
    win = pygame.display.set_mode((600, 600))  # afmetingen
    pygame.display.set_caption("Galgje")  # titel window
    return win  # dit hebben we later nog nodig


def draw(win, letterArray, woord):
    win.fill((255, 255, 255))  # achtergrond wit

    aantalFout = 0
    for letter in letterArray:
        if letter not in woord:
            aantalFout += 1
    if aantalFout != 0 and aantalFout < 12:
        if aantalFout > 11:
            aantalFout = 11
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

    if "_" not in woordTeTonen:
        woordTeTonen = "GEWONNEN"

    if aantalFout >= 11:
        woordTeTonen = "GAME OVER"

    fontOnderaan = pygame.font.SysFont("Calibri, Arial", 30)  # font voor van onder. Kleiner
    tekst = fontOnderaan.render(woordTeTonen, True, (0, 0, 0))  # render de zin
    win.blit(tekst, (600 / 2 - tekst.get_rect().width / 2, 500))  # toon op scherm


def speelSpel(win):
    woord = "Computerclub"
    letterArray = []

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
