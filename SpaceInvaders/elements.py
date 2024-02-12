import random
import pygame

class Aircraft(pygame.sprite.Sprite):
    def __init__(self, bullet_group):# alien_group
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
        self.rect.topleft = (200, 800)
        self.bullet_group = bullet_group
 
        self.final_shot = pygame.time.get_ticks()
        
        
    def update(self):
        keys = pygame.key.get_pressed()
        pantalla = pygame.display.get_surface()
        speed = 3
        cooldown = 500
        
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.animate()
        
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
            self.image = self.sprites_movement[0]
        
        if keys[pygame.K_RIGHT] and self.rect.x + self.image.get_width() < pantalla.get_width():
            self.rect.x += speed
            self.image = self.sprites_movement[1]
        
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= speed
            self.animate()
            
        if keys[pygame.K_DOWN] and self.rect.y + self.image.get_height() < pantalla.get_height():
            self.rect.y += speed
            self.animate()
        time_now = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and time_now - self.final_shot > cooldown: 
            bullet = Bullet(self.rect.centerx, self.rect.top) 
            self.bullet_group.add(bullet)
            self.final_shot = time_now          
      
    def animate(self):
        self.current_sprite += 1
        if self.current_sprite > 1:
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (95, 90))
        
    def create_bullet(self):
        return Bullet(self.rect.x,self.rect.y)
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("SpaceInvaders/aircraft_img/bullet.png"), (20, 30))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        

    def update(self):
        self.rect.y -= 5
        if self.rect.y < 0:
            self.kill()
                
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()       
        self.image = pygame.transform.scale(pygame.image.load("SpaceInvaders/enemy_img/e"+ str(random.randint(1, 2))+".png"),(110, 100))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.speed = 2
        
    def update(self):
        self.rect.y += 3
        self.rect.x += self.speed
        pantalla = pygame.display.get_surface()

        if self.rect.left < 0 or self.rect.right > random.randint(400, 800):
            self.speed *= -1
        if self.rect.x  + self.image.get_width()< 0 or self.rect.y + self.image.get_height() > pantalla.get_height() + 30:
            self.kill()
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("SpaceInvaders/enemy_img/enemy_bullet.png"), (20, 30))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y] 
        
    def update(self):
        pantalla = pygame.display.get_surface()
        self.rect.y += 6
        if self.rect.y > pantalla.get_height():
            self.kill()       
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
    
        