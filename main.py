import pygame, sys
from pygame.locals import *

class Cursor(pygame.Rect):
	def __init__(self):
		pygame.Rect.__init__(self, 0,0,1,1)
	def update(self):
		self.left, self.top = pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
	def __init__(self, ima1, ima2, x=800, y=20):
		self.ima_normal=ima1
		self.ima_seleccion=ima2
		self.ima_actual=self.ima_normal
		self.rect=self.ima_actual.get_rect()
		self.rect.left, self.rect.top=(x, y)
	def update(self, pantalla, cursor):
		if cursor.colliderect(self.rect):
			self.imagen_actual=self.ima_seleccion
		else: self.ima_actual = self.ima_normal

		pantalla.blit(self.ima_actual, self.rect)


def main():
	pygame.init()
	ventana = pygame.display.set_mode((1000, 650))
	#pygame.display.set_icon(pygame.image.load(""))
	pygame.display.set_caption("Super Mario")

	ima = pygame.image.load("Icon.png")
	posX, posy = 600, 100

	velocidad = 5

	imagenCarga = pygame.image.load("images/upload.png")

	cursor1 = Cursor()
	botonCarga = Boton(imagenCarga, imagenCarga)

	while True:

		ventana.blit(ima, (posX, posy))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		cursor1.update()
		pygame.display.update()

main()