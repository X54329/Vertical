import pygame

pygame.init()

window = pygame.display.set_mode( ( 800, 600) )

pygame.display.set_caption( "window")

black = (0, 0, 0)
white = ( 255, 255, 255)

x, y = 380, 549

moveX, moveY = 0, 0
velocityY = 0
accelerationY = .2

clock = pygame.time.Clock()


gameLoop = True
while gameLoop:
	
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			gameLoop = False

		moveY = moveY + velocityY



		if (event.type == pygame.KEYDOWN) :

			if (event.key == pygame.K_LEFT) :
				moveX = -5

			if (event.key == pygame.K_RIGHT) :
				moveX = 5
			
			if (event.key == pygame.K_UP) :
				velocityY = -1

		if (event.type == pygame.KEYUP) :

			if (event.key == pygame.K_LEFT) :
				moveX = 0

			if (event.key == pygame.K_RIGHT) :
				moveX = 0

			if (event.key == pygame.K_UP) :
				velocityY = 1.5 + counter

	window.fill (black)

	pygame.draw.rect( window, white, (x, y, 50, 50) )
	
	pygame.display.flip()
	
	clock.tick(100)

	x = moveX + x

	y = moveY + y
	print moveY

pygame.quit ()

