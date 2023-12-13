import pygame
import maine
#iniciamos el pygame 
pygame .init()

size = (800,600)
pantalla = pygame.display.set_mode(size)
#cremaos reloj
reloj = pygame.time.Clock()
FPS = 60
#boleano de control
running = True 
#crear la nave
position = (200,200)
nave = maine.Nave(position)
#grupo de sprites
grupo_sprites = pygame.sprite.Group(nave)
grupo_sprites.add(maine.Nave((100,100)))
grupo_sprites.add(maine.Nave((300,300)))
grupo_sprites.add(maine.Nave((200,200)))
while running:
    #limitamos el bucle al framerate definido
    reloj.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    teclas = pygame.key.get_pressed()
    pantalla.fill((255,255,255))
    update
    grupo_sprites.update(teclas)
    grupo_sprites.draw(pantalla)

    pygame.display.flip()

#finalizamos el juego
pygame.quit()