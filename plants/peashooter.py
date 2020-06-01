import pygame
from bullet import Bullet
class Peashooter(pygame.sprite.Sprite):
    def __init__(self):
        super(Peashooter, self).__init__()
        self.images=[pygame.image.load('images/plants/Peashooter/Peashooter_{:d}.png'.format(i)).convert_alpha() for i in range(13)]
        self.rect=self.images[0].get_rect()
        self.zone=(0,0)
        self.blood = 50
        self.isLive = True

    def shot(self):

        return Bullet(self)

