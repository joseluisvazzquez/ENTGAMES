import pygame


class Aircraft:
    def __init__(self) -> None:
        self.posleft = 200
        self.postop = 200
        aircraft_img = [pygame.image.load("SpaceInvaders/avion1.png"),pygame.image.load("SpaceInvaders/avion2.png"),pygame.image.load("SpaceInvaders/avion-left.png"),pygame.image.load("SpaceInvaders/avion-right.png"),pygame.image.load("SpaceInvaders/avion-bullet.png")]
        self.count = 0
        self.aircraft = [pygame.transform.scale(aircraft_img[0],(90,90)),pygame.transform.scale(aircraft_img[1],(90,90)),pygame.transform.scale(aircraft_img[2],(90,90)),pygame.transform.scale(aircraft_img[3],(90,90)),pygame.transform.scale(aircraft_img[4],(30,30))]
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
    def shoot(self):
        hj
class Background:
    def __init__(self) -> None:
         bg = ("SpaceInvaders/background.png")
