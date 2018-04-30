import pygame
pygame.init()
#gameDisplay=pygame.display.set_mode((800,800))
gameDisplay=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
display_width,display_height = pygame.display.get_surface().get_size()

alienSpeed=3

ponumber=3
powerlist=[]