import abc
import pygame
from components import SettingsManager

class Layer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self, event: pygame.event, mousePosition: tuple[int]) -> bool:
        """
        Handle event call.
        Returns True if the event was consumed, False otherwise.
        """
        pass

    @abc.abstractmethod
    def draw(self, outputSurfaceSize: tuple[int]) -> pygame.Surface:
        """
        Draws this screen of the pygame screen.
        """
        pass

    def quit(self) -> None:
        """
        Cleanup after this screen.
        """
        pass
