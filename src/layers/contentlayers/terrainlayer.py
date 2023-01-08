import sys, math

import pygame
import pygame.locals

from .contentlayer import ContentLayer
from components import DrawTile, constants, tilehelper

class TerrainLayer(ContentLayer):
    def setup(self):
        defaults = {
                "side": 15,
                "changeTerrainTo": lambda originalTerrain: originalTerrain,
        }
        self.setupSettings(defaults)

        self.gameplan = [
            [
                DrawTile(
                    constants.terrains.FOREST,
                    constants.terrainImages[constants.terrains.FOREST]
                ) for i in range(self.settings["side"])
            ] for j in range(self.settings["side"])
        ]


    def _draw(self, surfaceSize):
        self.surfaceSize = surfaceSize
        
        tileLength = tilehelper.getTileLength(self.surfaceSize, self.settings["side"])

        outputSurface = pygame.Surface(self.surfaceSize)
        outputSurface.fill((0, 0, 0, 255))

        for x, row in reversed(list(enumerate(self.gameplan))):
            for y, tile in enumerate(row):
                coordinates = tilehelper.getPositionOfTile(x, y, tileLength, self.settings["side"])
                outputSurface.blit(
                        tile.draw(tileLength + 1, x, y),
                        (coordinates[0], coordinates[1] - tileLength/4)
                )
        return outputSurface

    def handle(self, event, mousePosition):
        # wrong event type
        if (
            event.type == pygame.MOUSEBUTTONDOWN# or
            #(event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0])
        ):
            print("handling event")
            print(event)
            return self.handleClick(event, mousePosition)

    

    def handleClick(self, event, mousePosition):
        tileLength = tilehelper.getTileLength(self.surfaceSize, self.settings["side"])

        x, y = tilehelper.getTileFromCoordinates(mousePosition[0], mousePosition[1], tileLength, self.settings["side"])


        # position is outside
        if x < 0 or x >= len(self.gameplan) or y < 0 or y >= len(self.gameplan[0]):
            return False

        x, y = int(x), int(y)

        print(f"clicked on {x} {y}")
        # position is inside, so handle the click
        newState = self.settings["changeTerrainTo"](self.gameplan[x][y].state)
        print(newState)
        if newState == self.gameplan[x][y].state:
            return True
        
        return self.gameplan[x][y].changeState(newState, constants.terrainImages[newState])

