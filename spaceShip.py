import pygame
from display import *
# !__^__!  spaceShip
#  !_^_!   moving spaceShip  (not implemented)

left=[0]
right=[0]
class spaceShip():
    def __init__(self):
        self.symbol= "|/-^-\|"
        self.sheildSymbol= "|/-^-\|"
        self.health=3                          
        self.coordinates=(display_width/2,display_height-50)
        self.movingrt=False 
        self.movinglt=False
        self.score=0
        self.crashed=False
        self.mg=False
        self.mgcount=0

    def getHealth(self):
        return self.health

    def decHealth(self):
        self.health-=1
    
    def moveleft(self):
        self.coordinates=(self.coordinates[0]-5,display_height-50)
        
    def moveright(self):
        self.coordinates=(self.coordinates[0]+5,display_height-50)