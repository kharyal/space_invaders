import pygame
# !__^__!  spaceShip
#  !_^_!   moving spaceShip  (not implemented)

left=[0]
right=[0]
class spaceShip():
    def __init__(self):
        self.symbol= "|/-^-\|"
        self.moveSymbol= "|/-^-\|"
        self.health=3                          
        self.coordinates=(400,750)
        self.movingrt=False 
        self.movinglt=False
        self.score=0
        self.crashed=False

    def getHealth(self):
        return self.health

    def decHealth(self):
        self.health-=1
    
    def moveleft(self):
        self.coordinates=(self.coordinates[0]-5,750)
        
    def moveright(self):
        self.coordinates=(self.coordinates[0]+5,750)