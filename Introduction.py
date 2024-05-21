import pygame
import sys
import CharactersDetails
pygame.mouse.set_visible(False)
sound_allowed = True

def play_click_sound(sound_allowed):
    if sound_allowed:
        click_sound.play()

click_sound = pygame.mixer.Sound("resources/sounds/mouse-click-153941.mp3")

def start_game():
    global scroll_speed, sound_allowed
    pygame.init()


    WIDTH, HEIGHT = 1238, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Beyond The Sanctum")
    background = pygame.image.load('resources/images/BG4.png')
    font = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 25)
    font0 = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 30)
    font1 = pygame.font.Font("resources/fonts/Cinzel-VariableFont_wght.ttf", 30)
    font2 = pygame.font.Font("resources/fonts/CinzelDecorative-Regular.ttf", 60)
    font3 = pygame.font.Font("resources/fonts/times new roman italic.ttf", 23)


    scroll_offset = 0
    # Load the image
    original_image = pygame.image.load( "resources/images/LOGOsanctum.png")

    # Set new size for the image
    new_width = 175
    new_height = 175
    resized_image = pygame.transform.scale(original_image, (new_width, new_height))

    t ="beyond the sanctum"
    t1 = "BEYOND THE SANCTUM"
    t2 = "INTRODUCTION "
    text0_1 = "is a game about choices, risk and consequences. Once"
    text0_2 = "you make a choice, there is no going back."
    text0_3 = "Success is never a guarntee. Your journey hinges on a combination of your previous actions, your relationships to others characters, and skill checks."
    text0_4 = "During The adventure, you will embody Aiden, a young rebellious adventurer, thirsty for freedom and exploration, ready to face all challenges to uncover the secrets hidden."
    text1_0 = " Sanctum is a mysterious kingdom where high walls delineate not only the physical border of the territory but also an autonomous world where inhabitants have developed a unique way of life. Driven by commercial exchanges, schools welcome students thirsty for knowledge while surrounding farms provide abundant harvests. History says.. that these imposing walls were erected to protect society from the mysterious man-eating creatures The “ Grimrushers ” that roam beyond, thus imparting a sense of safety, but also endless questions to the population. \n\nYears have passed. And since then, Sanctum has experienced exponential population growth, putting a strain on the already limited resources within its walls. Faced with overpopulation, the leaders of Sanctum were forced to take drastic measures to ensure the survival of their people. Thus, expeditions were regularly launched beyond the walls, comprised of teams of explorers, scientists, farmers, and dedicated physicians.\n"
    text1_1 = "Their mission was twofold: to find new fertile lands where the people could settle and thrive, while unraveling the mystery of the creatures that had haunted rumors for so long.\n\nHowever, despite their courage and determination, none of these expeditions ever returned. The absence of new lands and the disappearance of these teams plunged Sanctum into a deep crisis.\n\nIn this climate of despair and uncertainty, the people of Sanctum needed a leader capable of finding a solution to this crisis."
    text1_2 = "Aiden, the fate of the kingdom rests in your hands. Are you ready to plunge into the heart of this exciting and perilous adventure? Unknown lands and mysteries await to be discovered. Will you dare to defy the darkness and uncover secrets buried for centuries?\n"
    text1_3 = "shame on you"
    text = "Press on Aiden to see Aiden!!"
    text2 = "GAME INSTRUCTIONS"
    text2_1 = " +   You can access the                                   only once, so make sure to set the settings exactly how you want them."
    text2_2 = "Game Menu"
    text2_3 = " +   To scroll down, use the down arrow key, and to scroll up, use the up arrow key."


    class Button:
        def __init__(self, text, position, width, height):
            self.text = text
            self.initial_position = position
            self.rect = pygame.Rect(position, (width, height))
            self.color = (168, 127, 71)  # Default color for text
            self.hover_color = (210,182,143)  # Color when hovered
            self.clicked_color = (0, 0, 0)  # Color when clicked
            self.clicked = False
            self.visible = True  # Flag to determine if button is visible

        def draw(self, surface, scroll_offset):
            if self.visible:  # Only draw if visible
                # Adjust the button position based on scroll_offset
                adjusted_position = (self.initial_position[0], self.initial_position[1] + scroll_offset)
                self.rect = pygame.Rect(adjusted_position, self.rect.size)
                font_surface = font.render(self.text, True, self.color)
                font_rect = font_surface.get_rect(center=self.rect.center)
                surface.blit(font_surface, font_rect)

        def check_hover(self, mouse_pos):
            if self.rect.collidepoint(mouse_pos):
                self.color = self.hover_color
            else:
                self.color = (168, 127, 71)  # Reset to default color

        def check_click(self, mouse_pos):
            if self.rect.collidepoint(mouse_pos) and not self.clicked:
                self.clicked = True
                self.color = self.clicked_color
                #self.visible = False  # Button is no longer visible
                return True
            return False


    class CharButton:
        def __init__(self, text, position, width, height, action=None):
            self.text = text
            self.initial_position = position
            self.rect = pygame.Rect(position, (width, height))
            self.color = (168, 127, 71)  # Default color for text
            self.hover_color = (210, 182, 143)  # Color when hovered
            self.clicked_color = (0,0,0) # Color when clicked
            self.clicked = False
            self.visible = True  # Flag to determine if button is visible
            self.action = action  # Action to perform when clicked

        def draw(self, surface, scroll_offset):
            if self.visible:  # Only draw if visible
                # Adjust the button position based on scroll_offset
                adjusted_position = (self.initial_position[0], self.initial_position[1] + scroll_offset)
                self.rect = pygame.Rect(adjusted_position, self.rect.size)
                font = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 30)
                font_surface = font.render(self.text, True, self.color)
                font_rect = font_surface.get_rect(center=self.rect.center)
                surface.blit(font_surface, font_rect)

        def check_hover(self, mouse_pos):
            if self.rect.collidepoint(mouse_pos):
                self.color = self.hover_color
            else:
                self.color = (168, 127, 71)  # Reset to default color

        def check_click(self, mouse_pos):
            if self.rect.collidepoint(mouse_pos) and not self.clicked:
                self.clicked = True
                self.color = self.clicked_color
                if self.action:
                    self.action()  # Perform the action
                return True
            return False


    class CharButton1:
        def __init__(self, text, position, width, height, action=None):
            self.text = text
            self.initial_position = position
            self.rect = pygame.Rect(position, (width, height))
            self.color = (168, 127, 71)  # Default color for text
            self.hover_color = (210, 182, 143)  # Color when hovered
            self.clicked_color = (0, 0, 0)  # Color when clicked
            self.clicked = False
            self.visible = True  # Flag to determine if button is visible
            self.action = action  # Action to perform when clicked

        def draw(self, surface, scroll_offset):
            if self.visible:  # Only draw if visible
                # Adjust the button position based on scroll_offset
                adjusted_position = (self.initial_position[0], self.initial_position[1] + scroll_offset)
                self.rect = pygame.Rect(adjusted_position, self.rect.size)
                font = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 25)
                font_surface = font.render(self.text, True, self.color)
                font_rect = font_surface.get_rect(center=self.rect.center)
                surface.blit(font_surface, font_rect)

        def check_hover(self, mouse_pos):
            if self.rect.collidepoint(mouse_pos):
                self.color = self.hover_color
            else:
                self.color = (168, 127, 71)  # Reset to default color

        def check_click(self, mouse_pos):
            if self.rect.collidepoint(mouse_pos) and not self.clicked:
                self.clicked = True
                self.color = self.clicked_color
                if self.action:
                    self.action()  # Perform the action
                return True
            return False

    def display_text(surface, text, pos, font, color, scroll_offset):
        max_width = WIDTH - 110  # Maximum line width
        space = font.size(' ')[0]
        line_spacing = 20  # Adjust this value for desired line spacing
        x, y = pos
        words = [word.split(' ') for word in text.splitlines()]
        for line in words:
            for word in line:
                word_surface = font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height + line_spacing
                surface.blit(word_surface, (x, y + scroll_offset))
                x += word_width + space
            x = pos[0]
            y += word_height + line_spacing

    def draw_text_box(surface, position, size, background_color, border_color, alpha1, scroll_offset):
        # Define the padding and border width
        padding = 15
        border_width = 1

        # Adjust the position based on the scroll offset
        adjusted_position = (position[0], position[1] + scroll_offset)

        # Create a transparent surface for the box
        box_surface = pygame.Surface(size, pygame.SRCALPHA)
        box_surface.fill((*background_color, alpha1))

        # Draw the border rectangle on the transparent surface
        border_rect = pygame.Rect((0, 0), size)
        pygame.draw.rect(box_surface, border_color, border_rect, border_width)

        # Blit the box surface onto the main surface
        surface.blit(box_surface, adjusted_position)


    # Function to display text with word wrapping
    def display_text(surface, text, pos, font, color, scroll_offset):
        max_width = WIDTH - 110  # Maximum line width
        space = font.size(' ')[0]
        line_spacing = 20  # Adjust this value for desired line spacing
        x, y = pos
        words = [word.split(' ') for word in text.splitlines()]
        for line in words:
            for word in line:
                word_surface = font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height + line_spacing
                surface.blit(word_surface, (x, y + scroll_offset))
                x += word_width + space
            x = pos[0]
            y += word_height + line_spacing


    def draw_text_box(surface, position, size, background_color, border_color, alpha1, scroll_offset):
        # Define the padding and border width
        padding = 15
        border_width = 1

        # Adjust the position based on the scroll offset
        adjusted_position = (position[0], position[1] + scroll_offset)

        # Create a transparent surface for the box
        box_surface = pygame.Surface(size, pygame.SRCALPHA)
        box_surface.fill((*background_color, alpha1))

        # Draw the border rectangle on the transparent surface
        border_rect = pygame.Rect((0, 0), size)
        pygame.draw.rect(box_surface, border_color, border_rect, border_width)

        # Blit the box surface onto the main surface
        surface.blit(box_surface, adjusted_position)

    # Function to display image and text with gradual appearance and disappearance
    def display_image_and_text_slow(image_path, text, duration, image_position, text_position):
        alpha = 0
        increment = 5  # Increment alpha value by 5 each frame

        # Load image and scale
        image = pygame.image.load(image_path)
        image_width, image_height = image.get_size()
        image = pygame.transform.scale(image, (200, 200))  # Scale the image to the desired size

        # Render text surface
        text_surface = font2.render(text, True, (255,255,255))
        text_width, text_height = text_surface.get_size()

        # Initial positions
        image_x, image_y = image_position
        text_x, text_y = text_position

        while alpha <= 255:
            screen.fill((0, 0, 0))


            # Set alpha for image
            image.set_alpha(alpha)
            screen.blit(image, (image_x, image_y))

            # Set alpha for text
            text_surface.set_alpha(alpha)
            screen.blit(text_surface, (text_x, text_y))

            pygame.display.flip()  # Update the display
            pygame.time.delay(50)  # Delay to control the speed of appearance
            alpha += increment

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return

        pygame.time.delay(duration * 1000)  # Delay without blocking

        while alpha >= 0:
            screen.fill((0, 0, 0))


            # Set alpha for image
            image.set_alpha(alpha)
            screen.blit(image, (image_x, image_y))

            # Set alpha for text
            text_surface.set_alpha(alpha)
            screen.blit(text_surface, (text_x, text_y))

            pygame.display.flip()  # Update the display
            pygame.time.delay(50)  # Delay to control the speed of disappearance
            alpha -= increment

    def button_click_action():
        CharactersDetails.Aiden(screen,sound_allowed)
    def button1_click_action():
        CharactersDetails.Sanctum(screen,sound_allowed)

    def button2_click_action():
        CharactersDetails.Grimrushers(screen,sound_allowed)

    def draw_line(surface, x1, y1, x2, y2, width, color, scroll_offset, visible=True):
        if visible:
            pygame.draw.line(surface, color, (x1, y1 + scroll_offset), (x2, y2 + scroll_offset), width)

    button0 = Button(" →", (980, 500), 200, 50)
    button1 = Button(" →", (980, 500), 200, 50)
    button2 = Button(" →", (980, 500), 200, 50)
    button8 = Button(" →", (980, 500), 200, 50)
    button3 = Button(">  Continue.", (120, 915), 200, 50)
    button4 = Button(">  Continue.", (120, 600), 200, 50)
    button5 = Button(">  YES.", (120, 450), 200, 40)
    button6 = Button(">  NO.", (120, 490), 200, 40)
    button7 = Button("→ Bye", (490, 480), 200, 50)
    Aiden = CharButton(" Aiden", (522, 346), 200, 50, button_click_action)
    Sanctum = CharButton1(" Sanctum", (55, 220), 200, 50, button1_click_action)
    Grimrushers = CharButton1(" Grimrushers", (435, 435), 200, 50, button2_click_action)

    scroll_speed = 50
    done = False
    done1 = False
    done2 = False
    done3 = False
    done4 = False
    done5 = False
    done6 = False
    done7 = False
    done8 = False
    display_text0 = True



    image_path = "resources/images/logo.png"
    target_size = (450, 450)
    display_image_and_text_slow(image_path, t1, 1, image_position=(500, 90), text_position=(240, 350))
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    while True:

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            elif events.type == pygame.MOUSEBUTTONDOWN:
                play_click_sound(sound_allowed)
                if button0.check_click(mouse_pos):
                    done = True
                    scroll_offset = 0
                elif button1.check_click(mouse_pos) and done:
                    done1 = True
                    scroll_offset = 0  # Reset scroll offset to display text from the beginning
                elif button2.check_click(mouse_pos) and done1:
                    done2 = True
                    scroll_offset = 0
                elif button3.check_click(mouse_pos) and done8:
                    done3 = True
                    line_visible = False  # Hide the line when "Continue" is clicked
                    scroll_offset = 0
                elif button4.check_click(mouse_pos) and done3:
                    done4 = True
                    line_visible = False  # Hide the line when "Continue" is clicked
                    scroll_offset = 0
                elif button5.check_click(mouse_pos) and done4:
                    done5 = True
                    line_visible = False  # Hide the line when "Continue" is clicked
                    scroll_offset = 0
                elif button6.check_click(mouse_pos) and done4:
                    done6 = True
                    line_visible = False  # Hide the line when "Continue" is clicked
                    scroll_offset = 0
                elif button7.check_click(mouse_pos) and done6:
                    done7 = True
                    line_visible = False  # Hide the line when "Continue" is clicked
                    scroll_offset = 0
                elif button8.check_click(mouse_pos) and done2 :
                    done8 = True
                    line_visible = False  # Hide the line when "Continue" is clicked
                    scroll_offset = 0

                elif Aiden.check_click(mouse_pos) :
                    Aiden.clicked = False  # Reset the clicked flag
                    Aiden.visible = True  # Make the button visible again

                elif Sanctum.check_click(mouse_pos) :
                    Sanctum.clicked = False  # Reset the clicked flag
                    Sanctum.visible = True  # Make the button visible again
                elif Grimrushers.check_click(mouse_pos) :
                    Grimrushers.clicked = False  # Reset the clicked flag
                    Grimrushers.visible = True  # Make the button visible again

        button1.check_hover(mouse_pos)
        button0.check_hover(mouse_pos)
        button2.check_hover(mouse_pos)
        button3.check_hover(mouse_pos)
        button4.check_hover(mouse_pos)
        button5.check_hover(mouse_pos)
        button6.check_hover(mouse_pos)
        button7.check_hover(mouse_pos)
        button8.check_hover(mouse_pos)
        Aiden.check_hover(mouse_pos)
        Sanctum.check_hover(mouse_pos)
        Grimrushers.check_hover(mouse_pos)

        if display_text0:
            draw_text_box(screen, (90, 120), (1040, 450), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            screen.blit(resized_image, (500, 120 + scroll_offset))
            display_text(screen, t, (120, 350), font1, (168, 127, 71), scroll_offset)
            display_text(screen, text0_1, (460, 350), font0, (255, 255, 255), scroll_offset)
            display_text(screen, text0_2, (120, 400), font0, (255, 255, 255), scroll_offset)
            button0.draw(screen, scroll_offset)
        if done:
            display_text0 = False
            draw_text_box(screen, (90, 120), (1040, 450), (50, 50, 50), (109, 69, 38), 120, scroll_offset)
            screen.blit(resized_image, (500, 120 + scroll_offset))
            display_text(screen, text0_3, (120, 350), font0, (255,255,255), scroll_offset)
            button1.draw(screen, scroll_offset)

        if done1:
            done = False

            draw_text_box(screen, (90, 120), (1040, 450), (50, 50, 50), (109, 69, 38), 120, scroll_offset)
            screen.blit(resized_image, (500, 120 + scroll_offset))
            display_text(screen, text0_4, (120, 350), font0, (255, 255, 255), scroll_offset)
            display_text(screen, text, (140, 495), font3, (205, 210, 155), scroll_offset)
            Aiden.draw(screen, scroll_offset)
            button2.draw(screen, scroll_offset)
        if done2:
            done1 = False
            Aiden.clicked = True
            draw_text_box(screen, (90, 120), (1040, 450), (50, 50, 50), (109, 69, 38), 120, scroll_offset)
            display_text(screen, text2, (130, 150), font1, (168, 127, 71), scroll_offset)
            display_text(screen, text2_1, (120, 280), font0, (255, 255, 255), scroll_offset)
            display_text(screen, text2_2, (380, 280),font1, (168, 127, 71), scroll_offset)
            display_text(screen, text2_3, (120, 420), font0, (255, 255, 255), scroll_offset)
            button8.draw(screen, scroll_offset)



        if done8:
            done2 = False
            draw_text_box(screen, (90, 60), (1050, 950), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, t2, (130, 110), font2, (168, 127, 71), scroll_offset)
            display_text(screen, "Press on Sanctum or Grimrushers to see the Sanctum and know more about these creatures!!", (150, 830), font3, (205, 210, 155), scroll_offset)
            display_text(screen, text1_0, (110, 230), font, 'white', scroll_offset)
            line_visible = True
            draw_line(screen, 130, HEIGHT + 190, WIDTH - 130, HEIGHT + 190, 1, (109, 69, 38), scroll_offset,line_visible)
            button3.draw(screen, scroll_offset)
            Sanctum.draw(screen, scroll_offset)
            Grimrushers.draw(screen, scroll_offset)

        if done3:
            done8 = False
            Sanctum.clicked = True
            Grimrushers.clicked = True
            draw_text_box(screen, (90, 60), (1050, 630), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text1_1, (110, 110), font, 'white', scroll_offset)
            draw_line(screen, 130, HEIGHT - 130, WIDTH - 130, HEIGHT - 130, 1, (109, 69, 38), scroll_offset,line_visible)
            button4.draw(screen, scroll_offset)

        if done4:
            done3 = False
            draw_text_box(screen, (90, 120), (1040, 450), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text1_2, (110, 200), font, 'white', scroll_offset)
            line_visible = True
            draw_line(screen, 130, HEIGHT - 290, WIDTH - 130, HEIGHT - 290, 1, (109, 69, 38), scroll_offset,line_visible)
            button5.draw(screen, scroll_offset)
            button6.draw(screen, scroll_offset)
        if done5:
            import my_game
            my_game.main_menu()
        elif done6:

            done4 = False
            draw_text_box(screen, (90, 120), (1040, 450), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text1_3, (380, 300), font2, (255, 255, 255), scroll_offset)
            button7.draw(screen, scroll_offset)
        if done7:
            break

        cursor_img = pygame.image.load('resources/images/Sans titre.png')
        cursor_img = pygame.transform.scale(cursor_img, (40, 40))  # Resize cursor image
        cursor_pos = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_pos)


        pygame.display.update()
        pygame.display.flip()

        # Scrolling functionality
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            # Check if scrolling up goes beyond the beginning of the text
            if scroll_offset + scroll_speed <= 0:
                scroll_offset += scroll_speed
        if keys[pygame.K_DOWN]:
            scroll_offset -= scroll_speed

start_game()
