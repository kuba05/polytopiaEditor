import pygame, sys

from components import SettingsManager
from setuplayers import SetupLayers

RESOLUTION = (600, 400)
FPS = 30
SETTINGS_FILE = "settings.conf"



def exit():
    settingsManager.saveSettings(SETTINGS_FILE)
    rootLayer.quit()
    pygame.quit()



pygame.init()
fpsClock = pygame.time.Clock()
display = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)

settingsManager = SettingsManager()
settingsManager.loadSettings(SETTINGS_FILE)
rootLayer = SetupLayers(display.get_size(), settingsManager).getRoot()

#loop
running = True


try:
    while running:
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                rootLayer.handle(event, pygame.mouse.get_pos())
        
        display.fill((0,0,0))
        display.blit(rootLayer.draw(display.get_size()), (0,0))
        pygame.display.update()
        fpsClock.tick(FPS)
except Exception as e:
    exit()
    raise e

exit()
sys.exit()


