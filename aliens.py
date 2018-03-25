import pygame

pygame.init()
pygame.font.init()

class aliens():
    def __init__(self):
        pass
    # sets coordinates of aliens
    def setCoordinate(self,coordinatesX,coordinatesY):
        self.coordinatesX=coordinatesX
        self.coordinatesY=coordinatesY

    # moves aliens in X direction
    def changeCoordinateX(self,direction):
        if direction == 1:
            self.coordinatesX+=3
        else:
            self.coordinatesX-=3
    
    # moves aliens in Y direction
    def changeCoordinateY(self):
        self.coordinatesY+=25

class aliens1(aliens):
    def __init__(self):
        self.symbol1="_( \ )_"      # these are  the different symbols for aliens
        self.symbol2="_( | )_"
        self.symbol3="_( / )_"
        self.symbol4="_( - )_"
        self.if_tesla1="_(---)_"
        self.if_tesla2="_(|||)_"
        self.health=1               # health of alien
        self.hit_type=0             # type of bullet if hit
        self.counter=0
        self.aliencolor=( 255, 42, 42 )

class aliens2(aliens):
    def __init__(self):
        self.symbol1="__(* *)__"
        self.symbol2="__(- -)__"
        self.symbol3="__(* *)__"
        self.symbol4="__(- -)__"
        self.if_tesla1="_(---)_"
        self.if_tesla2="_(|||)_"
        self.health=3
        self.hit_type=0
        self.counter=0
        self.aliencolor=( 177, 20, 158 )    

alienlist=[[],[],[],[],[],[],[],[],[],[],[]]

p=0

for i in range (0,7):
    alienlist[0].append(aliens1())
    alienlist[0][p].setCoordinate(100+p*90,30)
    p+=1

tes_a_color=( 34, 175, 255 )

mfont = pygame.font.SysFont('Comic Sans MS', 40)
a1t1 = mfont.render(alienlist[0][0].if_tesla1, False, tes_a_color)
a1t2 = mfont.render(alienlist[0][0].if_tesla2, False, tes_a_color)

alien_present=False
# draws aliens
def draw_aliens(count,direction,direction_change,gameDisplay,ship,alien_present,level_change):
    alien_present=False
    for j in alienlist:
        for i in j:
            if i.health>0:
                alien_present=True
                if i.hit_type!=2:
                    s1a1 = mfont.render(i.symbol1, False, i.aliencolor)     
                    s1a2 = mfont.render(i.symbol2, False, i.aliencolor)
                    s1a3 = mfont.render(i.symbol3, False, i.aliencolor)
                    s1a4 = mfont.render(i.symbol4, False, i.aliencolor)
                    if count<10:
                            gameDisplay.blit(s1a1,(i.coordinatesX,i.coordinatesY))
                    elif count>=10 and count<20:
                        gameDisplay.blit(s1a2,(i.coordinatesX,i.coordinatesY))
                    elif count>=20 and count<30:
                        gameDisplay.blit(s1a3,(i.coordinatesX,i.coordinatesY))
                    elif count>=3 and count<40:
                        gameDisplay.blit(s1a4,(i.coordinatesX,i.coordinatesY))
                elif i.hit_type==2:
                    if count%20<10:
                         gameDisplay.blit(a1t1,(i.coordinatesX,i.coordinatesY))
                    else:
                        gameDisplay.blit(a1t2,(i.coordinatesX,i.coordinatesY))
            if (i.coordinatesX>750 or i.coordinatesX<30) and i.health>0:
                direction_change=True
                direction=-1*direction
                
            if i.coordinatesY>700 and i.health>0:
                print("GAME OVER")
                ship.crashed=True

    if not alien_present:
        level_change=True
    if direction_change==True:
        for j in alienlist:
            for i in j:
                i.changeCoordinateY()
        direction_change=False
    for j in alienlist:
        for i in j:
            i.changeCoordinateX(direction)
    return(direction,direction_change,level_change)    
