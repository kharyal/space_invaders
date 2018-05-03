#handles bullets
import random
import pygame
from aliens import *
from display import *
pygame.init()
pygame.font.init()

bulletfont=pygame.font.SysFont('Comic Sans MS', 40)

class bullets():
    def __init__(self):
        pass

    def setCoordinate(self,coordinatesX,coordinatesY):  #called in board module
        self.coordinatesX=coordinatesX
        self.coordinatesY=coordinatesY

class alien_bullet(bullets):           # alien bullets
    def __init__(self):
        self.symbol="v"
        self.color=(205,9,59)
        self.present=False
    
    def changeCoordinate(self):
        self.coordinatesY+=display_height/160

class simple(bullets):                 # simple bullet
    def __init__(self):            
        self.symbol="^"                # symbol
        self.color=(16, 136, 144)
        self.present=False             # checks if bullet is present currently

    def changeCoordinate(self):        # changes Y coordinate 
        self.coordinatesY-=display_height/80

class tesla(bullets):                  # tesla bullet
    def __init__(self):
        self.symbol="!"
        self.color=(255, 105, 20)
        self.present=False

    def changeCoordinate(self):
        self.coordinatesY-=display_height/160

class mg(bullets):
    def __init__(self):
        self.symbol=".."
        self.color=( 98, 120, 75 )
        self.present=False
    def changeCoordinate(self):
        self.coordinatesY-=display_height/61    
# creating bullet instances and images
mg_bullet=[]
simple_bullet=simple()
simple_img = bulletfont.render(simple_bullet.symbol, False, simple_bullet.color)
tesla_bullet=tesla()
tesla_img=bulletfont.render(tesla_bullet.symbol, False, tesla_bullet.color)
alien_bult=alien_bullet()
alien_img = bulletfont.render(alien_bult.symbol,False,alien_bult.color)
for i in range(0,5):
    mg_bullet.append(mg())
mg_img = bulletfont.render(mg_bullet[0].symbol, False, mg_bullet[0].color)
# draws bullets
def draw_bullets(bullet,type,gameDisplay):
    if type==0:
        gameDisplay.blit(alien_img,(bullet.coordinatesX,bullet.coordinatesY))
    elif type==1:
        gameDisplay.blit(simple_img,(bullet.coordinatesX, bullet.coordinatesY))
    elif type==2:
        gameDisplay.blit(tesla_img,(bullet.coordinatesX, bullet.coordinatesY))
    elif type==3:
        gameDisplay.blit(mg_img,(bullet.coordinatesX, bullet.coordinatesY))
    bullet.changeCoordinate()
    if bullet.coordinatesY<0 or bullet.coordinatesY>display_height:
        bullet.present=False

def set_alien_bult_coordinates(alien_bult):
    global alienlist
    shooter=random.randint(0,len(alienlist[0])-1)
    if alienlist[0][shooter].health>0:
        alien_bult.present=True
        alien_bult.setCoordinate(alienlist[0][shooter].coordinatesX,alienlist[0][shooter].coordinatesY)

# handles collisions
def handle_bullet_collision(bullet,type,ship):
    for j in alienlist:
        for i in j:
            if type==1 or type==3:
                if bullet.present==True and i.health>0 and bullet.coordinatesX-i.coordinatesX<90 and bullet.coordinatesX-i.coordinatesX>0 and bullet.coordinatesY-i.coordinatesY<30 and bullet.coordinatesY-i.coordinatesY>0:
                    bullet.present=False
                    i.health-=1
                    if i.powerupPresent and i.health==0:
                        powerlist[i.poInd].present=True
                        powerlist[i.poInd].setCoordinate(i.coordinatesX,i.coordinatesY)
                    ship.score+=1
                    #print ("Your score = "+str(ship.score))
            if type==2:
                if bullet.present==True and i.health>0 and bullet.coordinatesX-i.coordinatesX<90 and bullet.coordinatesX-i.coordinatesX>0 and bullet.coordinatesY-i.coordinatesY<30 and bullet.coordinatesY-i.coordinatesY>0:
                    if i.hit_type==0:
                        bullet.present=False
                        i.hit_type=2
                        bullet.present=False
            if i.hit_type==2 and i.health>0:
                if i.counter==299:
                    i.health-=1
                    if i.powerupPresent and i.health==0:
                        powerlist[i.poInd].present=True
                        powerlist[i.poInd].setCoordinate(i.coordinatesX,i.coordinatesY)
                    ship.score+=1
                    i.counter=0
                    i.hit_type=0
                    if j.index(i)+1<len(j) and j[j.index(i)+1].health>0:
                        j[j.index(i)+1].health-=1
                        if j[j.index(i)+1].powerupPresent and j[j.index(i)+1].health==0:
                            powerlist[j[j.index(i)+1].poInd].present=True
                            powerlist[j[j.index(i)+1].poInd].setCoordinate(j[j.index(i)+1].coordinatesX,j[j.index(i)+1].coordinatesY)
                        ship.score+=1
                    if j.index(i)-1>=0 and j[j.index(i)-1].health>0:
                        j[j.index(i)-1].health-=1
                        if j[j.index(i)-1].powerupPresent and j[j.index(i)-1].health==0:
                            powerlist[j[j.index(i)-1].poInd].present=True
                            powerlist[j[j.index(i)+1].poInd].setCoordinate(j[j.index(i)+1].coordinatesX,j[j.index(i)+1].coordinatesY)
                        ship.score+=1
                    #print ("Your score = "+str(ship.score))
                i.counter=(i.counter+1)%300
    if type==0:
        i=ship
        if bullet.present==True and bullet.coordinatesX-i.coordinates[0]<90 and bullet.coordinatesX-i.coordinates[0]>0 and i.coordinates[1]-bullet.coordinatesY<30 and i.coordinates[1]-bullet.coordinatesY>0:
            i.health-=1
            bullet.present=False
            