import pygame, sys
from pygame.locals import *

pygame.init()


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
displaysurf = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)
pygame.display.set_caption("Arrow Test")

BLACK = ( 0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)

cat_img = pygame.image.load("cat.png").convert_alpha()
catx = 0
caty = 0
cat_width = cat_img.get_width()
cat_height = cat_img.get_height()

while True:
	displaysurf.fill(WHITE)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	keys = pygame.key.get_pressed()
	if keys[K_LEFT]:
		catx -= 5
		if catx <= 0:
			catx = 0
	if keys[K_RIGHT]:
		catx += 5
		if catx + cat_width > SCREEN_WIDTH:
			catx = SCREEN_WIDTH - cat_width
	if keys[K_UP]:
		caty -= 5
		if caty <= 0:
			caty = 0
	if keys[K_DOWN]:
		caty += 5
		if caty + cat_height > SCREEN_HEIGHT:
			caty = SCREEN_HEIGHT - cat_height
	displaysurf.blit(cat_img, (catx, caty))
	#print (str(cat_img.get_height()))
	pygame.display.update()
	pygame.time.Clock().tick(30)
