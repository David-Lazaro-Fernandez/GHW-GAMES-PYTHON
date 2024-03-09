# Example file showing a basic pygame "game loop"
import pygame
from apple import Apple

# pygame setup
pygame.init()
screen = pygame.display.set_mode((300, 500))
clock = pygame.time.Clock()

# Load images
background = pygame.image.load("assets/background field.png")
background = pygame.transform.scale(background, (300, 500))

running = True
dt=0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 40  # Define this near where you initialize player_pos
apple = Apple(screen)
apple_list = []
apple_generation_timer = 0



while running:
    print(apple_generation_timer)
    if apple_generation_timer > 100:
        apple_list.append(Apple(screen)) 
        apple_generation_timer = 0
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background, (0, 0))

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "red", player_pos, player_radius)

    # Draw all apples
    for simple_apple in apple_list:
        simple_apple.fall()  
        simple_apple.draw()

        if Apple.check_collision(simple_apple, player_pos, player_radius):
            print("Collision detected!")
            # Handle the collision (e.g., reset the apple, update the score, etc.)
            apple_list.remove(simple_apple)  # Example: remove the apple from the list
        
        

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
    apple_generation_timer += 1
pygame.quit()