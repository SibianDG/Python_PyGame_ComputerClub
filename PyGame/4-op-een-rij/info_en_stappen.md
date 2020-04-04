# 4-op-een-rij
We beginnen met de basis voor een PyGame + enkele functies & stukken die we waarschijnlijk nodig zullen moeten hebben.
```python
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
    pass


def plaatsStuk(board, rij, kol, stuk):
    pass


def controleerPlaatsLeeg(board, col):
    pass


def geefVolgendeVrijeRij(board, col):
    pass


def isGewonnen(board, stuk):
    pass


def tekenBord(board):
    pass


def inputSpeler():
    pass


bord = maakBord()
gameOver = False
speler = 0

pygame.init()

# een vierkant, stukje is 100 pixel.
SQUARESIZE = 100
width = AANTAL_KOLOMEN * SQUARESIZE
# +1 omdat we een ruimte boven het bord willen hebben.
height = (AANTAL_RIJEN + 1) * SQUARESIZE
schermGrootte = (width, height)

scherm = pygame.display.set_mode(schermGrootte)
tekenBord(bord)

while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            gameOver = True
            break


        if event.type == pygame.MOUSEBUTTONDOWN:
            print('geklikt')
```

## Stap per stap
We willen in een 2D-array het spelbord bijhouden. 0 is leeg, 1 is speler 1 en 2 is speler 2.
- pass is om geen fouten te hebben. `pass` mag dus verwijderd worden.
- maakbord()
    maak 2D- spelbord en zorg ervoor dat je de constanten (variabelen in hoofdletter) gebruikt om alles op te vullen met 0
- plaatsStuk(...)
    -stuk op die positie, met dat bord en dat stuk (of getal)
- controleerPlaatsLeeg(bord, kol)
    - je kijkt ofdat er plaats is op de bovenste rij. Zo ja? Dan is het leeg.
- geefVolgendeVrijeRij(bord, kol)
    - Zoekt naar de volgende rij waar het 0, om __later__ daar iets in te steken.
- isGewonnen(bord, stuk)
    - controleert ofdat de laatste zet mogelijks de laatste zet was van het spel.
    - *TIP: for lus min 3, omdat je anders buiten de lijst zit.
- tekenBord()
    - Ja kan vanalles proberen. Alvast hieronder een mogelijke oplossing.
- inputSpeler()
```python
    # kol krijgen
    positieX = event.pos[0]
    kol = int(math.floor(positieX / SQUARESIZE))
```

   - controleert of het leeg is.
   - op de volgende lege rij zet je het suk.
   - Als het spel klaar is toon je een tekst vanboven
   ```python
            label = myfont.render(f"Player {speler} wins!!", 1, kleur)
            scherm.blit(label, (40, 10))
```

   - en geeft terug ofdat het gameOver is of niet.

- code onderaan
    - vul het aan met dit. Als je je muis beweegt, dan toont hij ook een stuk.
    
```python
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
```

- `if event.type == pygame.MOUSEBUTTONDOWN:` 
    - Maak de ruimte vanboven terug zwart
    
```python
            pygame.draw.rect(scherm, ZWART, (0, 0, width, SQUARESIZE))
```

   - input correcte speler
   - tekenSpelbord
   - verander van speler
   
   - extra: `            if gameOver:
                pygame.time.wait(3000)`

[Een mogelijke oplossing vind je hier](./4-op-een-rij.py)