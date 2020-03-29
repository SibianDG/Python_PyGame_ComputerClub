import pygame

pygame.init()

screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("ComputerClub")  # titel van venster (helemaal vanboven)

# gewoon variabelen maken zoals vroeger. Het beschrijft de rechthoek.
x = 0
y = 500-60
width = 40
height = 60
speed = 15

run = True
while run:
    pygame.time.delay(100)  # miliseconden
    for event in pygame.event.get():  # je vraagt aan PyGame de events (zoals klik, keybordpress etc) en je vraagt die. Dat geeft een array terug, dus die overlopen we.
        if event.type == pygame.QUIT:  # als je kruisje hebt geklikt
            run = False
    keys = pygame.key.get_pressed()  # vraag een array. Die array heeft als inhoud True en False.
    # zie tabel hieronder hoe een scherm opgebouw is.
    if keys[pygame.K_LEFT] and x >= speed:  # achter de schermen geeft hij eigenlijk een index weer, maar om het voor ons makkelijker te houden is het gewoon deze "index" pygame.K_LEFT
        x -= speed
    if keys[pygame.K_RIGHT] and x <= screenWidth - width:
        x += speed

    if keys[pygame.K_UP] and y >= speed:
        y -= speed
    if keys[pygame.K_DOWN] and y <= screenHeight - height:
        y += speed

    # telkens wanneer je iets verplaatsts, dan moet de achtergrond terug egaal gemaakt worden.
    win.fill((0, 0, 0))

    # tekenen van een rechthoek. Parameters hier gebruikt: op welk scherm? Kleur (tuple)? Afmetingen (in tuple)
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # scherm updaten.
    pygame.display.update()

# stopt het scherm NA de while-loop!
pygame.quit()
