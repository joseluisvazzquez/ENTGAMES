import pygame


class Aircraft:
    def __init__(self) -> None:
        self.posleft = 30
        self.postop = 30
        aircraft_img = [pygame.image.load("ENTGAMES/avion1.png"),pygame.image.load("ENTGAMES/avion2.png")]
        self.count = 0
        self.aircraft = [pygame.transform.scale(aircraft_img[0],(60,90)),pygame.transform.scale(aircraft_img[1],(60,90))]

    def paint(self):
        self.count = (self.count+1)%40
        screen = pygame.display.get_surface()
        selected = self.count // 20
        screen.blit(self.aircraft[selected],(self.posleft, self.postop))
    
    def moveleft(self):
        if(self.posleft > 1):
            self.posleft -= 1
    def moveright(self):
        if(self.posleft > 1):
            self.posleft += 1
    def movetop(self):
        if(self.postop > 1):
            self.postop -= 1
    def movedown(self):
        if(self.postop > 1):
            self.postop += 1
    

