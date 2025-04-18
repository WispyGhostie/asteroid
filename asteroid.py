import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return ASTEROID_MIN_RADIUS
        else:
            angle = random.uniform(20, 50)
            v1,v2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
            a1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            a2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2
            self.kill()
            #return 10

        

