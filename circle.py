import pygame
from main import SCREEN_HEIGHT, SCREEN_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), 2)
        self.triangle()
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        pass
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
             self.rotate(dt)
        if keys[pygame.K_w]:
             self.move(dt)
        if keys[pygame.K_s]:
             self.move(-dt)