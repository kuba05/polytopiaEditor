import sys

import pygame
from . import Screen
from components import tile, constants

class GameScreen(Screen):
    def setup(self):
        print("setup")
        defaultsOne = {
                "side": 15,
                "tileLongerDiagonalLength": 150
        }
        
        self.fixEnviroment(defaultsOne)

        defaultsTwo = {
                "cameraOffset":  [
                    0,
                    self.settings["side"]/4 * self.settings["tileLongerDiagonalLength"]
                ],
                "mode": constants.modes.CHANGETILES,
                "changeto": constants.tiles.FOREST,
                "gameplan": [
                    [
                        tile.Tile(
                            self.display,
                            i,
                            j,
                            constants.tiles.FOREST
                        ) for i in range(self.settings["side"])
                    ] for j in range(self.settings["side"])
                ]
        }
        
        self.settings.log()
        self.fixEnviroment(defaultsTwo)

    def draw(self):
        gameplan = self.settings["gameplan"]

        for row in gameplan:
            for tile in row:
                tile.draw(self.settings["tileLongerDiagonalLength"], self.settings["cameraOffset"])

    def handle(self, event):
        # wrong event type
        if (
            event.type != pygame.MOUSEBUTTONDOWN and
            (event.type != pygame.MOUSEMOTION or not pygame.mouse.get_pressed()[0])
        ):
            return False
        
        # load relevant enviroment
        pos = pygame.mouse.get_pos()
        cameraOffset = self.settings["cameraOffset"]
        tileLongerDiagonalLength = self.settings["tileLongerDiagonalLength"]
        gameplan = self.settings["gameplan"]


        XCor = pos[0] - cameraOffset[0]
        YCor = pos[1] - cameraOffset[1]

        x = int((XCor + 2*YCor) // tileLongerDiagonalLength)
        y = int((XCor - 2*YCor) // tileLongerDiagonalLength)

        # position is outside
        if x < 0 or x >= len(gameplan) or y < 0 or y >= len(gameplan[0]):
            return False

        # position is inside, so handle the click
        return gameplan[x][y].changeState(self.settings["changeto"])
