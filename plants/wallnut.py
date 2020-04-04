import pygame
#¼á¹ûÇ½
class WallNut:
    def __init__(self):
        self.images=[pygame.image.load('images/plants/WallNut/WallNut_{:d}.png'.format(i)).convert_alpha() for i in range(16)]
        self.rect=self.images[0].get_rect()
        self.rect.left,self.rect.top=200,200

