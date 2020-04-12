import pygame, sys
from plants.peashooter import Peashooter
from plants.sunflower import SunFlower
from plants.wallnut import WallNut
from plants.sun import Sun

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
    pygame.time.set_timer(SUN_EVENT,1000)

    while 1:

        block.tick(30)

        # 鼠标点击（0，0，0）（1，0，0）
        press = pygame.mouse.get_pressed()
        # 坐标
        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type==SUN_EVENT:
                sun=Sun()
                sunList.append(sun)

            if event.type == pygame.MOUSEMOTION:
                # print(x,y)
                if not is_pick:
                    if 330 <= x <= 330 + card.get_rect().width and 10 <= y <= 10 + card.get_rect().height:
                        if press[0]:
                            p = Peashooter()
                            clickimage.append(p)
                            pick_type = 'pea'
                            is_pick = True

                    if 400 <= x <= 400 + card1.get_rect().width and 10 <= y <= 10 + card1.get_rect().height:
                        if press[0]:
                            sunflower = SunFlower()
                            clickimage.append(sunflower)
                            pick_type = 'flower'
                            is_pick = True


                    #是否点击了太阳
                    for sun in sunList:
                        if sun.rect.collidepoint((x,y)):
                            if press[0]:
                                #点击了太阳消失
                                sunList.remove(sun)
                                #收集了太阳加分
                                global sunnum,font,fontImg
                                sunnum=str(int(sunnum)+25)
                                fontImg = font.render(sunnum, True, (0, 0, 0))

                if is_pick :
                    # 330 180  405 274
                    if not is_plant:
                        if 330 <= x <= 405 and 180 <= y <= 274:
                            if pick_type == 'pea':
                                p = Peashooter()
                                p.zone = (330, 180)
                                p1.append(p)
                                if press[0]:
                                    peaList.append(p)
                                    clickimage.clear()
                                    p1.clear()
                                    is_pick = False
                                    is_plant=True
                            elif pick_type == 'flower':
                                f = SunFlower()
                                f.zone = (330, 180)
                                p1.append(f)
                                if press[0]:
                                    sunFlowerList.append(f)
                                    clickimage.clear()
                                    p1.clear()
                                    is_pick = False
                                    is_plant = True

                    else:
                        p1.clear()

                    if press[2]:
                        clickimage.clear()
                        is_pick = False

        # 绘制背景
        screen.blit(backgroup, (0, 0))
        # 卡槽
        screen.blit(card_slot, (250, 0))
        # card
        screen.blit(card, (330, 10))
        screen.blit(card1, (400, 10))
        # sunnum
        screen.blit(fontImg, (280, 60))



        if index > 13:
            index = 0
        # screen.blit(peashooter.images[index % 13], peashooter.rect)
        # screen.blit(sunflower.images[index % 18], sunflower.rect)
        # screen.blit(wallnut.images[index % 16], wallnut.rect)

        for image in clickimage:
            screen.blit(image.images[0], (x, y))
        for p in p1:
            screen.blit(p.images[0], p.zone)
        for pea in peaList:
            screen.blit(pea.images[index % 13], pea.zone)
        for sunFlower in sunFlowerList:
            screen.blit(sunFlower.images[index % 18], sunFlower.zone)
        for sun in sunList:
            screen.blit(sun.images[index % 22], sun.rect)
            sun.down()


        pygame.display.update()



        index += 1


if __name__ == '__main__':
    main()
