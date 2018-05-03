import pygame
pygame.init()
#gameDisplay=pygame.display.set_mode((800,800))
gameDisplay=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
display_width,display_height = pygame.display.get_surface().get_size()
origSpeed=display_width/400
alienSpeed=display_width/400

ponumber=4
powerlist=[]
level=0
changePage=False
level_change=False
alienlist=[[],[],[],[],[],[],[],[],[],[],[]]
count=0
