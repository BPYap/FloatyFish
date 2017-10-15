import os
import sys
import pygame
from pygame.locals import *
   
def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)
    
def load_image(name, colorkey=None):
    full_path = resource_path(os.path.join('resources', name))
    try: 
        image = pygame.image.load(full_path)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image.convert_alpha()
    
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
        
    full_path = os.path.join('resources', name)
    try:
        sound = pygame.mixer.Sound(full_path)
    except pygame.error, messaage:
        print 'Cannot load sound:', name
        raise SystemExit, message
    return sound
