import abc
import pygame

class Screen(metaclass=abc.ABCMeta):
    def __init__(self, display: pygame.Surface, getEnviroment, adjustEnviroment):
        self.display = display
        self.getEnviroment = getEnviroment
        self.adjustEnviroment = adjustEnviroment
        self.setup()


    @abc.abstractmethod
    def handle(self, event: pygame.event) -> bool:
        pass

    @abc.abstractmethod
    def draw(self) -> None:
        pass

    @abc.abstractmethod
    def setup(self) -> None:
        pass

    def quit(self) -> None:
        pass

    def fixEnviroment(defaults: dict[str, any]) -> None:
        for key, value in defaults:
            if self.getEnviroment(key) == None:
                self.adjustEnviroment(key, value)
