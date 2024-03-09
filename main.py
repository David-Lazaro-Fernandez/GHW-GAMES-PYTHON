# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup

class Apple: 
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(0, 300)
        self.y = 50
        self.color = (0, 162, 232)
        self.radius = 10

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


pygame.init()
screen = pygame.display.set_mode((300, 500))
clock = pygame.time.Clock()
running = True
dt=0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
apple = Apple(screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "red", player_pos, 40)
    apple.draw()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    # flip() the display to put your work on screen
    pygame.display.flip()

    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()