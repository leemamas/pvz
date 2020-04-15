import pygame
from bullet import Bullet
class Peashooter:
    def __init__(self):
        # self.image=pygame.image.load('images/plants/Peashooter/Peashooter_0.png').convert_alpha()
        self.images=[pygame.image.load('images/plants/Peashooter/Peashooter_{:d}.png'.format(i)).convert_alpha() for i in range(13)]
        self.rect=self.images[0].get_rect()
        self.zone=(0,0)

    def shot(self):

        return Bullet(self)

