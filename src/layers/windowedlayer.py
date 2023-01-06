from collections.abc import Callable

import pygame

from .layer import Layer
from .fullscreenlayer import FullscreenLayer
from components import SettingsManager

class WindowedLayer(Layer):
    def __init__(
            self,
            layer: FullscreenLayer,
            getWindowPosition: Callable[[SettingsManager], pygame.Rect],
            baseSurfaceSize,
            settingsManager: SettingsManager
    ):
        self.baseSurfaceSize = baseSurfaceSize
        self.getPosition = getWindowPosition
        self.currentPosition = pygame.Rect((0,0), (0,0))
        self.settings = settingsManager
        self.layer = layer(
                (self.currentPosition.w, self.currentPosition.h),
                self.settings
        )

        self.recalculatePosition()



    def recalculatePosition(self):
        newPosition = pygame.Rect(self.getPosition(self.settings))
        if newPosition == self.currentPosition:
            return
        self.currentPosition = newPosition



    def handle(self, event: pygame.event, mousePosition: tuple[int]) -> bool:
        """
        Handle event call.
        Returns True if the event was consumed, False otherwise.
        """
        # for mouse events we test, if the mouse is inside the window
        if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
            # mouse is outside this window
            if not self.currentPosition.collidepoint(mousePosition):
                # ignore event
                return False
        
        # let the layer handle the event        
        return self.layer.handle(
            event,
            # mousePosition has to be relative to the layer
            [
                mousePosition[0] - self.currentPosition.x,
                mousePosition[1] - self.currentPosition.y
            ]
        )



    def draw(self, outputSurfaceSize: tuple[int]) -> pygame.Surface:
        """
        Draws this layer in given pygame Surface
        """
        self.baseSurfaceSize = outputSurfaceSize
        self.recalculatePosition()
        surface = pygame.Surface(self.baseSurfaceSize, pygame.SRCALPHA)
        surface.fill((0,0,0,0))
        surface.blit(
                self.layer.draw(
                    (self.currentPosition.w, self.currentPosition.h)
                ),
                (self.currentPosition.x, self.currentPosition.y)
        )
        return surface



    def quit(self) -> None:
        """
        Cleanup after this layer.
        """
        self.layer.quit()
