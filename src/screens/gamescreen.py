import sys

import pygame
import pygame.locals
from . import Screen
from components import tile, constants

class GameScreen(Screen):
    def setup(self):
        defaultsOne = {
                "side": 15,
                "tileDiagonalLength": 150,
                "scrollingSpeed": 10
        }
        
        self.fixEnviroment(defaultsOne)

        defaultsTwo = {
                "cameraOffset":  [
                    100,
                    self.settings["side"]/4 * self.settings["tileDiagonalLength"]
                ],
                "mode": constants.modes.SELECT,
                "onTileClick": lambda tile: False,
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
                tile.draw(self.settings["tileDiagonalLength"], self.settings["cameraOffset"])

    def handle(self, event):
        # wrong event type
        if (
            event.type == pygame.MOUSEBUTTONDOWN or
            (event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0])
        ):
            self.handleClick(event)
            return True

        if (event.type == pygame.KEYDOWN):
            self.handleScrolling(
                    event.key == pygame.locals.K_UP,
                    event.key == pygame.locals.K_DOWN,
                    event.key == pygame.locals.K_LEFT,
                    event.key == pygame.locals.K_RIGHT
            )
            return True


       
    def handleScrolling(self, up, down, left, right):
        if up: 
            self.settings["cameraOffset"][1] += self.settings["scrollingSpeed"]
        if down:
            self.settings["cameraOffset"][1] -= self.settings["scrollingSpeed"]
        if left:
            self.settings["cameraOffset"][0] += self.settings["scrollingSpeed"]
        if right:
            self.settings["cameraOffset"][0] -= self.settings["scrollingSpeed"]


        displaySize = self.display.get_size()

        tolerance = 2 * self.settings["tileDiagonalLength"]

        maxScrollUp = self.settings["side"]/2 * self.settings["tileDiagonalLength"]/2

        maxScrollDown = -(self.settings["side"]/2 * self.settings["tileDiagonalLength"]/2 - displaySize[1])

        maxScrollLeft = 0

        maxScrollRight = -(self.settings["side"] * self.settings["tileDiagonalLength"] - displaySize[0])

        if self.settings["cameraOffset"][1] > maxScrollUp + tolerance:
            self.settings["cameraOffset"][1] = maxScrollUp + tolerance

        if self.settings["cameraOffset"][1] < maxScrollDown - tolerance: 
            self.settings["cameraOffset"][1] = maxScrollDown - tolerance

        if self.settings["cameraOffset"][0] > maxScrollLeft + tolerance:
            self.settings["cameraOffset"][0] = maxScrollLeft + tolerance
        
        if self.settings["cameraOffset"][0] < maxScrollRight - tolerance:
            self.settings["cameraOffset"][0] = maxScrollRight - tolerance



    def handleClick(self, event):
        # load relevant enviroment
        pos = pygame.mouse.get_pos()
        cameraOffset = self.settings["cameraOffset"]
        tileDiagonalLength = self.settings["tileDiagonalLength"]
        gameplan = self.settings["gameplan"]


        XCor = pos[0] - cameraOffset[0]
        YCor = pos[1] - cameraOffset[1]

        x = int((XCor + 2*YCor) // tileDiagonalLength)
        y = int((XCor - 2*YCor) // tileDiagonalLength)

        # position is outside
        if x < 0 or x >= len(gameplan) or y < 0 or y >= len(gameplan[0]):
            return False

        # position is inside, so handle the click
        return self.settings["onTileClick"](gameplan[x][y])
