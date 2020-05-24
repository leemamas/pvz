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
        self.stop=False
        self.kill=1
        self.old=0  #原始形象

    def move(self):
        if not self.stop:
            self.rect.left-=self.speed

    #改变形象
    def changimage(self):
        if self.old==0:
            self.images = [pygame.image.load('images/Zombie/Zombie_{:d}.png'.format(i)).convert_alpha() for i in
                           range(22)]
        #吃花
        elif self.old==1:
            self.images = [pygame.image.load('images/ZombieAttack/ZombieAttack_{:d}.png'.format(i)).convert_alpha() for i in range(21)]

        #other
        else:
            pass

    #攻击
    def attack(self,enemyList):
        for enemy in enemyList:
            enemy.rect.left,enemy.rect.top=enemy.zone
            if  pygame.sprite.collide_circle_ratio(0.5)(enemy,self):
                # print('hit')

                #碰撞停止行进
                self.stop=True
                #改变僵尸吃花朵的形象
                self.old=1

                #攻击
                print(enemy.blood)
                enemy.blood-=self.kill
                if enemy.blood==0:
                    enemy.isLive=False
                    #消灭花朵后继续行进
                    self.stop=False
                    #变回原来的形象
                    self.old=0






