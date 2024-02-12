import random
import pygame, sys
from elements import Aircraft, Background, Enemy, EnemyBullet
background = Background()
bullet_group = pygame.sprite.Group()
enemy_group =  pygame.sprite.Group()
enemy_bullet_group =  pygame.sprite.Group()
aircraft = Aircraft(bullet_group)
all_sprites = pygame.sprite.Group()
all_sprites.add(aircraft)
 

# bullet_sprites.add(bullet)
start_time = pygame.time.get_ticks()
start_time_bullet = pygame.time.get_ticks()
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
    
    def create_aliens():
        enemy = Enemy(random.randint(70, 600), 10)
        enemy_group.add(enemy)
    
    current_time = pygame.time.get_ticks()
    current_time_bullet = pygame.time.get_ticks()
    
    lapsed_time = current_time - start_time
    lapsed_time_bullet = current_time_bullet - start_time_bullet
    
    if lapsed_time >= 5000:
        create_aliens()
        start_time = current_time
    
    if lapsed_time_bullet >= 1000:
        attacking_enemy = enemy_group.sprites()

        if attacking_enemy:
            attacking_enemies = attacking_enemy[0]
            enemy_bullet = EnemyBullet(attacking_enemies.rect.centerx,attacking_enemies.rect.bottom)
            enemy_bullet_group.add(enemy_bullet)
            start_time_bullet = current_time_bullet
            print(len(enemy_bullet_group))
            
    
    all_sprites.update()
    bullet_group.update()
    enemy_group.update()
    enemy_bullet_group.update()
    
    background.scrollback()
    
    all_sprites.draw(background.screen)
    bullet_group.draw(background.screen)
    enemy_group.draw(background.screen)
    enemy_bullet_group.draw(background.screen)
    #redibujar juego
    pygame.display.flip()
pygame.quit()