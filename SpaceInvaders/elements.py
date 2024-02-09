from random import randint
import pygame

class Aircraft(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = [
            pygame.image.load("SpaceInvaders/aircraft_img/avion1.png"),
            pygame.image.load("SpaceInvaders/aircraft_img/avion2.png")
            ]
        self.sprites_movement = [
            pygame.transform.scale(pygame.image.load("SpaceInvaders/aircraft_img/avion-left.png"), (95,90)),
            pygame.transform.scale(pygame.image.load("SpaceInvaders/aircraft_img/avion-right.png"), (95,90))]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = (95, 90)
    def update(self):
        self.handle_input()
        # self.animate()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.animate()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 3
            self.image = self.sprites_movement[0]
        if keys[pygame.K_RIGHT] and self.rect.right < 492:
            self.rect.x += 3
            self.image = self.sprites_movement[1]
        
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 3
            self.animate()
        if keys[pygame.K_DOWN] and self.rect.bottom < 892:
            self.rect.y += 3
            self.animate()

    def animate(self):
        self.current_sprite += 1
        if self.current_sprite > 1:
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (95, 90))
class Background:
    def __init__(self) -> None:
        width = 482
        height = 892
        self.screen = pygame.display.set_mode((width,height))
        self.bg = pygame.image.load("SpaceInvaders/frame.png").convert()
        self.bg_height = self.bg.get_height()
        self.scroll = 0

    def scrollback(self):
        self.scroll += 1.5
        if self.scroll > self.bg_height:
            self.scroll = 0
        self.screen.blit(self.bg, (0, self.scroll - self.bg_height))
        self.screen.blit(self.bg, (0, self.scroll))
    
    #Funcion de niveles y mas... Esta en proceso   
    
        