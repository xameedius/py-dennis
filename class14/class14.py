
# To install any module that does not come with python use a package manager or do it manually
#USe pip to install a module

# Verify Installation
# print(pygame.__version__)

# Things to Learn Today
# 1) Install Pygame (Or any Module)
# 2) Create a basic game window
# 3) Unserstand the gameloop
# 4) Handle Quitting the game properly

# pygame.init() --> Initilizes Pygame
# pygame.display.set_mode((WIDTH,HEIGHT)) --> Creates a window
# pygame.display.set_caption("Title") --> Sets the Window Title
# pygame.event.get() --> Checks for user input
# pygame.QUIT() --> Allows the user to close the Window

import pygame

# Initilize Pygame
pygame.init()

# Set window size
WIDTH , HEIGHT = 800 , 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Set Window Title
pygame.display.set_caption("My first Pygame Window")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # Exit game loop

    # Everything Else comes here
    screen.fill((255, 204, 0)) # Fill screen with blue color
    pygame.display.update() # Update the display

pygame.quit()  # Close Pygame properly



