import pygame, sys
from pygame.locals import *

pygame.init()

displaysurf = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption("Arrow Test")

BLACK = ( 0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)

cat_img = pygame.image.load("cat.png")
catx = 10
caty = 10

while True:
	displaysurf.fill(WHITE)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	keys = pygame.key.get_pressed()
	if keys[K_LEFT]:
		catx -= 5
	if keys[K_RIGHT]:
		catx += 5
	if keys[K_UP]:
		caty -= 5
	if keys[K_DOWN]:
		caty += 5
	displaysurf.blit(cat_img, (catx, caty))
	pygame.display.update()
	pygame.time.Clock().tick(30)
