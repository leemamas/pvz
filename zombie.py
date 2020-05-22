import pygame
class Zombie:
    def __init__(self):
        self.images=[pygame.image.load('images/Zombie/Zombie_{:d}.png'.format(i)).convert_alpha() for i in range(22)]
        self.rect=self.images[0].get_rect()
        self.rect.left=1000
        self.rect.top=200
        self.speed=5

    def move(self):
        self.rect.left-=self.speed

