import pygame
from tools import *

FLOAT_DISPLACEMENT_Y = -4.5
SINK_DISPLACEMENT_Y = 1
SINK_ACCELERATION = 0.5
MOVE_DISPLACEMENT_X = 3

class Guppy(pygame.sprite.Sprite):
    def __init__(self, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('guppy.png')
        self.image_right = self.image
        self.image_left = pygame.transform.flip(self.image, True, False)
        self.deadImage = load_image('dead_guppy.png')
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-4, -4)
        self.rect.midbottom = (self.rect.width/2, screen_height)
        
        self.float = False
        self.moveLeft = False
        self.leftFlipped = False
        self.moveRight = False
        self.rightFlipped = True
        self.moveDown = False
        self.sinkingSpeed = SINK_DISPLACEMENT_Y
        
        self.rotation = 0
        
        self.isDead = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, (0,0,255), self.rect, 2)
            
    def move(self, screen_width, screen_height):
        if (self.isDead):
            self.image = self.deadImage
            if self.rect.y > 0:
                self.rect.y -= SINK_DISPLACEMENT_Y
            return
            
        if self.moveLeft:
            if not self.leftFlipped: 
                self.image = self.image_left
                self.rotation *= -1
            self.leftFlipped = True
            self.rightFlipped = False
            if (self.rect.x > 0):
                self.rect.x -= MOVE_DISPLACEMENT_X
        elif self.moveRight:
            if not self.rightFlipped:
                self.image = self.image_right
                self.rotation *= -1
            self.leftFlipped = False
            self.rightFlipped = True
            if (self.rect.x + self.rect.width < screen_width):
                self.rect.x += MOVE_DISPLACEMENT_X
        elif self.moveDown:
            if (self.rect.y + self.rect.height < screen_height):
                self.rect.y += SINK_DISPLACEMENT_Y * 2.5
            
        if (self.float):
            self.sinkingSpeed = SINK_DISPLACEMENT_Y
            self.rotation = 0
            
            if(self.leftFlipped):
                self.image = self.image_left
            else:
                self.image = self.image_right
            if(self.rect.y) > 0:
                self.rect.y += FLOAT_DISPLACEMENT_Y
        elif(self.rect.y + self.rect.height < screen_height):
            if (self.sinkingSpeed < 3):
                self.sinkingSpeed += SINK_ACCELERATION
            self.rect.y += self.sinkingSpeed
            if(self.rightFlipped): 
                if self.rotation > -60:
                    self.rotation -= 2
                self.image = pygame.transform.rotate(self.image_right, self.rotation)
            elif(self.leftFlipped):
                if self.rotation < 60:
                    self.rotation += 2
                self.image = pygame.transform.rotate(self.image_left, self.rotation)
              
    def reset(self, screen_height):
        self.image = load_image('guppy.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.rect.width/2, screen_height)
        
        self.float = False
        self.moveLeft = False
        self.leftFlipped = False
        self.moveRight = False
        self.rightFlipped = True
        self.moveDown = False
        self.sinkingSpeed = SINK_DISPLACEMENT_Y
        
        self.rotation = 0
        
        self.isDead = False
        