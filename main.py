import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from utils import draw_text
from config.fonts import POINT_FONT

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # Fonts
    point_font = pygame.font.Font(POINT_FONT, 25)

    # Pygame groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    # Create a player with the Player class
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Delta Time
    dt = 0

    # Points counter
    points = 0

    # Game Loop
    while True:
        # Check if the user has closed the window to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Color the entire screen black
        screen.fill("black")

        draw_text(str(points), point_font, "white", screen, 50, 50)

        for item in drawable:
            item.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                print(f"Points: {points}")
                sys.exit()
            
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                    points += 10

        # Refresh the screen
        pygame.display.flip()
        # Limit the game's framerate to 60FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
