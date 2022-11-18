import pygame
from . import Screen
from components import constants


class GameOverlay(Screen):
    def setup(self):
        defaults = {
                "gameOverlaySize": 100,
                "changeto": constants.tiles.FOREST
        }
        
        self.fixEnviroment(defaults)

        self.overlayShift = 0

        for tile in constants.tiles:
            print(tile)
            print(constants.tiles[tile])

        self.buttons = {
                constants.tiles[tile]: constants.tilesSurfaces[constants.tiles[tile]]
                for tile in constants.tiles
        }



    def handle(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]):
            pos = pygame.mouse.get_pos()
            displaySize = self.display.get_size()
            if pos[1] >= displaySize[1] - self.settings["gameOverlaySize"]:
                self.__handleClick(pos[0]/displaySize[0])
                return True
        return False



    def __handleClick(self, part):
        """
        part is the part of the overlay that was clicked on
        """
        self.settings["changeto"] = list(self.buttons.keys())[int(part*len(self.buttons))]


        
    def draw(self):
        displaySize = self.display.get_size()

        for i, button in enumerate(self.buttons.keys()):
            self.display.blit(
                pygame.transform.scale(
                    self.buttons[button],
                    (
                        displaySize[0] / len(self.buttons), self.settings["gameOverlaySize"]
                    )
                ),
                (
                    displaySize[0] / len(self.buttons) * i,
                    displaySize[1] - self.settings["gameOverlaySize"]
                )
            )

