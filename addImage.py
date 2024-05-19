import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Resized Image Example")

TEXT0 = "BEYOND THE SANCTUM "
TEXT1 = "is a game about choices, risk and consequences. Once you make a choice, there is no going back."
# Load the image
original_image = pygame.image.load("LOGOsanctum.png")  # Replace "your_image_file.png" with the path to your image file
original_width, original_height = original_image.get_size()

# Set new size for the image
new_width = 175
new_height = 175
resized_image = pygame.transform.scale(original_image, (new_width, new_height))

# Set position of the image
image_x = 300
image_y = 30

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill with white

    # Draw the resized image
    screen.blit(resized_image, (image_x, image_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
