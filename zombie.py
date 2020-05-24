import pygame
class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super(Zombie, self).__init__()
        self.images=[pygame.image.load('images/Zombie/Zombie_{:d}.png'.format(i)).convert_alpha() for i in range(22)]
        self.rect=self.images[0].get_rect()
        self.rect.left=1000
        self.rect.top=200
        self.speed=1
        self.blood=3
        self.islive=True

    def move(self):
        self.rect.left-=self.speed

