
import pygame
from aliens import *
import random
pygame.init()
pygame.font.init()
pygame.init()
pygame.font.init()
from display import *
from powerups import *
def changelevel(level,alienlist,level_change,ship):
    alienSpeed=origSpeed
    level+=1
    if level == 1:
        powerlist.clear()
        alienlist[0].clear()
        p=0
        for i in range (0,7):
            alienlist[0].append(aliens1())
            alienlist[0][p].setCoordinate(100+p*90,30)
            p+=1
        for i in alienlist:
            for j in i:
                randnum=random.randint(1,101)
                if randnum%4==0:
                    #print(i.index(j))
                    j.powerupPresent=True
                    potype=random.randint(0,ponumber)
                    if potype==0:
                        j.poInd=len(powerlist)
                        po=hp()
                        po.setCoordinate(j.coordinatesX,j.coordinatesY)
                        powerlist.append(po)
                    elif potype==1:
                        j.poInd=len(powerlist)                
                        po=machineGun()
                        po.setCoordinate(j.coordinatesX,j.coordinatesY)                
                        powerlist.append(po)
                    elif potype==2:
                        j.poInd=len(powerlist)
                        po=danger()
                        po.setCoordinate(j.coordinatesX,j.coordinatesY)
                        powerlist.append(po)
                    elif potype==3:
                        j.poInd=len(powerlist)
                        po=freeze()
                        po.setCoordinate(j.coordinatesX,j.coordinatesY)
                        powerlist.append(po)
                    #print(j.poInd)
                    #print(len(powerlist))
        for i in powerlist:
            i.resize(int(display_height))
    if level==2:
        powerlist.clear()
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

        for i in alienlist:
            for j in i:
                randnum=random.randint(1,101)
                if randnum%4==0:
                    #print(i.index(j))
                    j.powerupPresent=True
                    potype=random.randint(0,ponumber)
                    if potype==0:
                        j.poInd=len(powerlist)
                        po=hp()
                        po.setCoordinate(j.coordinatesX,j.coordinatesY)
                        powerlist.append(po)
                    elif potype==1:
                        j.poInd=len(powerlist)                
                        po=machineGun()
                        po.setCoordinate(j.coordinatesX,j.coordinatesY)                
                        powerlist.append(po)
                    elif potype==2:
                        j.poInd=len(powerlist)
                        po=danger()
                        po.setCoordinate(j.coordinatesX,j.coordinatesY)
                        powerlist.append(po)
                    elif potype==3:
                        j.poInd=len(powerlist)
                        po=freeze()
                        po.setCoordinate(j.coordinatesX,j.coordinatesY)
                        powerlist.append(po)
                    #print(j.poInd)
                    #print(len(powerlist))
        for i in powerlist:
            i.resize(int(display_height))

    if level==3:
        ship.crashed=True
    return level




