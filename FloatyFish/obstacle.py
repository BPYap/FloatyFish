import pygame

class Obstacle(object):
    def __init__(self,x,y,width,height,color,ishidden=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.surface = pygame.Surface((width,height))
        self.surface.fill(color)
        self.ishidden = ishidden
        
    def draw(self,surface):
        if self.ishidden==True:
            self.surface.set_alpha(0)
        else:
            self.surface.set_alpha(240)
        surface.blit(self.surface,self.rect)
		


        

