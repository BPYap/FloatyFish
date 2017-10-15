import pygame, sys
from pygame.locals import *
import obstacle

pygame.init()

gamewidth=1164
gameheight=600
widthoflevel=100
widthofway=80
widthofwall=widthoflevel-widthofway

windowSurface = pygame.display.set_mode((gamewidth,gameheight))
pygame.display.set_caption("Rampage!")

BLACK = (0, 0, 0)
OBSTACLESCOLOR = (48, 2, 2)
RED = (255, 0, 0)
TRANSOBSTACLESCOLOR = (181, 5, 5)
BLUE = (0, 0, 255)

obstacles = []
def addobstacle(x,y,width,height,color,ishidden=False):
    global obstacles
    obstacles.append(obstacle.Obstacle(x,y,width,height,color,ishidden))

windowSurface.fill(BLACK)

#100 as one level,50/100 is wall
#level 1
addobstacle(0,gameheight-150,widthofwall,100,OBSTACLESCOLOR)
addobstacle(widthofway,280,widthofwall,100,OBSTACLESCOLOR)
addobstacle(widthofway,11,widthofwall,100,OBSTACLESCOLOR)
addobstacle(widthoflevel-5,380,5,gameheight-380,OBSTACLESCOLOR)
addobstacle(widthofway,210,widthofwall,70,TRANSOBSTACLESCOLOR,True)
addobstacle(widthofway,0,widthofwall,30,OBSTACLESCOLOR)
#level 2
level2way=widthoflevel+widthofway
addobstacle(level2way,0,widthofwall,200,OBSTACLESCOLOR)
addobstacle(level2way,gameheight-180,widthofwall,141,OBSTACLESCOLOR)
addobstacle(widthoflevel,300,widthoflevel,100,TRANSOBSTACLESCOLOR,True)
#level 3
level3way=widthoflevel*2+widthofway
addobstacle(level3way,150,widthofwall,250,OBSTACLESCOLOR)
addobstacle(level3way,0,widthofwall,100,TRANSOBSTACLESCOLOR,True)
addobstacle(level3way,400,widthofwall,140,TRANSOBSTACLESCOLOR,True)
#level 4
level4way=widthoflevel*3+widthofway
level4trick=20
addobstacle(level4way,450,widthofwall,gameheight-450,OBSTACLESCOLOR)
addobstacle(level4way-level4trick,360,widthofwall+level4trick,90,TRANSOBSTACLESCOLOR,True)
addobstacle(level4way,0,widthofwall,150,OBSTACLESCOLOR)
#level 5
level5way=widthoflevel*4+widthofway
addobstacle(level5way,0,widthofwall,250,OBSTACLESCOLOR)
addobstacle(level5way,350,widthofwall,150,OBSTACLESCOLOR)
#level 6
level6way=widthoflevel*5+widthofway
addobstacle(level6way,300,widthofwall,70,TRANSOBSTACLESCOLOR,True)
addobstacle(level6way,0,widthofwall,220,TRANSOBSTACLESCOLOR,True)
addobstacle(level6way,370,widthofwall,150,OBSTACLESCOLOR)
#level 7
level7way=widthoflevel*6+widthofway
addobstacle(level7way,80,widthofwall,gameheight-80,OBSTACLESCOLOR)
#level 8
level8way=widthoflevel*7+widthofway
level8trick=20
addobstacle(level8way,0,widthofwall,150,OBSTACLESCOLOR)
#addobstacle(level8way)
addobstacle(level8way-level8trick,370,widthofwall+level8trick,150,OBSTACLESCOLOR)
#level 9
level9way=widthoflevel*8+widthofway
addobstacle(level9way,100,widthofwall,50,OBSTACLESCOLOR)
#addobstacle(level9way-widthofway,130,widthofway,20,TRANSOBSTACLESCOLOR,True)
#addobstacle(level9way,150,widthofwall,180,TRANSOBSTACLESCOLOR,True)
#addobstacle(level9way-widthofway,330,widthofway,40,TRANSOBSTACLESCOLOR,True)
addobstacle(level9way,500,widthofwall,100,OBSTACLESCOLOR)
#level 10
level10way=widthoflevel*9+widthofway
addobstacle(level10way,130,widthofwall,gameheight-130,OBSTACLESCOLOR)
addobstacle(level10way,0,widthofwall,50,OBSTACLESCOLOR)
#final
final=widthoflevel*10+widthofway
addobstacle(final-widthofway,130,widthofway,30,TRANSOBSTACLESCOLOR,True)
addobstacle(final,300,gamewidth-final,200,TRANSOBSTACLESCOLOR,True)
addobstacle(final,500,gamewidth-final,20,OBSTACLESCOLOR)


# for ob in obstacles:
    # ob.draw(windowSurface)

# pygame.display.update()

# while True:
    # for event in pygame.event.get():
        # if event.type == QUIT:
            # pygame.quit()
            # sys.exit()
            
            
