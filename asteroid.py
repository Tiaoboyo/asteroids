from circle import CircleShape
from constants import * 
from main import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, dt):
        self.radius = radius
        self.x = x
        self.y = y
        pygame.draw.circle(self.position, self.radius(), 2)
        self.update.circle(self.velocity * dt)
