import pygame, sys

from screens import screenmanager
from settingsmanager import SettingsManager


pygame.init()
RESOLUTION = (600, 400)
FPS = 30
SETTINGS_FILE = "settings.conf"



fpsClock = pygame.time.Clock()
display = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)

settingsManager = SettingsManager()
settingsManager.loadSettings(SETTINGS_FILE)
screenManager = screenmanager.ScreenManager(display, settingsManager)

pygame.key.set_repeat(50)
#loop
running = True
while running:
    events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            screenManager.handle(event)
    
    display.fill((0,0,0))
    screenManager.draw()
    pygame.display.update()
    fpsClock.tick(FPS)

settingsManager.saveSettings(SETTINGS_FILE)
screenManager.quit()
pygame.quit()
sys.exit()


