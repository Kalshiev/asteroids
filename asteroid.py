from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, coin):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.coin = coin
        self.vertex_list = []

    def rock(self):
        rock_vertex_list = []
        for i in self.vertex_list:
            point = pygame.Vector2(0, 1).rotate(self.rotation + i)
            rock_vertex_list.append(self.position + point * self.radius)
        return rock_vertex_list
    
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
            new_vertex_list1 = []
            for _ in self.vertex_list:
                new_vertex_list1.append(random.randint(100,360))
            new_vertex_list1.sort()
            asteroid1.vertex_list = new_vertex_list1

            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, 1)
            asteroid2.velocity = angle2 * 1.2
            new_vertex_list2 = []
            for _ in self.vertex_list:
                new_vertex_list2.append(random.randint(100,360))
            new_vertex_list2.sort()
            asteroid2.vertex_list = new_vertex_list2