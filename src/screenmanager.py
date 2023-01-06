import pygame
from components import SettingsManager
from layers import TerrainLayer, Layer, GameOverlay, WindowedLayer 

class ScreenManager(Layer):
    def __init__(self, surfaceSize: tuple[int], settingsManager: SettingsManager):

        self.settings = settingsManager
    
        self.surfaceSize = surfaceSize

        self.layers = (
            WindowedLayer(
                GameOverlay,
                self.getGameOverlayPosition,
                self.surfaceSize,
                self.settings
            ),
            WindowedLayer(
                TerrainLayer,
                self.getGamePosition,
                self.surfaceSize,
                self.settings
            )

        )

    def getGamePosition(self, settings):
        position = (0, 0, self.surfaceSize[0], self.surfaceSize[1] - settings["gameOverlayHeight"])
        return position

    def getGameOverlayPosition(self, settings):
        position = (0, self.surfaceSize[1] - settings["gameOverlayHeight"], self.surfaceSize[0], settings["gameOverlayHeight"])
        return position


    def quit(self):
        for layer in self.layers:
            layer.quit()



    def handle(self, event, mousePosition):
        for layer in self.layers[::-1]:
            # if event is consumed, True is returned
            if layer.handle(event, mousePosition):
                return True

        return False
    


    def draw(self, surfaceSize: tuple[int]):
        self.surfaceSize = surfaceSize
        surface = pygame.Surface(surfaceSize, pygame.SRCALPHA)
        surface.fill((0,0,0,0))

        for layer in self.layers:
            surface.blit(layer.draw(surfaceSize), (0,0))

        return surface


