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
- Dit is de basis. Jullie kunnen natuurlijk zelf nog meer toevoegen, aanpassen etc. Veel succes!
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
