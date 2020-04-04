import pygame
#Ì«Ñô»¨
class SunFlower:
    def __init__(self):
        self.images=[pygame.image.load('images/plants/SunFlower/SunFlower_{:d}.png'.format(i)).convert_alpha() for i in range(18)]
        self.rect=self.images[0].get_rect()
        self.rect.left,self.rect.top=200,100

