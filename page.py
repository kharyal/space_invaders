from display import *
from level1 import *
from aliens import *
from powerups import *
import pygame
import math
pygame.init()
disp_height=display_height
def disp_page(level,count):
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    titlefont = pygame.font.SysFont('Comic Sans MS', 70)
    color=( 55,151,40)
    if level==0:
        title=titlefont.render("SPACE INVADERS",False,color)
        start=myfont.render("start............(s)",False,color)
        instructions=myfont.render("instructons......(i)",False,color)
        quiti=myfont.render("quit................(q)",False,color)
        gameDisplay.blit(title,(display_width/3, display_height/3-100))
        gameDisplay.blit(start,(display_width/3, display_height/3+100))
        gameDisplay.blit(instructions,(display_width/3, display_height/3+200))
        gameDisplay.blit(quiti,(display_width/3, display_height/3+300))
    if level==-1.1:
        title=titlefont.render("BASIC",False,color)
        text=[]
        a=myfont.render("Your space-ship is under attack, save it from aliens!!!",False,color)
        text.append(a)
        a=myfont.render("Move your ship using 'A' and 'D' and shoot bullets with 'W'",False,color)
        text.append(a)
        a=myfont.render("Kill as many aliens as you can and reach the Highest score!!!",False,color)
        text.append(a)
        nextpg=myfont.render("(n) next",False,color)
        prevpg=myfont.render("(q) quit",False,color)
        main=myfont.render("(m) main menu->",False,color)
        gameDisplay.blit(title,(display_width/3, display_height/5))
        ind=0
        for i in text:
            gameDisplay.blit(i,(10, display_height/3+ind*30))
            ind+=1
        text.clear()
        gameDisplay.blit(nextpg,(3*display_width/4, display_height/3+ind*30+5*math.sin(math.radians(count))))
        gameDisplay.blit(prevpg,(display_width/4, display_height/3+ind*30+5*math.sin(math.radians(count))))
        ind+=2
        gameDisplay.blit(main,(2*display_width/5, display_height/3+ind*30+5*math.sin(math.radians(count))))
    if level==-1.2:
        title=titlefont.render("ALIENS",False,color)
        a1=aliens1()
        alien1=myfont.render(a1.symbol1,False,a1.aliencolor)
        alien2=myfont.render(a1.symbol2,False,a1.aliencolor)
        alien3=myfont.render(a1.symbol3,False,a1.aliencolor)
        alien4=myfont.render(a1.symbol4,False,a1.aliencolor)
        
        if count<10:
            gameDisplay.blit(alien1,(display_width/5,display_height/3))
        elif count>=10 and count<20:
            gameDisplay.blit(alien2,(display_width/5,display_height/3))
        elif count>=20 and count<30:
            gameDisplay.blit(alien3,(display_width/5,display_height/3))
        elif count>=30 and count<40:
            gameDisplay.blit(alien4,(display_width/5,display_height/3))
        a2=aliens2()
        alien1=myfont.render(a2.symbol1,False,a2.aliencolor)
        alien2=myfont.render(a2.symbol2,False,a2.aliencolor)
        if count%20<10:
            gameDisplay.blit(alien1,(display_width/5,display_height/3+50))
        elif count%20>=10 and count%20<20:
            gameDisplay.blit(alien2,(display_width/5,display_height/3+50))
        inst1=myfont.render("these are bob aliens. they die in 1 hit",False,color)
        inst2=myfont.render("these are poop aliens. they die in 3 hit",False,color)
        inst3=myfont.render("Avoid alien bullets",False,color)
        nextpg=myfont.render("(n) next",False,color)
        prevpg=myfont.render("(p) prev",False,color)
        main=myfont.render("(m) main menu->",False,color)
        gameDisplay.blit(title,(display_width/3, display_height/5))
        gameDisplay.blit(inst1,(display_width/3, display_height/3))
        gameDisplay.blit(inst2,(display_width/3, display_height/3+50))
        gameDisplay.blit(inst3,(display_width/8, display_height/3+90))
        gameDisplay.blit(nextpg,(3*display_width/4, display_height/3+4*30+5*math.sin(math.radians(count))))
        gameDisplay.blit(prevpg,(display_width/4, display_height/3+4*30+5*math.sin(math.radians(count))))
        gameDisplay.blit(main,(2*display_width/5, display_height/3+6*30+5*math.sin(math.radians(count))))
    
    if level==-1.3:
        title=titlefont.render("POWERUPS",False,color)
        p=[]
        p1=hp()
        p1.resize(disp_height)
        x=p1.symbol
        p.append(x)
        p1=machineGun()
        p1.resize(disp_height)
        x=p1.symbol
        p.append(x)
        p1=danger()
        p1.resize(disp_height)
        x=p1.symbol
        p.append(x)
        p1=freeze()
        p1.resize(disp_height)
        x=p1.symbol
        p.append(x)
        
        text=[]
        t=myfont.render("It heals you",False,color)
        text.append(t)
        t=myfont.render("This is ammo for MG. Use it by pressing 'E'",False,color)
        text.append(t)
        t=myfont.render("This decreases your health",False,color)
        text.append(t)
        t=myfont.render("This freezes your ship for some time",False,color)
        text.append(t)        
        t=myfont.render("You can also use Tesla bullet with 'W'. It also damages aliens adjecent to hit alien",False,color)
        nextpg=myfont.render("(n) next",False,color)
        text.append(t)        
        prevpg=myfont.render("(p) prev",False,color)
        main=myfont.render("(m) main menu->",False,color)
        gameDisplay.blit(title,(display_width/3, display_height/5))
        for i in range(0,ponumber+1):
            if i<ponumber:
                gameDisplay.blit(p[i],(10, display_height/3+i*90+5*math.cos(math.degrees(count))))
            gameDisplay.blit(text[i],(10, display_height/3+i*90+40))
        text.clear()
        gameDisplay.blit(nextpg,(3*display_width/4, display_height/3+i*120+5*math.sin(math.degrees(count))))
        gameDisplay.blit(prevpg,(display_width/4, display_height/3+i*120+5*math.sin(math.degrees(count))))
        gameDisplay.blit(main,(2*display_width/5, display_height/3+(i)*120+30+30+5*math.sin(math.degrees(count))))

    if level==-1.4:    
        title=titlefont.render("ENJOY!!!",False,color)
        start=myfont.render("(s) start",False,color)
        main=myfont.render("(m) main menu->",False,color)
        gameDisplay.blit(title,(display_width/3, display_height/5))        
        gameDisplay.blit(main,(2*display_width/5, display_height/5+100))
        gameDisplay.blit(start,(2*display_width/5, display_height/5+200))

def handleKeyPresses(level,ship,event,count):
    if level==0:
        #   handles all the keyDown events
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                ship.crashed=True
            if event.key==pygame.K_i:
                level=-1.1
            if event.key==pygame.K_s:
                level=0
                level_change=True
                level=changelevel(level,alienlist,level_change,ship)
                level_change=False
    elif level==-1.1:
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_n and count<20:
                level=-1.2
            if event.key==pygame.K_q:
                ship.crashed=True
            if event.key==pygame.K_m:
                level=0
    elif level==-1.2:
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_n and count>23:
                level=-1.3
            if event.key==pygame.K_p and count>23:
                level=-1.1
            if event.key==pygame.K_m:
                level=0
    elif level==-1.3:
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_n and count<20:
                level=-1.4
            if event.key==pygame.K_p and count<20:
                level=-1.2
            if event.key==pygame.K_m:
                level=0
    elif level==-1.4:
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                level=0
                level_change=True
                level=changelevel(level,alienlist,level_change,ship)
                level_change=False
            if event.key==pygame.K_m:
                level=0
    return level