import pygame
from elements import Aircraft

pygame.init()

screen = pygame.display.set_mode((480,800))

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
    background_image = pygame.image.load("SpaceInvaders/background.png")
    screen.blit(background_image, [0, 0])
    
    keyboard = pygame.key.get_pressed()
    if not keyboard[pygame.K_LEFT] and not keyboard[pygame.K_RIGHT]:
       aircraft.paint()
       
    if keyboard[pygame.K_LEFT] and  keyboard[pygame.K_RIGHT]:
        aircraft.paint()

    if keyboard[pygame.K_LEFT] and not keyboard[pygame.K_RIGHT]:
        aircraft.moveleft()
        aircraft.paintleft()

    if keyboard[pygame.K_UP]:
        aircraft.movetop()
        
    if keyboard[pygame.K_RIGHT] and not keyboard[pygame.K_LEFT]:
        aircraft.moveright()
        aircraft.paintright()
    
    if keyboard[pygame.K_DOWN]:
        aircraft.movedown()
    if keyboard[pygame.K_BACKSPACE]:
        aircraft.shoot()
    
    

    #redibujar juego
    pygame.display.flip()
pygame.quit
