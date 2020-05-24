
import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self,plant):
        super(Bullet, self).__init__()
        self.image=pygame.image.load('images/bullets/peaBullet.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.left=plant.zone[0]+35
        self.rect.top=plant.zone[1]
        self.speed=15
        self.status=True
        self.attact=1

    def move(self):
        if self.rect.left<1200:
            self.rect.left+=self.speed
        else:
            self.status=False

    def hit(self,enemyList):
        for enemy in enemyList:
            if  pygame.sprite.collide_circle_ratio(0.5)(enemy,self):
                # print('hit zombie')

                enemy.blood-=self.attact
                if enemy.blood==0:
                    enemy.islive=False
                self.status=False