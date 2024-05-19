import pygame
import sys
import random
import CharactersDetails
pygame.mouse.set_visible(False)

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clickable Button")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (168, 127, 71)
HOVER_GRAY = (210, 182, 143)


# Define the Button class
class CharButton:
    def __init__(self, text, position, width, height, action=None):
        self.text = text
        self.initial_position = position
        self.rect = pygame.Rect(position, (width, height))
        self.color = GRAY  # Default color for text
        self.hover_color = HOVER_GRAY  # Color when hovered
        self.clicked_color = BLACK  # Color when clicked
        self.clicked = False
        self.visible = True  # Flag to determine if button is visible
        self.action = action  # Action to perform when clicked

    def draw(self, surface, scroll_offset):
        if self.visible:  # Only draw if visible
            # Adjust the button position based on scroll_offset
            adjusted_position = (self.initial_position[0], self.initial_position[1] + scroll_offset)
            self.rect = pygame.Rect(adjusted_position, self.rect.size)
            font = pygame.font.Font(None, 36)
            font_surface = font.render(self.text, True, self.color)
            font_rect = font_surface.get_rect(center=self.rect.center)
            surface.blit(font_surface, font_rect)

    def check_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color
        else:
            self.color = GRAY  # Reset to default color

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos) and not self.clicked:
            self.clicked = True
            self.color = self.clicked_color
            if self.action:
                self.action()  # Perform the action
            return True
        return False


# Function to perform when the button is clicked
def button_click_action():
    CharactersDetails.centaurs(screen)



# Create a Button object with a custom action
button = CharButton("Click me!", (300, 250), 200, 100, button_click_action)



# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = pygame.mouse.get_pos()
                if button.check_click(pos):
                    button.clicked = False  # Reset the clicked flag
                    button.visible = True  # Make the button visible again

    # Fill the screen with white
    screen.fill(WHITE)

    # Get the current mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the button is hovered or clicked
    button.check_hover(mouse_pos)

    # Draw the button
    button.draw(screen, 0)


    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
