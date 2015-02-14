"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

From:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example

Explanation video: http://youtu.be/8IRyt7ft7zg

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""

import pygame
from pybrain.optimization import * 
import numpy
# -- Global constants

num_ai_steps = 100
outer_steps = numpy.array(0 for i in range(0,num_ai_steps)) # I was thinking 1=up, 2=down,3=left,4=right
outer_steps.resize(100)
i=0
# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)

# Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player controls. """

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None


    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('Test')

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

# Create the player paddle object
player = Player(50, 500)
player.walls = wall_list
all_sprite_list.add(player)

clock = pygame.time.Clock()


def see_height(steps):
 done = False
 print "seeing height reached"
 player.rect.x = 50
 player.rect.y = 500
 i=0
 while not done:

     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             done = True

         else:
            if steps[i]==3:
                player.changespeed(-3, 0)
            elif steps[i]==4:
                player.changespeed(3, 0)
            elif steps[i]==1:
                player.changespeed(0, -3)
            elif steps[i]==2:
                player.changespeed(0, 3)
	    else:
		player.changespeed(0,0)
     if (i<num_ai_steps-1):
        i=i+1
     else:
	steps[i]=0 #Stop when we're done
	print "We're done"
	return 600-player.rect.y
     all_sprite_list.update()

     screen.fill(BLACK)

     all_sprite_list.draw(screen)

     pygame.display.flip()

     clock.tick(60)
 return 0

#see_height(outer_steps)
l = GA(see_height, outer_steps)
l.maxEvaluations = 10
print l.learn()
print "WTF"

