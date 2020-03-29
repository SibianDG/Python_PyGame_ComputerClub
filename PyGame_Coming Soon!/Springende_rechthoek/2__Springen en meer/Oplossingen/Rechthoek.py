import pygame
pygame.init()

screenWidth = 500
screenHeight = 500
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("First Game")

x = 0
y = screenHeight-60
width = 40
height = 60
vel = 5

jumping = False
# sprongstappen. 10 - 0 -> omhoog, 0 - -10 -> naar beneden.
# we kunnen die min gebruiken om aan te geven om te stijgen of te dalen
jumpCount = 10

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel

    if not jumping:
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jumpCount >= -10:
            # functie x², rekening houdend met stijgen en dalen.
            # * 0.5 is om het smoother te laten lopen.
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            #  reset
            jumpCount = 10
            jumping = False

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

