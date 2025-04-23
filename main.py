# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroids import *
from shot import *
from circle import *

def main():
    #Screen Details
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    fps = 60
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Create Containers for Player Class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    #Game Loop
    while True:
        pygame.Surface.fill(screen, (0,0,0))
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              return
        dt = clock.tick(fps) / 1000

            # **Handle Input: Spacebar to shoot**
        keys = pygame.key.get_pressed()  # Check current key states
        if keys[pygame.K_SPACE]:  # If spacebar is pressed
            player.shoot(shots)  # Call the shoot method

        #Updateable characters
        updatable.update(dt)

        #Drawable Characters
        for entity in drawable:
            entity.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.collide(player):
                sys.exit("Game Over!")
        
        for shot in shots:  # Loop over every shot in the game
            for asteroid in asteroids:  # Compare it to every asteroid
                if asteroid.collides_with(shot):  # Check for a collision
                    shot.kill()  # Remove the shot on impact
                    asteroid.split()  # Remove the asteroid

        pygame.display.flip()


if __name__ == "__main__":
    main()
