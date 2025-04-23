from circle import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0  # Initialization of
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    
    def shoot(self, shots):
        if self.shoot_timer <= 0:  # Only allow shooting if no cooldown
            # Create a direction vector based on the player's rotation
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            # Scale the direction vector by PLAYER_SHOOT_SPEED
            velocity = direction * PLAYER_SHOOT_SPEED
            # Create a new shot at the player's position
            new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, velocity)
            # Add the shot to the shots group
            shots.add(new_shot)
            # Reset the shoot timer
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        