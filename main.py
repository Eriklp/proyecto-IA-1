import pygame

pygame.init()
Screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_icon(pygame.image.load("Icon.png"))
pygame.event.set_allowed(None)  # PyGame will now not check for any inputs
allowed_events = (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN,
                  pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT)
for event in allowed_events:         # PyGame will now only check inputs for things used in the
    pygame.event.set_allowed(event)