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
