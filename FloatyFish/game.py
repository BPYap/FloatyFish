import sys
import pygame
from pygame.locals import *

from tools import *

import guppy
import enemy
import map
import diamond

S_WIDTH = 1164
S_HEIGHT = 600
CAPTION = "Floaty Fish"
MOUSE_VISIBLE = False
GAME_OVER_DELAY = 45 

if not pygame.mixer: print 'Sound module is missing.'

pygame.init()
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT)) 
pygame.display.set_caption(CAPTION) 
pygame.mouse.set_visible(MOUSE_VISIBLE)

background = pygame.Surface(screen.get_size()).convert()
background.fill((0,0,0))
background_image = load_image('background.png')
start_bg = load_image("start.png")
game_over_bg = load_image("game_over.png")
victory_bg = load_image("victory.png")
background.blit(background_image, (0, 0))

# Loading Screen    
screen.blit(background, (0,0))
pygame.display.flip()
    
# pygame.mixer.music.load('resources/background.wav')
# if config.play_sound:
    # pygame.mixer.music.play(-1)
    
# error_sound = load_sound('error.wav')
# error_sound.set_volume(0.2)

# Class instantiation
start = True
game_over = False
game_over_delay = GAME_OVER_DELAY
victory = False

guppy = guppy.Guppy(S_HEIGHT)
octopus = enemy.Octopus(380,170)
enemy = enemy.Enemy(730, 200)
diamond = diamond.Diamond(S_WIDTH-45, S_HEIGHT-50)

clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_SPACE:
                if start:
                    start = False
                else:
                    guppy.float = True
            elif event.key == K_RIGHT:
                guppy.moveRight = True
            elif event.key == K_LEFT:
                guppy.moveLeft = True
            elif event.key == K_DOWN:
                guppy.moveDown = True
            elif event.key == K_r and (guppy.isDead or victory):
                guppy.reset(S_HEIGHT)
                enemy.reset(730,200)
                diamond.reset()
                game_over = False
                game_over_delay = GAME_OVER_DELAY
                victory = False
            # elif event.key == ord('c'):
                # background.fill((0,0,0))
            # elif event.key == ord('d'):
                # DEBUG_MODE = not DEBUG_MODE
                # if not DEBUG_MODE:
                    # background.fill((0,0,0))
            # elif event.key == ord('m'):
                # config.play_sound = not config.play_sound
                # if config.play_sound:
                    # pygame.mixer.music.play(-1)
                # else:
                    # pygame.mixer.music.stop()
                
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                guppy.moveRight = False
            elif event.key == K_LEFT:
                guppy.moveLeft = False
            elif event.key == K_DOWN:
                guppy.moveDown = False
            elif event.key == K_SPACE:
                guppy.float = False
    guppy.move(S_WIDTH, S_HEIGHT)
    octopus.move()
    enemy.move()
    
    for ob in map.obstacles:
        if guppy.rect.colliderect(ob.rect):
            guppy.isDead = True
            ob.ishidden = False
            game_over = True
    
    if guppy.rect.colliderect(enemy.rect):
        guppy.isDead = True
        enemy.isDead = True
        game_over = True
    elif guppy.rect.colliderect(octopus.rect):
        guppy.isDead = True
        game_over = True
    elif guppy.rect.colliderect(diamond.rect):
        diamond.eaten()
        victory = True
    
    
    screen.blit(background, (0,0))
    
    for ob in map.obstacles:
        ob.draw(screen)
        
    guppy.draw(screen)
    octopus.draw(screen)
    enemy.draw(screen)
    if diamond.isEaten == False:
        diamond.draw(screen)
    
    if start:
        screen.blit(start_bg, (0,0))
    elif game_over:
        if game_over_delay == 0:
            screen.blit(game_over_bg, (0,0))
        else:
            game_over_delay -= 1
    elif victory:
        screen.blit(victory_bg, (0,0))
        
    pygame.display.flip()
    
    clock.tick(60)
    
        
        
        
        
        
        
        
        
        

