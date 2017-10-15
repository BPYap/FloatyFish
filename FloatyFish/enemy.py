import pygame
from tools import *

SINK_DISPLACEMENT_Y = 1
defined_enemy_left = 710
defined_enemy_right = 930
MOVE_DISPLACEMENT_X = 2
defined_octopus_top = 160
defined_octupos_btm = 390
MOVE_DISPLACEMENT_Y = 3.5

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=load_image('enemy.png')
        self.deadImage=load_image('dead_enemy.png')
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.leftFlipped=False
        self.moveRight=False
        self.rightFlipped=True
        self.isDead=False
		
    def draw(self,surface):
        surface.blit(self.image,self.rect)
		
    def move(self):
        if(self.isDead):
            self.image=self.deadImage
            if self.rect.y>0:
                self.rect.y-=SINK_DISPLACEMENT_Y
            return

        if self.rightFlipped:
            self.leftFlipped=False
            if (self.rect.x > defined_enemy_right):
                self.image = pygame.transform.flip(self.image, True, False)
                self.leftFlipped = True
                self.rightFlipped = False
            else:
                self.rect.x += MOVE_DISPLACEMENT_X

        elif self.leftFlipped:
            self.rightFlipped=False
            if(self.rect.x < defined_enemy_left):
                self.image = pygame.transform.flip(self.image, True, False)
                self.rightFlipped = True
                self.leftFlipped = False
            else:
                self.rect.x -= MOVE_DISPLACEMENT_X
                
    def reset(self, x, y):
        self.image=load_image('enemy.png')
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.leftFlipped=False
        self.moveRight=False
        self.rightFlipped=True
        self.isDead=False

class Octopus(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=load_image('jellyfish.png')
        self.deadImage=load_image('dead_jellyfish.png')
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.movedown=True
        self.isDead=False
        
    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def reset(self,x,y):
        self.image=load_image('jellyfish.png')
        self.deadImage=load_image('dead_jellyfish.png')
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.movedown=True
        self.isDead=False
        
    def move(self):
        if(self.isDead):
            self.image=self.deadImage
            if self.rect.y>0:
                self.rect.y-=SINK_DISPLACEMENT_Y
            return
        
        if(self.movedown):
            if(self.rect.y<defined_octupos_btm):
                self.rect.y += MOVE_DISPLACEMENT_Y
            else:
                self.movedown=False
        else:
            if(self.rect.y>defined_octopus_top):
                self.rect.y -= MOVE_DISPLACEMENT_Y
            else:
                self.movedown=True
