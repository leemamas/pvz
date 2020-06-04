import pygame
from plants.sun import Sun
class SunFlower(pygame.sprite.Sprite):
    def __init__(self):
        super(SunFlower, self).__init__()
        self.images=[pygame.image.load('images/plants/SunFlower/SunFlower_{:d}.png'.format(i)).convert_alpha() for i in range(18)]
        self.rect=self.images[0].get_rect()
        self.rect.left,self.rect.top=200,100
        self.zone=(0,0)
        self.blood=50
        self.isLive=True
        self.isProductSum=False
        #控制生成的速率
        self.product_sun_rate=0


    def productSun(self,list):
        sun = Sun()
        sun.rect.left, sun.rect.top = self.zone
        sun.belong = self
        list.append(sun)
