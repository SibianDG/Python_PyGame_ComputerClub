# 1. Getting started with PyGame

Hiermee was je begonnen:
```python
import pygame
pygame.init()


win = pygame.display.set_mode((500, 500))
```
Dus heel even pauzeren. Wat is dat allemaal? Nu we pygame gebruiken en we iets daarvan willen gebruiken moeten we altijd eerst `pygame.[iets]` schrijven.
*__Enkel voor nerds__: Je roept een methode of functie aan in de de klasse pygame. net zoals string.upper() waarbij String klasse is en upper() methode.*
Voor de de rest roep je display, dus het tonen van het scherm met als modus of opties een 500x500 pixelscherm. (x, y) is een tuple. Overeenkomstig met een array van 2 elementen. Vaak gebruikt en handig, maar kan ook met meerdere elementen. Zie het gewoon als een array voorlopig, later leg ik wel uit wat er speciaal aan is.

Een beetje verder gaan. Laten we een rechthoek maken, laten verscheinen en bewegen.:
```python
import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("ComputerClub")  # titel van venster (helemaal vanboven)

# gewoon variabelen maken zoals vroeger. Het beschrijft de rechthoek.
x = 0
y = 0
width = 40
height = 60
speed = 5

run = True
while run:
    pygame.time.delay(100)  # miliseconden
    for event in pygame.event.get():  # je vraagt aan PyGame de events (zoals klik, keybordpress etc) en je vraagt die. Dat geeft een array terug, dus die overlopen we.
        if event.type == pygame.QUIT:  # als je kruisje hebt geklikt
            run = False
    keys = pygame.key.get_pressed() # vraag een array. Die array heeft als inhoud True en False.
    # zie tabel hieronder hoe een scherm opgebouw is.
    if keys[pygame.K_LEFT]: # achter de schermen geeft hij eigenlijk een index weer, maar om het voor ons makkelijker te houden is het gewoon deze "index" pygame.K_LEFT
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # telkens wanneer je iets verplaatsts, dan moet de achtergrond terug egaal gemaakt worden. 
    win.fill((0, 0, 0))

    # tekenen van een rechthoek. Parameters hier gebruikt: op welk scherm? Kleur (tuple)? Afmetingen (in tuple)
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # scherm updaten.
    pygame.display.update()

# stopt het scherm NA de while-loop!
pygame.quit()
``` 

##### Richtingen
- links: x - 1
- rechts: x + 1
- boven: y - 1
- onder: y + 1

### Kleuren - RGB
De kleuren in Python zijn in RGB (omdat het op schermen is). RGB staat voor Rood Groen Blauw. (0, 0, 0) betekent geen licht van niets, dus zwart. De maximum waarde is 255, met als gevolg als je (255, 255, 255) hebt, dan heb je alle licht tegelijk en dus wit.
- [Kleurenpsychologie](https://www.w3schools.com/colors/colors_psychology.asp)
- [Kleuren samenstellen](https://color.adobe.com/create)




