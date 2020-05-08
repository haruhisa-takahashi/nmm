import pygame
import sys
import os

# プログラミングは、思った通りに動けばオッケー！！！

MARIO_IMG = "resources/marios.png"
BLOCK_IMG = "resources/tiles.png"
BG_IMG = "resources/stage.png"

W = 800
H = 600
TI = "NMM"
MAGNI = 2.69
SPEED = 3
MARIO_X = 128
MARIO_Y = 10
MARIO_W = 32
MARIO_H = 32



class MarioMaker:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption(TI)
        self.background = self.set_background(BG_IMG)
        clock = pygame.time.Clock()
        self.mario_sheet = self.load_image(MARIO_IMG)
        self.mario = Mario(self)
        self.all = pygame.sprite.Group()
        self.all.add(self.mario)
        while True:
            clock.tick(60)
            self.event_handler()
            self.update()
            self.draw()

    def set_background(self, image):
        background = pygame.image.load(image).convert()
        bg_rect = background.get_rect()
        fixed_background = pygame.transform.scale(background, (int(bg_rect.width * MAGNI), int(bg_rect.height * MAGNI)))
        return fixed_background
    
    def load_image(self, filename):
        self.spritesheet = SpriteSheet(filename)
        return SpriteSheet(filename)
    
    def create_blocks(self):
        pass

    def event_handler(self):
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

        self.screen.blit(self.background, (0,0))
        self.all.draw(self.screen)
        pygame.display.flip()


class Mario(pygame.sprite.Sprite):
    def __init__(self, mariomaker):
        pygame.sprite.Sprite.__init__(self)
        self.mariomaker = mariomaker
        self.image = self.mariomaker.mario_sheet.get_image(178, 32, 12, 16)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = MARIO_X
        self.rect.y = MARIO_Y
        self.vx = 0
        self.vy = 0
        self.width = self.rect.width
        self.height = self.rect.height
        self.on_floor = False
        self.mario_r = self.image
        self.mario_l = pygame.transform.flip(self.image, True, False)

    def update(self):
        pk = pygame.key.get_pressed()
        if pk[pygame.K_RIGHT]:
            self.vx = SPEED
            self.image = self.mario_r
        elif pk[pygame.K_LEFT]:
            self.vx = -SPEED
            self.image = self.mario_l
        else:
            self.vx = 0
        
        #サービスサービス
        if pk[pygame.K_UP]:
            self.vy = -SPEED
        elif pk[pygame.K_DOWN]:
            self.vy = SPEED
        else:
            self.vy = 0

        self.rect.x += self.vx
        self.rect.y += self.vy



class SpriteSheet():
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert_alpha()
    
    def get_image(self, x,y,w,h):
        image = pygame.Surface((w,h))
        image.blit(self.spritesheet,(0,0),(x,y,w,h))
        image = pygame.transform.scale(image, (MARIO_W, MARIO_H))
        return image

class BackGround(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        

MarioMaker()