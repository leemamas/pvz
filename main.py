import pygame, sys
from plants.peashooter import Peashooter
from plants.sunflower import SunFlower
from plants.wallnut import WallNut

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
#卡槽
card_slot=pygame.image.load('images/cardSlot.png').convert()
#card
card=pygame.image.load('images/cards/card_peashooter.png').convert()
card1=pygame.image.load('images/cards/card_sunflower.png').convert()
card_rect=card.get_rect()
card1_rect=card1.get_rect()
scale=0.78
card=pygame.transform.scale(card,(int(card_rect.width*scale),int(card_rect.height*scale)))
card1=pygame.transform.scale(card1,(int(card1_rect.width*scale),int(card1_rect.height*scale)))
#阳光数
sunnum='0'
font=pygame.font.SysFont('arial',20)
fontImg=font.render(sunnum,True,(0,0,0))



# 主函数
def main():
    block = pygame.time.Clock()
    peashooter = Peashooter()
    sunflower=SunFlower()
    wallnut=WallNut()
    index = 0
    while 1:

        block.tick(30)
        # 绘制背景
        screen.blit(backgroup, (0, 0))
        #卡槽
        screen.blit(card_slot, (250, 0))
        #card
        screen.blit(card, (330, 10))
        screen.blit(card1, (400, 10))
        #sunnum
        screen.blit(fontImg, (280, 60))

        if index > 13:
            index = 0
        screen.blit(peashooter.images[index % 13], peashooter.rect)
        screen.blit(sunflower.images[index % 18], sunflower.rect)
        screen.blit(wallnut.images[index % 16], wallnut.rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        index += 1


if __name__ == '__main__':
    main()
