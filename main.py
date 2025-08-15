import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

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

    # Game Loop
    while True:
        # Check if the user has closed the window to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Color the entire screen black
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        # Refresh the screen
        pygame.display.flip()
        # Limit the game's framerate to 60FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
