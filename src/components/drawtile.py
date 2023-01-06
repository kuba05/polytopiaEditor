from math import ceil
from . import constants
import pygame
import pygame.gfxdraw

class DrawTile:
    def __init__(self, state, image):
        self.lastLength = None
        self.changeState(state, image)
        


    def changeState(self, state, newImage):
        self.state = state
        self.originalSurface = newImage.convert_alpha()
        self.rotatedSurface = None


   
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
    


    def draw(self, diagonalLength, x, y):
        if self.lastLength != diagonalLength or self.rotatedSurface == None:
            self.recalculateSurface(diagonalLength)
            self.lastLength = diagonalLength
        
        return self.rotatedSurface
