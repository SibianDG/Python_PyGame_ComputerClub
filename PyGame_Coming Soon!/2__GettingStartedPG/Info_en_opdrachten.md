# 2. Getting started with PyGame

Hiermee was je begonnen:
```python
import pygame
pygame.init()


win = pygame.display.set_mode((500, 500))
```
Dus heel even pauzeren. Wat is dat allemaal? Nu we pygame gebruiken en we iets daarvan willen gebruiken moeten we altijd eerst `pygame.[iets]` schrijven.
*__Enkel voor nerds__: Je roept een methode of functie aan in de de klasse pygame. net zoals string.upper() waarbij String klasse is en upper() methode.*
Voor de de rest roep je display, dus het tonen van het scherm met als modus of opties een 500x500 pixelscherm. (x, y) is een tuple. Overeenkomstig met een array van 2 elementen. Vaak gebruikt en handig, maar kan ook met meerdere elementen. Zie het gewoon als een array voorlopig. ik leg later wel uit wat er speciaal aan is. 
