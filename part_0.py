import pygame
import sys
import os

# プログラミングは、思った通りに動けばオッケー！！！
# スクリーンを表示しよう！

# その１
WIDTH = 800
# その２
HEIGHT = 600
# その３
TITLE = "NANCHATTE MARIO MAKER"
# その５
#SC = (,,)

class MarioMaker:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.key_handler()
            self.update()
            self.draw()
    
    def key_handler(self):
        for dondokodon in pygame.event.get():
            if dondokodon.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def update(self):
        pass

    def draw(self):
        # その４
        #self.screen.fill(SC)
        pygame.display.flip()

MarioMaker()