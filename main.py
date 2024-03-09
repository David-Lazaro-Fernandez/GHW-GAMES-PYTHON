import pygame
import os

frames_folder = os.path.join(os.path.dirname(__file__), "assets", "frames")

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.frame_index = 0
        self.frames = []

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def draw(self, screen):
        # Draw the current frame of the character on the screen
        screen.blit(self.frames[self.frame_index], (self.x, self.y))

# create an instance of the Character class
character = Character(200, 250)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                character.move_left()
            elif event.key == pygame.K_d:
                character.move_right()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    character.animate()
    character.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()