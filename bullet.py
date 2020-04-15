
import pygame
class Bullet:
    def __init__(self,plant):
        self.image=pygame.image.load('images/bullets/peaBullet.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.left=plant.zone[0]+35
        self.rect.top=plant.zone[1]
        self.speed=15
        self.status=True

    def move(self):
        if self.rect.left<1200:
            self.rect.left+=self.speed
        else:
            self.status=False