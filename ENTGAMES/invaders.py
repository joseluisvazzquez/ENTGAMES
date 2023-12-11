import pygame
from aircraft import Aircraft, background
pygame.init()

screen = pygame.display.set_mode((900,600))

aircraft = Aircraft()
#enemies = Enemies()
exit = False
clock = pygame.time.Clock()
FPS = 60
while not exit:
    clock.tick(60)
    #gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    #gestionar cambiso 
    keyboard = pygame.key.get_pressed()
    if keyboard[pygame.K_LEFT]:
        aircraft.moveleft()

    if keyboard[pygame.K_UP]:
        aircraft.movetop()

    if keyboard[pygame.K_RIGHT]:
        aircraft.moveright()

    if keyboard[pygame.K_DOWN]:
        aircraft.movedown()

    background_img = background()
    #pygame.draw.rect(pantalla,(255,255,255),pygame.Rect(posIzd,posTop,60,60))
    background.draw()
    aircraft.paint()
    #redibujar juego
    pygame.display.flip()
pygame.quit
