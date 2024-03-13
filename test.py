import pygame
import os
# Traverse through all the images in the folder
character_running_frames = []
character_running_folder_path = "assets/frames/character_running"
for filename in os.listdir(character_running_folder_path):
    if filename.endswith(".gif"):
        image_path = os.path.join(character_running_folder_path, filename)
        image = pygame.image.load(image_path)
        character_running_frames.append(image)

print(character_running_frames)