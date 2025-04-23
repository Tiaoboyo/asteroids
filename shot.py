from circle import CircleShape
from constants import * 

import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        # Initialize the shot at the given x, y position with SHOT_RADIUS
        super().__init__(x, y, radius)
        self.velocity = velocity  # Set the shot's velocity as a pygame.Vector2

    def draw(self, screen):
        # Draw the shot as a white circle
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Update the shot's position based on its velocity
        self.position += self.velocity * dt