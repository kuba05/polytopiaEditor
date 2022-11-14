from . import constants
import pygame

class Tile:
    def __init__(self, screen, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.screen = screen
        self.__adjustColor()

    def __adjustColor(self):
        if self.state == 0:
            self.color = pygame.Color(255,0,0)
        if self.state == 1:
            self.color = pygame.Color(0,255,0)
        if self.state == 2:
            self.color = pygame.Color(0,0,255)
        if self.state == 3:
            self.color = pygame.Color(255,255,255)
        if self.state == constants.tiles.FOREST:
            self.color = pygame.Color(0, 255, 0)

    def changeState(self, newState):
        print("chaning state")
        print(self)
        self.state = newState
        self.__adjustColor()
    def draw(self, diagonalLength, cameraOffset):
        pOne = ((self.x+self.y)*diagonalLength/2 + cameraOffset[0], (self.y-self.x)*diagonalLength/4 + cameraOffset[1])
        pTwo = (pOne[0]+diagonalLength, pOne[1])
        pThree = (pOne[0] + diagonalLength/2, pOne[1] + diagonalLength/4)
        pFour = (pThree[0], pThree[1] - diagonalLength/2)
        
#        print(pOne, pTwo, pThree, pFour)
        pygame.draw.polygon(self.screen, self.color, (pOne, pThree, pTwo, pFour))
