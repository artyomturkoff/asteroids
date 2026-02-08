import pygame
from logger import log_event
from random import uniform
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = uniform(20, 50)
        new_vector_first = self.velocity.rotate(angle)
        new_vector_second = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_new_asteroid, second_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius), Asteroid(self.position.x, self.position.y, new_radius)
        first_new_asteroid.velocity = new_vector_first * 1.2
        second_new_asteroid.velocity = new_vector_second * 1.2

        