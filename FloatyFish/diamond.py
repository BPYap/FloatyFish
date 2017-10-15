import pygame
from tools import *

class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('diamond.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        self.isEaten = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, (0,0,255), self.rect, 2)
        
    def eaten(self):
        if self.isEaten == False:
            self.isEaten = True
              
    def reset(self):
        self.isEaten = False
        