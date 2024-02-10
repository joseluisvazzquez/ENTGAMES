import pygame, sys
from elements import Aircraft, Background, Bullet

background = Background()
bullet_group = pygame.sprite.Group()

aircraft = Aircraft(bullet_group)
all_sprites = pygame.sprite.Group()
all_sprites.add(aircraft)


# bullet_sprites.add(bullet)

pygame.init()


exit = False
clock = pygame.time.Clock()
FPS = 60
while not exit:
    clock.tick(60)
    #gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
     
     
    all_sprites.update()
    bullet_group.update()
    background.scrollback()
    all_sprites.draw(background.screen)
    bullet_group.draw(background.screen)
    
    #redibujar juego
    pygame.display.flip()
pygame.quit()