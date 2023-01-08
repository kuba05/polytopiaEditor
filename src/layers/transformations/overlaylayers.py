import pygame

from ..layer import Layer, LayerBuilder
from components import SettingsManager

class OverlayLayers(Layer):
    def __init__(self,
            surfaceSize: tuple[int],
            settingsManager: SettingsManager,
            layerBuilders: tuple[LayerBuilder] = []
    ):
        """
        Draw multiple Layers over each other.
        """

        self.settings = settingsManager
    
        self.surfaceSize = surfaceSize

        self.layers = [builder.build(self.surfaceSize, self.settings) for builder in layerBuilders]

    
    def addLayer(self, layerBuilder):
        self.layers.append(
                layerBuilder.build(self.surfaceSize, self.settings)
        )



    def quit(self):
        for layer in self.layers:
            layer.quit()



    def handle(self, event, mousePosition):
        for layer in self.layers[::-1]:
            # if event is consumed, True is returned
            if layer.handle(event, mousePosition):
                return True

        return False
    


    def _draw(self, surfaceSize: tuple[int]):
        self.surfaceSize = surfaceSize
        surface = pygame.Surface(self.surfaceSize, pygame.SRCALPHA)
        surface.fill((0,0,0,0))

        for layer in self.layers:
            surface.blit(layer.draw(surfaceSize), (0,0))

        return surface

