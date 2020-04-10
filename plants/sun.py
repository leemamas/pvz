import pygame
import random
class Sun:
    def __init__(self):
        self.images=[pygame.image.load('images/Sun/Sun_{:d}.png'.format(i)).convert_alpha() for i in range(22)]
        self.rect=self.images[0].get_rect()
        self.rect.left=random.choice([200,300,400])
        self.rect.top=0
        self.speed=5

    def down(self):
        self.rect.top+=self.speed