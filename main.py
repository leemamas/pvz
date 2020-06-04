import pygame, sys
from plants.peashooter import Peashooter
from plants.sunflower import SunFlower
from plants.wallnut import WallNut
from plants.sun import Sun
from zone import Zone
from zombie import Zombie
# 这初始化

pygame.init()

# 窗体大小
screen_size = (1200, 600)
screen = pygame.display.set_mode(screen_size)
# 窗体名称
pygame.display.set_caption('pvz')
# 背景
bg_path = 'images/Background.jpg'
backgroup = pygame.image.load(bg_path).convert()
# 卡槽
card_slot = pygame.image.load('images/cardSlot.png').convert()
# card
card = pygame.image.load('images/cards/card_peashooter.png').convert()
card1 = pygame.image.load('images/cards/card_sunflower.png').convert()
card_rect = card.get_rect()
card1_rect = card1.get_rect()
scale = 0.78
card = pygame.transform.scale(card, (int(card_rect.width * scale), int(card_rect.height * scale)))
card1 = pygame.transform.scale(card1, (int(card1_rect.width * scale), int(card1_rect.height * scale)))
# 阳光数
sunnum = '100'
font = pygame.font.SysFont('arial', 20)
fontImg = font.render(sunnum, True, (0, 0, 0))


# 主函数
def main():
    block = pygame.time.Clock()
    # peashooter = Peashooter()
    # 点击存放卡片的图像
    clickimage = []
    # 临时存放pea
    p1 = []
    peaList = []
    # sunflower=SunFlower()
    sunFlowerList = []
    zombieList=[]
    zombie=Zombie()
    zombieList.append(zombie)

    #僵尸的敌人
    enemy_zombie_list=[]

    #花朵产生的太阳列表
    flower_product_list=[]

    wallnut = WallNut()
    sunList=[]
    index = 0
    # 是否点击了卡片
    is_pick = False
    pick_type = None
    #区域是否种植了植物
    is_plant=False
    #太阳下落的时间
    SUN_EVENT=pygame.USEREVENT+1
    pygame.time.set_timer(SUN_EVENT,5000)

    # #花朵产能事件
    # FLOWER_PRODUCT_SUM_EVENT=pygame.USEREVENT+1
    # #这是1秒，改5
    # pygame.time.set_timer(FLOWER_PRODUCT_SUM_EVENT,5000)


    z=Zone()
    bulletList=[]

    while 1:

        block.tick(30)

        # 鼠标点击（0，0，0）（1，0，0）
        press = pygame.mouse.get_pressed()
        # 坐标
        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #太阳下落
            if event.type==SUN_EVENT:
                sun=Sun()
                #这个是下落的太阳
                sunList.append(sun)

            # #PRODUCT SUM BY FLOWER
            # if event.type==FLOWER_PRODUCT_SUM_EVENT:
            #     for flower in sunFlowerList:
            #         #没有生太阳时
            #         if not flower.isProductSum:
            #             #产能
            #             sun = Sun()
            #             #太阳的位置
            #             sun.rect.left,sun.rect.top=flower.rect.left,flower.rect.top
            #             #属于谁？
            #             sun.belong=flower
            #             flower_product_list.append(sun)
            #             flower.isProductSum=True




            if event.type == pygame.MOUSEMOTION:

                # if z.is_card_slot_zone(x,y,card_slot.get_rect().width,card_slot.get_rect().height):
                #     print('cardslot zone!')
                # elif z.is_plant_zone(x,y):
                #     # print('plant zone !')
                #     print(z.getIndex(x,y))
                # else:
                #     print('other zone!')
                #没有点击卡片
                if not is_pick:
                    if press[0]:
                        if 330 <= x <= 330 + card.get_rect().width and 10 <= y <= 10 + card.get_rect().height:
                                p = Peashooter()
                                clickimage.append(p)
                                pick_type = 'pea'
                                is_pick = True

                        if 400 <= x <= 400 + card1.get_rect().width and 10 <= y <= 10 + card1.get_rect().height:
                                sunflower = SunFlower()
                                clickimage.append(sunflower)
                                pick_type = 'flower'
                                is_pick = True
                else :
                    if z.is_plant_zone(x,y):
                        if z.getIndex(x,y) and not is_plant:
                            if pick_type == 'pea':
                                p = Peashooter()
                                a,b=z.getIndex(x,y)
                                # print(z.getIndex(x,y))
                                p.zone=z.getGridPos(a,b)
                                # print('==p==',a,b)
                                #没有种植物
                                if  z.plantInfo[b][a]==0:
                                    p1.append(p)
                                    is_plant=True

                                    if press[0] :
                                        peaList.append(p)
                                        enemy_zombie_list.append(p)
                                        # bullet=p.shot()
                                        # bulletList.append(bullet)
                                        clickimage.clear()
                                        p1.clear()
                                        is_pick = False
                                        z.plantInfo[b][a]=1

                            elif pick_type == 'flower':
                                f = SunFlower()
                                a, b = z.getIndex(x, y)
                                f.zone = z.getGridPos(a, b)
                                # print('==f==', a, b)
                                if  z.plantInfo[b][a]==0:
                                    p1.append(f)
                                    is_plant = True
                                    if press[0]:
                                        sunFlowerList.append(f)
                                        enemy_zombie_list.append(f)
                                        clickimage.clear()
                                        p1.clear()
                                        is_pick = False
                                        z.plantInfo[b][a] = 1
                        else:
                            p1.clear()
                            is_plant=False


                    if press[2]:
                        is_pick = False
                        clickimage.clear()
                        p1.clear()
                        is_plant = False



                #是否点击了下落太阳
                for sun in sunList:
                    if sun.rect.collidepoint((x,y)):
                        if press[0]:
                            #点击了太阳消失
                            sunList.remove(sun)
                            #收集了太阳加分
                            global sunnum,font,fontImg
                            sunnum=str(int(sunnum)+25)
                            fontImg = font.render(sunnum, True, (0, 0, 0))

                # 是否点击了下落太阳
                for sun in flower_product_list:
                    if sun.rect.collidepoint((x, y)):
                        if press[0]:
                            # 点击了太阳消失
                            flower_product_list.remove(sun)
                            # 收集了太阳加分
                            sunnum = str(int(sunnum) + 25)
                            fontImg = font.render(sunnum, True, (0, 0, 0))

                            sun.belong.isProductSum=False




        # 绘制背景
        screen.blit(backgroup, (0, 0))
        # 卡槽
        screen.blit(card_slot, (250, 0))
        # card
        screen.blit(card, (330, 10))
        screen.blit(card1, (400, 10))
        # sunnum
        screen.blit(fontImg, (280, 60))


        if index > 23:
            index = 0
        # screen.blit(peashooter.images[index % 13], peashooter.rect)
        # screen.blit(sunflower.images[index % 18], sunflower.rect)
        # screen.blit(wallnut.images[index % 16], wallnut.rect)

        #它是不断产生？？
        #它是重叠起来看不出，其实是一直产生的，我们要控制它生成1个，
        # print('listlen:',len(flower_product_list))

        for image in clickimage:
            screen.blit(image.images[0], (x, y))
        for p in p1:
            screen.blit(p.images[0], p.zone)
        #豌豆
        for pea in peaList:
            if pea.isLive:
                if index%99==1:
                    bullet = pea.shot()
                    bulletList.append(bullet)
                screen.blit(pea.images[index % 13], pea.zone)
            else:
                peaList.remove(pea)
                enemy_zombie_list.remove(pea)
        #太阳花
        # print('产出的能量数量',len(flower_product_list))
        for sunFlower in sunFlowerList:
            if sunFlower.isLive:

                screen.blit(sunFlower.images[index % 18], sunFlower.zone)
                # print('{},位置的花朵,是否产出了太阳{},速率{}'.format(sunFlower.zone,sunFlower.isProductSum,sunFlower.product_sun_rate))
                if not sunFlower.isProductSum:
                    sunFlower.product_sun_rate+=1
                    if sunFlower.product_sun_rate==100:
                        sunFlower.productSun(flower_product_list)
                        sunFlower.isProductSum=True
                        sunFlower.product_sun_rate=0

            else:
                sunFlowerList.remove(sunFlower)
                enemy_zombie_list.remove(sunFlower)

        print('num:',len(sunList))
        for sun in sunList:
            screen.blit(sun.images[index % 22], sun.rect)
            sun.down()
            if sun.rect.top>600:
                sunList.remove(sun)
        #花朵生的太阳渲染
        for sun in flower_product_list:
            screen.blit(sun.images[index % 22], sun.rect)

        for bullet in bulletList:
            if bullet.status:
                screen.blit(bullet.image,bullet.rect)
                bullet.move()
                bullet.hit(zombieList)
            else:
                bulletList.remove(bullet)

        #僵尸
        for zombie in zombieList:
            if zombie.islive:
                zombie.changimage()
                screen.blit(zombie.images[index % 21], zombie.rect)
                zombie.move()
                zombie.attack(enemy_zombie_list)
            else:
                zombieList.remove(zombie)


        # print(len(bulletList))
        pygame.display.update()



        index += 1


if __name__ == '__main__':
    main()
