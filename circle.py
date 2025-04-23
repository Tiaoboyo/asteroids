import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_SHOOT_SPEED

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
        if self.shoot_timer > 0:
            self.shoot_timer -= dt  # Gradually reduce the timer
    
    def collide(self, other):
        distance = self.position.distance_to(other.position)
        if distance <= (self.radius + other.radius):
            return True
        return False
    
    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

