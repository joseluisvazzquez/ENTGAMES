import pygame
pygame.init()
pantalla = pygame.display.set_mode((800,600))

imagenav = pygame.image.load("avion2.png")
avion = pygame.transform.scale(imagenav,(85,90))
salir = False
posIzd = 10
posTop = 10
while not salir:
    #gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True

    #gestionar cambiso 
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        posIzd -= 1
    if teclas[pygame.K_UP]:
        posTop -= 1
    if teclas[pygame.K_RIGHT]:
        posIzd += 1
    if teclas[pygame.K_DOWN]:
        posTop += 1
    pantalla.fill((255,200,255))
    #pygame.draw.rect(pantalla,(255,255,255),pygame.Rect(posIzd,posTop,60,60))
    pantalla.blit(avion,(posIzd, posTop))
    

    #redibujar juego
    pygame.display.flip()
pygame.quit
