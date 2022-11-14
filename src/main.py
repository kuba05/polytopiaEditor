import pygame, sys

from screens import screenmanager

pygame.init()
RESOLUTION = (600, 400)
FPS = 30

fpsClock = pygame.time.Clock()
display = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)

screen = screenmanager.ScreenManager(display)

#loop
running = True
while running:
    events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            screen.handle(event) 
 #   screenManager.update(events)
    screen.draw()
    pygame.display.update()
    fpsClock.tick(FPS)

screen.quit()
pygame.quit()
sys.exit()


