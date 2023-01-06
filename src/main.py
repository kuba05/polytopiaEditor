import pygame, sys

from screenmanager import ScreenManager
from components import SettingsManager


RESOLUTION = (600, 400)
FPS = 30
SETTINGS_FILE = "settings.conf"



def exit():
    settingsManager.saveSettings(SETTINGS_FILE)
    screenManager.quit()
    pygame.quit()



pygame.init()
fpsClock = pygame.time.Clock()
display = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)

settingsManager = SettingsManager()
settingsManager.loadSettings(SETTINGS_FILE)
screenManager = ScreenManager(display.get_size(), settingsManager)

#loop
running = True


try:
    while running:
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                screenManager.handle(event, pygame.mouse.get_pos())
        
        display.fill((0,0,0))
        display.blit(screenManager.draw(display.get_size()), (0,0))
        pygame.display.update()
        fpsClock.tick(FPS)
except Exception as e:
    exit()
    raise e

exit()
sys.exit()


