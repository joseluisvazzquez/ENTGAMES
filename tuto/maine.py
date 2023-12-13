from typing import Any
import pygame

class Nave(pygame.sprite.Sprite):
    #constructor
    def __init__(self, position) -> None:
        super().__init__() 
        #cargamos una imagen
        self.image = pygame.image.load("SpaceInvaders/avion1.png")
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()

        self.rect.topleft = position
    def update(self, *args: Any, **kwargs: Any) -> None:
        teclas = args[0]
        if teclas[pygame.K_LEFT]:
            self.rect.x -=2
        if teclas[pygame.K_RIGHT]:
            self.rect.x +=2
    