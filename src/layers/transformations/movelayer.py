from collections.abc import Callable

import pygame

from ..layer import Layer, LayerBuilder
from components import SettingsManager

class MoveLayer(Layer):
    def __init__(
            self,
            surfaceSize: tuple[int],
            settingsManager: SettingsManager,
            layerBuilder: LayerBuilder,
            getWindowPosition: Callable[[tuple[int], SettingsManager], pygame.Rect]
    ):
        self.surfaceSize = surfaceSize
        self.settings = settingsManager

        self.getPosition = getWindowPosition
        self.currentPosition = pygame.Rect(
                (0, 0, 0, 0)
        )
        
        self.layer = layerBuilder.build(
                (self.currentPosition.w, self.currentPosition.h),
                self.settings
        )
        self.recalculatePosition()



    def recalculatePosition(self):
        newPosition = pygame.Rect(self.getPosition(self.surfaceSize, self.settings))
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



    def _draw(self, surfaceSize: tuple[int]) -> pygame.Surface:
        """
        Draws this layer in given pygame Surface
        """
        self.surfaceSize = surfaceSize
        self.recalculatePosition()
        surface = pygame.Surface(self.surfaceSize, pygame.SRCALPHA)
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
