from . import constants
import pygame
import pygame.gfxdraw

class Tile:
    def __init__(self, screen, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.screen = screen
        self.lastLength = None
        self.originalSurface = None
        self.rotatedSurface = None
        
        self.__adjustColor()



    def __adjustColor(self):
        self.originalSurface = constants.tilesImages[self.state].convert_alpha()
        self.rotatedSurface = None



    def changeState(self, newState):
        print("chaning state")
        print(self)
        self.state = newState
        self.__adjustColor()


   
    def recalculateSurface(self, diagonalLength):
        surface = pygame.transform.scale(
                self.originalSurface,
                (diagonalLength, diagonalLength)
        )

        surface = pygame.transform.rotate(
                surface,
                45
        )

        self.rotatedSurface = pygame.transform.scale(
                surface,
                (diagonalLength, diagonalLength/2)
        )
    


    def draw(self, diagonalLength, cameraOffset):
        if self.lastLength != diagonalLength or self.rotatedSurface == None:
            self.recalculateSurface(diagonalLength)
            self.lastLength = diagonalLength


        leftBottom = ((self.x+self.y)*diagonalLength/2 + cameraOffset[0], (self.y - self.x - 1)*diagonalLength/4 + cameraOffset[1])
        
        self.screen.blit(
            self.rotatedSurface,
            leftBottom
        )
