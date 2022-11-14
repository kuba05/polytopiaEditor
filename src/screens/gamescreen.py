import sys

import pygame
from . import Screen
from components import tile, constants

class GameScreen(Screen):

    def setup(self):
        defaults = {
                "side": 15,
                "cameraOffset":  [
                    0,
                    self.getEnviroment("side")/4 * self.getEnviroment("tileLongerDiagonalLength")
                ],
                "mode": constants.modes.CHANGETILES,
                "changeto": constants.tiles.FOREST
                "gameplan": [
                    [
                        tile.Tile(
                            self.display,
                            i,
                            j,
                            (i+j)%4
                        ) for i in range(enviroment["side"])
                    ] for j in range(enviroment["side"])
                ]
        }

        self.fixEnviroment(defaults)

        

    def draw(self):
        """
        Draw on screen
        """
        gameplan = self.getEnviroment("gameplan")

        for row in gameplan:
            for tile in row:
                tile.draw()



    def handle(self, event):
        """
        Handle events.
        """
        # wrong event type
        if (
            event.type != pygame.MOUSEBUTTONDOWN and
            (event.type != pygame.MOUSEMOTION or not pygame.mouse.get_pressed()[0])
        ):
            return False
        
        # load relevant enviroment
        pos = pygame.mouse.get_pos()
        cameraOffset = self.getEnviroment("cameraOffset")
        longerDiagonalLength = self.getEnviroment("tileLongerDiagonalLength")
        gameplan = self.getEnviroment("gameplan")


        XCor = pos[0] - cameraOffset[0]
        YCor = pos[1] - cameraOffset[1]

        x = int((XCor + 2*YCor) // tileLongerDiagonalLength)
        y = int((XCor - 2*YCor) // tileLongerDiagonalLength)

        # position is outside
        if x < 0 or x >= len(gameplan) or y < 0 or y >= len(gameplan[0]):
            return False

        # position is inside, so handle the click
        return gameplan[x][y].handle(event)
