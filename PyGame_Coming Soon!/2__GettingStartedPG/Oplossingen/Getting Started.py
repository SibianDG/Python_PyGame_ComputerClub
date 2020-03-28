import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("ComputerClub")  # titel van venster (helemaal vanboven)


# gewoon variabelen maken zoals vroeger.
x = 50
y = 50
width = 40
height = 60
speed = 5

run = True

while run:
    pygame.time.delay(100)  # miliseconden
    for event in pygame.event.get():  # je vraagt aan PyGame de events (zoals klik, keybordpress etc) en je vraagt die. Dat geeft een array terug, dus die overlopen we.
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    #TODO 28/03/2020: screenshot is info over pixels van een scherm. Links boven
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
