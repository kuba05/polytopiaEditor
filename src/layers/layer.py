import abc
import pygame
from components import SettingsManager

class LayerBuilder:
    def __init__(self, layer, params):
        self.layer = layer
        self.params = params

    def build(self, surfaceSize: tuple[int], settingsManager: SettingsManager):
        """
        create layer
        """
        return self.layer(surfaceSize, settingsManager, *self.params)

class Layer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, surfaceSize: tuple[int], settingsManager: SettingsManager, *params):
        pass

    @abc.abstractmethod
    def handle(self, event: pygame.event, mousePosition: tuple[int]) -> bool:
        """
        Handle event call.
        Returns True if the event was consumed, False otherwise.
        """
        pass
    
    @abc.abstractmethod
    def _draw(self, surfaceSize: tuple[int]) -> pygame.Surface:
        pass

    def draw(self, surfaceSize: tuple[int]) -> pygame.Surface:
        """
        Draws this layer on given pygame surface.
        """
        surface = pygame.Surface(surfaceSize, pygame.SRCALPHA)
        surface.fill((0,0,0,0))
        surface.blit(self._draw(surfaceSize), (0,0))
        return surface

    def quit(self) -> None:
        """
        Cleanup after this screen.
        """
        pass

    @classmethod
    def builder(className, *params) -> LayerBuilder:
        return LayerBuilder(className, params)

