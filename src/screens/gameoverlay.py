import pygame
from . import Screen
from components import constants

class Button():
    def __init__(self, image, onClick):
        self.image = image
        self.onClick = onClick

    def changeTileStateOnClick(newTileStateFunction):
        """
        helper function, because python has some issues with nasting anonymous functions and variable scopes
        """
        return lambda overlay: overlay.changeOnTileClick(
            lambda tile: tile.changeState(newTileStateFunction)
        )
    
    def multipleFunctions(*func):
        def helper(a):
            for f in func:
                f(a)
            return 0

        return helper

class GameOverlay(Screen):
    def setup(self):
        defaults = {
                "gameOverlaySize": 100,
                "onTileClick": lambda tile: constants.tiles.FOREST,
                "mode": constants.modes.SELECT
        }
       
        self.fixEnviroment(defaults)

        self.mode = self.settings["mode"]
        
        print(self.mode)
        self.overlayShift = 0
        
        self.setButtons()



    def changeMode(self, mode):
        print("mode changed")
        self.settings["mode"] = mode
        self.mode = mode
        self.setButtons()



    def setButtons(self):
        if self.settings["mode"] == constants.modes.SELECT:
            self.buttons = [
                    Button(
                        constants.modesImages[mode], #image
                        lambda overlay: overlay.changeMode(mode) #onclick
                    )
                    for mode in constants.modes if mode != constants.modes.SELECT
            ]

        if self.settings["mode"] == constants.modes.CHANGETILES:
            # button to move back to selection
            self.buttons = [
                    Button(
                        constants.modesImages[constants.modes.SELECT],
                        Button.multipleFunctions(
                            lambda overlay: overlay.changeMode(constants.modes.SELECT),
                            lambda overlay: overlay.changeOnTileClick(lambda tile: False)
                        )
                    )
            ] + [
                    Button(
                        constants.tilesImages[tile], #image
                        Button.changeTileStateOnClick(tile)
                    )
                    for tile in constants.tiles
            ]



    def handle(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]):
            pos = pygame.mouse.get_pos()
            displaySize = self.display.get_size()
            if pos[1] >= displaySize[1] - self.settings["gameOverlaySize"]:
                self.__handleClick(pos[0]/displaySize[0])
                return True
        return False


    def changeOnTileClick(self, onTileClick):
        self.settings["onTileClick"] = onTileClick

    def __handleClick(self, part):
        """
        part is the part of the overlay that was clicked on
        """
        #invoke onClick part of buttons
        self.buttons[int(part*len(self.buttons))].onClick(self)


        
    def draw(self):

        if self.settings["mode"] != self.mode:
            self.changeMode(self.settings["mode"])

        displaySize = self.display.get_size()

        for i, button in enumerate(self.buttons):
            self.display.blit(
                pygame.transform.scale(
                    button.image, 
                    (
                        displaySize[0] / len(self.buttons), self.settings["gameOverlaySize"]
                    )
                ),
                (
                    displaySize[0] / len(self.buttons) * i,
                    displaySize[1] - self.settings["gameOverlaySize"]
                )
            )

