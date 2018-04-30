import pygame
from aliens import *
import random
pygame.init()
from display import *
class powerups():
    def __init__(self):
        pass

    def setCoordinate(self,coordinatesX,coordinatesY):  #called in board module
        self.coordinatesX=coordinatesX
        self.coordinatesY=coordinatesY

    def changeCoordinateY(self):
        self.coordinatesY+=3
    
    def resize(self,disp_height):
        self.symbol=pygame.transform.scale(self.symbol,(int(disp_height/30),int(disp_height/30))) 

#health powerup
class hp(powerups):
    def __init__(self):
        self.symbol=pygame.image.load('hpPup.jpg')
        self.present=False
        self.done=False
        self.type=0

class machineGun(powerups):
    def __init__(self):
        self.symbol=pygame.image.load('mgPup.jpg')
        self.present=False
        self.done=False
        self.type=1

class danger(powerups):
    def __init__(self):
        self.symbol=pygame.image.load('dangerPup.png')
        self.present=False
        self.done=False
        self.type=2

for i in alienlist:
    for j in i:
        randnum=random.randint(1,101)
        if randnum%4==0:
            #print(i.index(j))
            j.powerupPresent=True
            potype=random.randint(0,ponumber)
            if potype==0:
                j.poInd=len(powerlist)
                #po=machineGun()
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
                #po=machineGun()
                po=danger()
                po.setCoordinate(j.coordinatesX,j.coordinatesY)
                powerlist.append(po)
            #print(j.poInd)
            #print(len(powerlist))

for i in powerlist:
    i.resize(int(display_height))

def drawPU():
    for i in powerlist:
        if i.present:
            gameDisplay.blit(i.symbol,(i.coordinatesX,i.coordinatesY))
            i.changeCoordinateY()

def handlePUcollisions(ship):
    for i in powerlist:
        if i.present and (((i.coordinatesX-ship.coordinates[0]<display_height/30) and (i.coordinatesX-ship.coordinates[0]>0)) or ((ship.coordinates[0]-i.coordinatesX<90) and (ship.coordinates[0]-i.coordinatesX>0))) and (ship.coordinates[1]-i.coordinatesY<display_height/30) and (ship.coordinates[1]-i.coordinatesY>0):
            i.present=False
            if i.type==0:
                ship.health+=1
            if i.type==1:
                ship.mg=True
            if i.type==2:
                ship.health-=1