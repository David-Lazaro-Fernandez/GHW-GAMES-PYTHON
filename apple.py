import random
import math
import pygame

class Apple: 
    
    def __init__(self, screen):
        self.GRAVITY = 0.1
        self.screen = screen
        self.x = random.randint(0, 300)
        self.y = 0
        self.color = (0, 162, 232)
        self.radius = 10
        self.velocity_y = 0
        self.acceleration_y = self.GRAVITY  # Gravity
    def draw(self):
        apple_image = pygame.image.load("assets/meatballs.png")
        apple_image = pygame.transform.scale(apple_image, (70, 70))
        self.screen.blit(apple_image, (self.x, self.y))

    def fall(self):
        # Update the apple's position
        self.velocity_y += self.acceleration_y
        self.y += self.velocity_y

        if self.y > self.screen.get_height():
            self.y = 0
            self.x = random.randint(0, self.screen.get_width())
            self.velocity_y = 0

    def check_collision(apple, player_pos, player_radius):
        # Calculate the distance between the apple and the player
        distance = math.sqrt((apple.x -  player_pos.x) ** 2 + (apple.y - player_pos.y) ** 2)
        # Check if the distance is less than the sum of the radii (collision)
        if distance <= apple.radius + player_radius:
            return True
        else:
            return False