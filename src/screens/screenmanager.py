import pygame
from . import GameScreen, GameOverlay
import helper

class ScreenManager():
    def __init__(self, pygameScreen):
        self.settings = helper.loadSettings()
        self.enviroment = {}
        self.display = display
        self.screens = [
                GameScreen(
                    self.pygamescreen,
                    self.getEnviroment,
                    self.adjustEnviroment
                ),
                GameOverlay(
                    self.pygamescreen,
                    self.getEnviroment,
                    self.adjustEnviroment
                )
        ]


    def quit(self):
        """
        Terminate all processes
        """
        for screen in self.screens:
            screen.quit()
        helper.saveSettings(self.getSettings())

    def getSettings(self):
        return self.settings

    def adjustEnviroment(self, key, value):
        self.enviroment[key] = value
        
    def getEnviroment(self, key):
        # new syntax for merging dicts
        joined = self.enviroment | self.settings

        if key in joined:
            return joined[key]
        return None



    def handle(self, event):
        """
        Handle event call.
        Returns True if the event was consumed, False otherwise.
        """
        for screen in self.screens[::-1]:
            if screen.handle(event):
                return True

        return False
    
    def draw(self):
        """
        Draws on the pygame screen.
        """
        for screen in self.screens:
            screen.draw()

    


