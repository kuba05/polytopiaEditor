import pygame
from . import Screen, GameScreen, GameOverlay
import helper

class ScreenManager(Screen):
    def setup(self):
        screensToCreate = (
            GameScreen,
            GameOverlay
        )

        self.screens = [
                Screen(
                    self.display,
                    self.settings
                )

                for Screen in screensToCreate
        ]

    def quit(self):
        for screen in self.screens:
            screen.quit()

    def handle(self, event):
        for screen in self.screens[::-1]:
            if screen.handle(event):
                return True

        return False
    
    def draw(self):
        for screen in self.screens:
            screen.draw()
