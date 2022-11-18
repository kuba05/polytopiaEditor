import abc
import pygame
from settingsmanager import SettingsManager

class Screen(metaclass=abc.ABCMeta):
    def __init__(self, display: pygame.Surface, settingsManager: SettingsManager):
        self.display = display
        self.settings = settingsManager
        self.setup()

    @abc.abstractmethod
    def handle(self, event: pygame.event) -> bool:
        """
        Handle event call.
        Returns True if the event was consumed, False otherwise.
        """
        pass

    @abc.abstractmethod
    def draw(self) -> None:
        """
        Draws this screen of the pygame screen.
        """
        pass

    @abc.abstractmethod
    def setup(self) -> None:
        """
        This method is called upon construction of the object.

        Both getEnviroment and adjustEnviroment are available.

        For setting default values of enviroment, please use fixEnviroment.
        """
        pass

    def quit(self) -> None:
        """
        Cleanup after this screen.
        """
        pass

    def fixEnviroment(self, defaults: dict[str, any]) -> None:
        """
        defaults = {
            name1: value1,
            name2: value2,
            ...
        }

        Checks for each 'name', that it exists in enviroment and if not, it creates it setting its value to 'value'
        """
        print("fixing enviroment")
        print(defaults)
        for key, value in defaults.items():
            if key not in self.settings:
                self.settings[key] = value
