"""returns the position of board at any instance"""
import pygame
import sys
from aliens import *
from spaceShip import *
from bullets import *
from level1 import *
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)
black=(0,0,0)
white=(255,255,255)
shipcolor=( 55,151,40)
ship=spaceShip()
line=myfont.render("---------------------------------------------------------------------------------------------------------------",False,shipcolor)
shipImg = myfont.render(ship.symbol, False, shipcolor)

display_width=800
display_hieght=800

gameDisplay=pygame.display.set_mode((display_width,display_hieght))
pygame.display.set_caption('spaceInvaders')

#important variables
clock=pygame.time.Clock()

movinglt=False
movingrt=False
direction=1
direction_change=False
count=0
tesla_counter=[0]
level_change=False
crashed=False
level=1

while not ship.crashed:
    timer=(pygame.time.get_ticks())%5000
    for event in pygame.event.get():
        pass
    if event.type == pygame.QUIT:
        ship.crashed==True
    
#   handles all the keyDown events
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_q:
            ship.crashed=True
        if event.key==pygame.K_a:
            movinglt=True
        if event.key==pygame.K_d:
            movingrt=True
        if event.key==pygame.K_SPACE:
            if not simple_bullet.present:
                simple_bullet.present=True
                simple_bullet.setCoordinate(ship.coordinates[0]+27,ship.coordinates[1])
        if event.key==pygame.K_w:
            if not tesla_bullet.present:
                tesla_bullet.present=True
                tesla_bullet.setCoordinate(ship.coordinates[0]+27,ship.coordinates[1])
    
    elif event.type==pygame.KEYUP:
        if event.key==pygame.K_a:
            movinglt=False
        if event.key==pygame.K_d:
            movingrt=False

    gameDisplay.fill(black)

    if movinglt and ship.coordinates[0]>0:
#        print("movinglt")
        gameDisplay.blit(shipImg,ship.coordinates)
        ship.moveleft()
        gameDisplay.blit(shipImg,ship.coordinates)
    elif movingrt and ship.coordinates[0]<730:
#        print("movingrt")
        gameDisplay.blit(shipImg,ship.coordinates)
        ship.moveright()
        gameDisplay.blit(shipImg,ship.coordinates)
    else:
#        print("notMoving")
        gameDisplay.blit(shipImg,ship.coordinates)
    
#   draws aliens and gets important values
    tup=draw_aliens(count,direction,direction_change,gameDisplay,ship,alien_present,level_change)
    level_change=tup[2]
    direction=tup[0]
    direction_change=tup[1]
    count=(count+1)%40
#    print(ship.coordinates[0])
#   handles bullets
    if simple_bullet.present:
        draw_bullets(simple_bullet,1,gameDisplay)

    if tesla_bullet.present:
        draw_bullets(tesla_bullet,2,gameDisplay)
    if timer%5000>=499 and timer%5000<550:
        set_alien_bult_coordinates(alien_bult)
    if alien_bult.present:
        draw_bullets(alien_bult,0,gameDisplay)

    handle_bullet_collision(simple_bullet,1,ship)
    handle_bullet_collision(tesla_bullet,2,ship)
    handle_bullet_collision(alien_bult,0,ship)
    if ship.health==0:
        ship.crashed=True
    gameDisplay.blit(line,(0,700))

    if level_change:
        level=changelevel(level,alienlist,level_change,ship)
        level_change=False
    pygame.display.update()
    clock.tick(60)