import abc
import pygame
from .layer import Layer
from components import SettingsManager

class FullscreenLayer(Layer):
    def __init__(self, surfaceSize: tuple[int], settingsManager: SettingsManager):
        """
        FullscreenLayer uses, unlike WindowedLayer, the whole surface it was given.
        """
        self.surfaceSize = surfaceSize
        self.settings = settingsManager
        self.setup()

    @abc.abstractmethod
    def handle(self, event: pygame.event, mousePosition: tuple[int]) -> bool:
        """
        Handle event call.
        Returns True if the event was consumed, False otherwise.
        """
        pass

    @abc.abstractmethod
    def draw(self, surfaceSize: tuple[int]) -> pygame.Surface:
        """
        Draws this layer on given pygame surface.
        """
        pass

    @abc.abstractmethod
    def setup(self) -> None:
        """
        This method is called upon construction of the object.

        Both self.settings and self.setupSettings are available.

        For setting default values of enviroment, please use fixEnviroment.
        """
        pass

    def changeSurface(self, newSurface: pygame.Surface) -> None:
        self.surface = newSurface

    def quit(self) -> None:
        """
        Cleanup after this screen.
        """
        pass

    def setupSettings(self, defaults: dict[str, any]) -> None:
        """
        defaults = {
            name1: value1,
            name2: value2,
            ...
        }

        Checks for each 'name', that it exists in enviroment and if not, it creates it setting its value to 'value'
        """
        for key, value in defaults.items():
            if key not in self.settings:
                self.settings[key] = value
