from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, coin):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.coin = coin

    def rock(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        d = self.position + forward * self.radius + right
        return [a, b, c, d]
    
    def rotate(self, dt):
        if self.coin < 0.5:
            self.rotation += dt * self.radius - 2
        else:
            self.rotation -= dt * self.radius - 2
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.rock(), 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rotate(dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            angle1 = self.velocity.rotate(random_angle)
            angle2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, 0)
            asteroid1.velocity = angle1 * 1.2

            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, 1)
            asteroid2.velocity = angle2 * 1.2