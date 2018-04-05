import pygame, sys
from pygame.locals import *

class Cursor(pygame.Rect):
	def __init__(self):
		pygame.Rect.__init__(self, 0,0,1,1)
	def update(self):
		self.left, self.top = pygame.mouse.get_pos()

def main():
	pygame.init()
	ventana = pygame.display.set_mode((1000, 650))
	#pygame.display.set_icon(pygame.image.load(""))
	pygame.display.set_caption("Super Mario")

	ima = pygame.image.load("Icon.png")
	posX, posy = 600, 100

	velocidad = 5
	while True:

		ventana.blit(ima, (posX, posy))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()

main()