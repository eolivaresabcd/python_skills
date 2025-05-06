import pygame
import random

W = 800 # Width of the window
H = 600 # Height of the window
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

# CREATE PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Initialize the sprite class
        self.image = pygame.Surface((50, 50)) # image of the player
        self.image.fill(GREEN) # Fill the image with green color
        self.rect = self.image.get_rect() # Get the rectangle of the image
        self.rect.center = (W // 2, H // 2) # Set the position of the player to the center of the window

    def update(self):
        self.rect.x += random.randint(-50, 50) # Move the player randomly in the x direction
        self.rect.y += random.randint(-50, 50) # Move the player randomly in the y direction
        if self.rect.x < 0: # If the player goes out of the left side of the window
            self.rect.x = 0 # Set the x position to 0
        if self.rect.x > W - self.rect.width:
            self.rect.x = W - self.rect.width
        if self.rect.y < 0: # If the player goes out of the top side of the window
            self.rect.y = 0 # Set the y position to 0
        if self.rect.y > H - self.rect.height:
            self.rect.y = H - self.rect.height

# INITIALIZE PYGAME AND CREATE A WINDOW
pygame.init() # Initialize the pygame library
pygame.mixer.init() # Initialize the mixer module for sound
screen = pygame.display.set_mode((W, H)) # Create a window with the specified width and height
pygame.display.set_caption("Pygame Template") # Set the window title
pygame.time.Clock() # Create a clock object to control the frame rate

all_sprites = pygame.sprite.Group() # Create a group to hold all sprites
player = Player() # Create a player object
all_sprites.add(player) # Add the player to the group of sprites

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

    all_sprites.update() # Update all sprites in the group

    # RENDER THE GAME

    screen.fill(BLACK) # Fill the screen with black color
    all_sprites.draw(screen) # Draw all sprites in the group on the screen
    # after drawing everything, flip the display
    pygame.display.flip() # Update the display

pygame.quit() # Quit pygame when the game loop ends
