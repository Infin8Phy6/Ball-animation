import pygame
import sys
pygame.init()
# set up the screen
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Draw a Ball")
# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# set up the ball
radius = 50
x = 350
y = 250
#this controlls the speed of the ball
speed_x = 5
speed_y = 5

# set up the clock
clock = pygame.time.Clock()
# main loop
# we set the logic for the movement of the ball
while True:
    # check for events
    # check for events

    # clear the screen
    screen.fill(WHITE)

    # move the ball
    x += speed_x
    y += speed_y

    # check for collision with walls
    if x > 650 or x < 50:
        speed_x = -speed_x
    if y > 450 or y < 50:
        speed_y = -speed_y

    # draw the ball
    pygame.draw.circle(screen, BLACK, (x, y), radius)

    # update the screen
    pygame.display.update()

    # set the frame rate
    clock.tick(60)
