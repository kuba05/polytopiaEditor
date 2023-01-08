import pygame
from .contentlayer import ContentLayer
from components import constants, Button, Function


class GameControl(ContentLayer):
    def setup(self):
        defaults = {
                "gameControlHeight": 100,
                "changeTerrainTo": lambda originalTerrain: originalTerrain,
        }
       
        self.mode = constants.gameoverlay.modes.SELECTMODE
        self.setupSettings(defaults)
        
        self.setButtons()



    def changeMode(self, mode):
        print("mode changed")
        print("new mode")
        self.mode = mode
        self.setButtons()



    def changeSettings(self, **kwargs):
        for key, value in kwargs.items():
            self.settings[key] = value
        self.settings.log()

    def setButtons(self):
        if self.mode == constants.gameoverlay.modes.SELECTMODE:
            self.buttons = [
                    Button(
                        #image
                        constants.gameoverlay.modesImages[mode],
                        #onclick
                        Function(
                            self.changeMode,
                            mode
                        )
                    )
                    for mode in constants.gameoverlay.modes if mode != constants.gameoverlay.modes.SELECTMODE
            ]
            return

        if self.mode == constants.gameoverlay.modes.BANANA:
            self.buttons = [
            # button to move back to selection
                    Button(
                        constants.gameoverlay.modesImages[constants.gameoverlay.modes.SELECTMODE], #image
                        Button.multipleFunctions(
                            Function(self.changeMode, constants.gameoverlay.modes.SELECTMODE),
                            Function(self.changeSettings, changeTerrainTo = lambda previous: previous)
                        )
                    )
            ]

        if self.mode == constants.gameoverlay.modes.CHANGETERRAIN:
            self.buttons = [
            # button to move back to selection
                    Button(
                        constants.gameoverlay.modesImages[constants.gameoverlay.modes.SELECTMODE], #image
                        Button.multipleFunctions(
                            Function(self.changeMode, constants.gameoverlay.modes.SELECTMODE),
                            Function(self.changeSettings, changeTerrainTo = lambda originalTerrain: originalTerrain)
                        )
                    )
            ] + [
                    Button(
                        constants.terrainImages[terrain], #image
                        Function(self.changeSettings, changeTerrainTo = Function(str, terrain))
                    )
                    for terrain in constants.terrains
            ]
            return


    def handle(self, event, mousePosition):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            self.__handleClick(mousePosition[0]/self.surfaceSize[0])
            return True
        return False


    
    def __handleClick(self, part):
        """
        part is the part of the overlay that was clicked on
        """
        #invoke onClick part of buttons
        self.buttons[int(part*len(self.buttons))].onClick()


        
    def _draw(self, surfaceSize):
        self.surfaceSize = surfaceSize

        display = pygame.Surface(surfaceSize)

        for i, button in enumerate(self.buttons):
            display.blit(
                pygame.transform.scale(
                    button.image, 
                    (
                        self.surfaceSize[0] / len(self.buttons), self.surfaceSize[1]
                    )
                ),
                (
                    self.surfaceSize[0] / len(self.buttons) * i,
                    0
                )
            )

        #display.fill((255,255,255))
        return display

