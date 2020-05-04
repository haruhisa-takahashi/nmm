import pygame
import os
import sys

# プログラミングは、思った通りに動けばオッケー！！！
# スプライトを動かしてみよう！

# MARIOMAKER
WIDTH = 300
HEIGHT = 200
FPS = 60
TITLE = "NANCHATTE MARIO MAKER"
SC = (10,20,40)

# MARIO
SPEED_LR = 10
SPEED_UD = 15
MC = (0,100,100)


class MarioMaker:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        clock = pygame.time.Clock()
        self.all = pygame.sprite.Group()
        mario = Mario()
        self.all.add(mario)
        
        while True:
            clock.tick(FPS)
            self.key_handler()
            self.update()
            self.draw()
    
    def key_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def update(self):
        self.all.update()

    def draw(self):
        self.screen.fill(SC)
        self.all.draw(self.screen)
        pygame.display.flip()


class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill(MC)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.vx = 0
        self.vy = 0
"""
    def update(self):
        pk = pygame.key.get_pressed()

        if pk[pygame.K_RIGHT]:
            self.vx = SPEED_LR
        elif pk[pygame.K_LEFT]:
            self.vx = -SPEED_LR
        elif pk[pygame.K_UP]:
            self.vy = -SPEED_UD
        elif pk[pygame.K_DOWN]:
            self.vy = SPEED_UD
        else:
            self.vx = 0
            self.vy = 0

        self.rect.x += self.vx
        self.rect.y += self.vy
"""

MarioMaker()