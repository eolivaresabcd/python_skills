import pygame
import random

W = 360 # Width of the window
H = 480 # Height of the window
FPS = 30 # Frames per second

# DEFINE COLORS
WHITE = (255, 255, 255) # RGB color for white
BLACK = (0, 0, 0) # RGB color for black
RED = (255, 0, 0) # RGB color for red
GREEN = (0, 255, 0) # RGB color for green
BLUE = (0, 0, 255) # RGB color for blue
YELLOW = (255, 255, 0) # RGB color for yellow
CYAN = (0, 255, 255) # RGB color for cyan
MAGENTA = (255, 0, 255) # RGB color for magenta

# INITIALIZE PYGAME AND CREATE A WINDOW

pygame.init() # Initialize the pygame library
pygame.mixer.init() # Initialize the mixer module for sound
screen = pygame.display.set_mode((W, H)) # Create a window with the specified width and height
pygame.display.set_caption("Pygame Template") # Set the window title
pygame.time.Clock() # Create a clock object to control the frame rate

# GAME LOOP
running = True # Variable to control the game loop
while running:

    # Set the frame rate
    pygame.time.Clock().tick(FPS) # Limit the frame rate to FPS so that the game runs at a consistent speed
                                    # if the game updates slower than the FPS, it will wait until the next frame,
                                    # otherwise we would have lag

    # EVENT HANDLING (AKA PROCESS INPUT)

    for event in pygame.event.get(): # Loop through all events in the event queue
        # check for closing the window by clicking the X button
        if event.type == pygame.QUIT:
            running = False

    # UPDATE THE GAME STATE

    # RENDER THE GAME

    screen.fill(CYAN) # Fill the screen with black color
    # after drawing everything, flip the display
    pygame.display.flip() # Update the display

pygame.quit() # Quit pygame when the game loop ends
