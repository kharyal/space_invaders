
import pygame
from aliens import *
pygame.init()
pygame.font.init()
pygame.init()
pygame.font.init()
def changelevel(level,alienlist,level_change,ship):
    level+=1
    if level==2:
        alienlist[0].clear()
        p=0
        for i in range(0,6):
            alienlist[0].append(aliens2())
            alienlist[0][i].setCoordinate(100+i*90,30)

        for i in range(0,3):
            alienlist[1].append(aliens2())
            alienlist[1][p].setCoordinate(100+p*90,0)
            p+=1
            alienlist[1].append(aliens1())
            alienlist[1][p].setCoordinate(100+p*90,0)
            p+=1
        for i in range(0,6):
            alienlist[2].append(aliens1())
            alienlist[2][i].setCoordinate(100+i*90,-30)
    if level==3:
        ship.crashed=True
    return level




