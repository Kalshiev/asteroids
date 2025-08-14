import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    while True:
        # Check if the user has closed the window to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Color the entire screen black
        pygame.Surface.fill(screen, (0,0,0))

        # Refresh the screen
        pygame.display.flip()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
