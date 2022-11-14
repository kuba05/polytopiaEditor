import pygame
from . import Screen

class GameOverlay(Screen):
    
    def handle(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]):
            pos = pygame.mouse.get_pos()
            if pos[1] >= self.screen.get_size()[1] - self.settings["gameOverlaySize"]:
                return True
        return False

    def draw(self):
        size = self.screen.get_size()
        pygame.draw.rect(self.screen, (50,50,50), ((0, size[1]-self.settings["gameOverlaySize"]),(size[0], size[1])))

