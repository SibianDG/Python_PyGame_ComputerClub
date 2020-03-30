# 1. Installatie PyGame

### Windows
Open Windows PowerShell
Voer uit: `pip install pygame`

### MacOS
Open terminal:
`pip install pygame` *niet 100% zeker, laat me iets weten!*

### Linux Ubuntu
`sudo apt-get install python-pygame`

#Gebruik PyGame
bovenaan aan het script doe je de import:
`import pygame`

#PyCharm
Typ `import pygame` in een nieuw script. Er komt een rode lijn. Klik er op en installeer pygame via PyCharm. Dit is zodat PyCharm weet dat je hiermee bezig bent en dat hij fouten kan zien, makkelijk kan aanvullen etc.

Voer het volgende uit en kijk of je heel even een 500x500 scherm krijgt:
```python
import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Test")
```


###### voetnotitie
Zo importeer je elke library makkelijk. Zo ook libraries voor bigdata, machine learling, AI, robots aansturen etc. Ga naar Google en leer wat je wil!
