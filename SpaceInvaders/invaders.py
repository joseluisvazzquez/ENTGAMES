import pygame
from elements import Aircraft, Background

background = Background()

aircraft = Aircraft()
all_sprites = pygame.sprite.Group()
all_sprites.add(aircraft)

pygame.init()


exit = False
clock = pygame.time.Clock()
FPS = 60
while not exit:
    clock.tick(60)
    #gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        

    keyboard = pygame.key.get_pressed()
    all_sprites.update()
    background.scrollback()
    all_sprites.draw(background.screen)
    #redibujar juego
    
    
    pygame.display.flip()
pygame.quit()