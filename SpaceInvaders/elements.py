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
            pygame.image.load("SpaceInvaders/aircraft_img/avion-left.png"),
            pygame.image.load("SpaceInvaders/aircraft_img/avion-right.png")]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = (200, 400)

<<<<<<< HEAD
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
        if keys[pygame.K_RIGHT] and self.rect.right < 482:
            self.rect.x += 3
            self.image = self.sprites_movement[1]
        
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 3
            self.animate()
        if keys[pygame.K_DOWN] and self.rect.bottom < 898:
            self.rect.y += 3
            self.animate()

    def animate(self):
        self.current_sprite += 1
        if self.current_sprite > 1:
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (50, 50))
=======
class Aircraft:
    def __init__(self) -> None:
        self.posleft = 200
        self.postop = 200
        aircraft_img = [pygame.image.load("SpaceInvaders/avion1.png"),pygame.image.load("SpaceInvaders/avion2.png"),pygame.image.load("SpaceInvaders/avion-left.png"),pygame.image.load("SpaceInvaders/avion-right.png")]
        self.count = 0
        self.aircraft = [pygame.transform.scale(aircraft_img[0],(90,90)),pygame.transform.scale(aircraft_img[1],(90,90)),pygame.transform.scale(aircraft_img[2],(90,90)),pygame.transform.scale(aircraft_img[3],(90,90))]
        screen = pygame.display.get_surface()
        self.screen2 = screen
    
    def paint(self):
        self.count = (self.count+1)%40
        self.screen2 
        selected = self.count // 20
        self.screen2.blit(self.aircraft[selected],(self.posleft, self.postop))

    def paintleft(self):
        self.screen2
        self.screen2.blit(self.aircraft[2],(self.posleft, self.postop))
    def paintright(self):
        self.screen2
        self.screen2.blit(self.aircraft[3],(self.posleft, self.postop))
        
    def moveleft(self):
        if(self.posleft > 0):
            self.posleft -= 3
        
    def moveright(self):
        if(self.posleft < 480 - 90):
            self.posleft += 3
            
    def movetop(self):
        if(self.postop > 0):
            self.postop -= 3
    def movedown(self):
        if(self.postop <800 - 90):
            self.postop += 3

>>>>>>> 54b74b593ef8295d69207400b7b7b8d6f0e0aa11
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
    
        