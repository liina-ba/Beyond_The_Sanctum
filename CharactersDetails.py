import time
import pygame
from pygame import QUIT
import sys
pygame.init()

def play_click_sound(sound_allowed):
    if sound_allowed:
        click_sound.play()
click_sound = pygame.mixer.Sound("resources/sounds/mouse-click-153941.mp3")

pygame.init()
font1 = pygame.font.Font("resources/fonts/Cinzel-VariableFont_wght.ttf", 20)
font2 = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 25)

def display_multiline_text(window, font, text, color, x, y,timeSleep=2):
    lines = text.split('\n')
    rendered_lines = [font.render(line, True, color) for line in lines]
    for i, rendered_line in enumerate(rendered_lines):
        window.blit(rendered_line, (x, y + i * font.get_linesize()))

def typewriter_effect(surface, font, message, position, color=(255, 255, 255), delay=0.05, callback=None):
    for i, char in enumerate(message):
        surface.blit(font.render(char, True, color), position)
        pygame.display.update()
        pygame.time.wait(int(delay * 1000))  # Delay in milliseconds
        position = (position[0] + font.size(char)[0], position[1])  # Move to the next character
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
    if callback:
        callback()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

def draw_text_box(surface, position, size, background_color, border_color, alpha):
    # Define the padding and border width
    padding = 15
    border_width = 1

    # Adjust the position based on the scroll offset
    adjusted_position = (position[0], position[1] )

    # Create a transparent surface for the box
    box_surface = pygame.Surface(size, pygame.SRCALPHA)
    box_surface.fill((*background_color, alpha))

    # Draw the border rectangle on the transparent surface
    border_rect = pygame.Rect((0, 0), size)
    pygame.draw.rect(box_surface, border_color, border_rect, border_width)

    # Blit the box surface onto the main surface
    surface.blit(box_surface, adjusted_position)


class Button:
    def __init__(self, text, position, width, height):
        self.text = text
        self.initial_position = position
        self.rect = pygame.Rect(position, (width, height))
        self.color = (168, 127, 71)  # Default color for text
        self.hover_color = (210, 182, 143)  # Color when hovered
        self.clicked_color = (0, 0, 0)  # Color when clicked
        self.clicked = False
        self.visible = True  # Flag to determine if button is visible

    def draw(self, surface):
        if self.visible:  # Only draw if visible
            # Adjust the button position based on scroll_offset
            adjusted_position = (self.initial_position[0], self.initial_position[1] )
            self.rect = pygame.Rect(adjusted_position, self.rect.size)
            font_surface = font2.render(self.text, True, self.color)
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
            self.visible = False  # Button is no longer visible
            return True
        return False


def centaurs(screen,sound_allowed):

    font1 = pygame.font.Font("resources/fonts/Cinzel-VariableFont_wght.ttf", 20)
    font2 = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 25)
    background = pygame.image.load("resources/images/BG4.png")
    centaur1 = pygame.image.load("resources/images/centaur1.png")
    centaur1_2 = pygame.image.load("resources/images/centaur1_2.png")

    newCentaurs = """
        Centaurs, majestic beings of myth and legend,embody the fusion of human intellect and equine grace
        Their upper bodies resemble those of humans,with muscular torsos, broad shoulders, and expressive faces 
        reflecting wisdom earned through ages. 
        Below the waist, powerful horse bodies extend,adorned with sleek coats and flowing manes that ripple 
        in the wind as they gallop across the land.
        With keen senses and unparalleled agility,centaurs navigate both forest and field with effortless grace """

    centaures2 = """
        embodying a harmonious balance between strength and grace
        Their society values tradition and honor
        often led by wise elders who guide their communities with timeless wisdom
        Despite their formidable appearance
        centaurs are known for their deep connection to nature 
        and their affinity for song, dance, and storytelling.
        They are both guardians of the wilderness and keepers of ancient lore
        embodying the timeless spirit of the untamed world.
        """
    running = True

    CtnReading = Button("> Continue Reading", (150, 500), 210, 50)
    back=Button("> Back to the game",(150,520),200,50)
    done = False
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_click_sound(sound_allowed)
                if CtnReading.check_click(mouse_pos):
                    done = True
                elif back.check_click(mouse_pos):
                    return True

        screen.blit(background, (0, 0))
        draw_text_box(screen, (90, 90), (1060, 520), (50, 50, 50), (109, 69, 38), 130)
        display_multiline_text(screen, font2, newCentaurs, (255, 255, 255), 100, 90)
        screen.blit(centaur1, (750, 300))
        CtnReading.draw(screen)
        CtnReading.check_hover(mouse_pos)

        if done:
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))  # Fill screen with black
            draw_text_box(screen, (90, 90), (1060, 520), (50, 50, 50), (109, 69, 38), 130)
            display_multiline_text(screen, font2, centaures2, (255, 255, 255), 100, 95)
            screen.blit(centaur1_2, (700, 120))
            back.draw(screen)
            back.check_hover(mouse_pos)

        cursor_img = pygame.image.load('resources/images/Sans titre.png')
        cursor_img = pygame.transform.scale(cursor_img, (40, 40))  # Resize cursor image
        cursor_pos = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_pos)
        pygame.mouse.set_visible(False)
        pygame.display.flip()

    return True


def Aiden(screen,sound_allowed):

    background = pygame.image.load("resources/images/BG4.png")
    Aiden = pygame.image.load("resources/images/Aiden3.png")
    resized_image = pygame.transform.scale(Aiden, (443, 580))

    running = True

    back = Button(" Return Back", (500, 640), 200, 50)

    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_click_sound(sound_allowed)
                if back.check_click(mouse_pos):
                    return True

        screen.blit(background, (0, 0))
        draw_text_box(screen, (400, 60), (450, 585), (50, 50, 50), (109, 69, 38), 120)
        screen.blit(resized_image, (403, 63))
        back.check_hover(mouse_pos)
        back.draw(screen)

        cursor_img = pygame.image.load('resources/images/Sans titre.png')
        cursor_img = pygame.transform.scale(cursor_img, (40, 40))  # Resize cursor image
        cursor_pos = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_pos)
        pygame.mouse.set_visible(False)


        pygame.display.flip()



    return True

def Sanctum (screen,sound_allowed):

    pygame.init()
    screen = pygame.display.set_mode((1238, 700), pygame.RESIZABLE)
    font1 = pygame.font.Font("resources/fonts/Cinzel-VariableFont_wght.ttf", 20)
    background = pygame.image.load("resources/images/BG4.png")
    msg = " Sanctum Seen From The Sky"

    img1 = pygame.image.load("resources/images/SanctumVueCiel.jpg")
    backButton = Button(" Return Back", (500, 570), 200, 50)



    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_click_sound(sound_allowed)
                if backButton.check_click(mouse_pos):
                    return True

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(img1, (250, 114))
        display_multiline_text(screen, font1, msg, (255, 255, 255), 460, 50)
        backButton.draw(screen)
        backButton.check_hover(mouse_pos)

        cursor_img = pygame.image.load('resources/images/Sans titre.png')
        cursor_img = pygame.transform.scale(cursor_img, (40, 40))  # Resize cursor image
        cursor_pos = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_pos)
        pygame.mouse.set_visible(False)
        pygame.display.update()

    return True


def BethDescreption(screen, sound_allowed):
    pygame.init()
    screen = pygame.display.set_mode((1238, 700), pygame.RESIZABLE)
    background = pygame.image.load("resources/images/BG4.png")
    font2 = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 25)

    Beth_Descreption = """
    Beth, or Elizabeth, the tribe's revered elder,exudes wisdom and experience. 
    Her weathered face tells stories of trials endured and lessons learned. 
    She holds deep knowledge of the Grimrushers,the tribe's menacing foes. 
    Yet, she also carries the prophecy of the savior who will deliver them. 
    With a voice both authoritative and gentle
    she guides her people with fairness and compassion. 
    Though aged, Elizabeth remains a steadfast presence 
    vigilant for signs of the prophecy's fulfillment 
    and determined to see her tribe through to victory.

   """
    detail = " Details about Beth also know as Elizabeth : "
    old_woman = pygame.image.load("resources/images/beth.png")
    backBtn = Button("> Back to the game", (140, 470), 200, 50)

    running = True
    while running:  # this loop is to check if the game is closed or no
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_click_sound(sound_allowed)
                if backBtn.check_click(mouse_pos):
                    return True

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        draw_text_box(screen, (90, 90), (1060, 480), (50, 50, 50), (109, 69, 38), 130)
        display_multiline_text(screen, font2, Beth_Descreption, "white", 100, 90)
        backBtn.draw(screen)
        backBtn.check_hover(mouse_pos)
        screen.blit(old_woman, (850, 150))

        cursor_img = pygame.image.load('resources/images/Sans titre.png')
        cursor_img = pygame.transform.scale(cursor_img, (40, 40))  # Resize cursor image
        cursor_pos = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_pos)
        pygame.mouse.set_visible(False)
        pygame.display.update()

    return True


def CryptedLetter(screen, sound_allowed):
     pygame.init()
     screen = pygame.display.set_mode((1238, 700), pygame.RESIZABLE)
     background = pygame.image.load("resources/images/BG4.png")
     backButton= Button("> Back to the game",(490,550),200,50)
     Crypted_Letter= pygame.image.load("resources/images/new crypted letter.png")


     running = True
     while running :

           mouse_pos = pygame.mouse.get_pos()
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   running = False
               elif event.type == pygame.MOUSEBUTTONDOWN:
                   play_click_sound(sound_allowed)
                   if backButton.check_click(mouse_pos):
                       return True

           screen.fill((0, 0, 0))
           screen.blit(background, (0, 0))
           screen.blit(Crypted_Letter,(300,100))
           backButton.draw(screen)
           backButton.check_hover(mouse_pos)

           cursor_img = pygame.image.load('resources/images/Sans titre.png')
           cursor_img = pygame.transform.scale(cursor_img, (40, 40))  # Resize cursor image
           cursor_pos = pygame.mouse.get_pos()
           screen.blit(cursor_img, cursor_pos)
           pygame.mouse.set_visible(False)


           pygame.display.update()
           pygame.display.flip()
     return True

def RoyalCeremony(screen,sound_allowed):
     pygame.init()
     pygame.display.set_caption("Beyond The Sanctum")
     screen = pygame.display.set_mode((1238, 700), pygame.RESIZABLE)
     font0 = pygame.font.Font("resources/fonts/times new roman italic.ttf", 20)
     background = pygame.image.load("resources/images/BG4.png")
     royal_ceremony=pygame.image.load("resources/images/RoyalCeremony.jpg")
     backButton= Button("> Back to the game",(500,620),200,50)
     running = True
     royal = """
     In the heart of the grand palace, under the gaze of the morning sun, the Royal Ceremony unfolds
     with solemn majesty. Clad in robes of regal splendor, the king presides over ancient blessings,
     receives gifts from distant lands, and speaks words of wisdom that echo through the hallowed halls. 
     It is a tapestry of tradition and reverence, weaving together 
     the past, present, and future of the kingdom in a moment of shared devotion and unity.
     """

     while running:

         mouse_pos = pygame.mouse.get_pos()
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False
             elif event.type == pygame.MOUSEBUTTONDOWN:
                 play_click_sound(sound_allowed)
                 if backButton.check_click(mouse_pos):
                     return True


         screen.fill((0, 0, 0))
         screen.blit(background, (0, 0))  # Fill screen with black
         screen.blit(royal_ceremony,(180,90))
         draw_text_box(screen, (180, 420), (885, 200), (0,0,0), (0,0,0), 180)
         display_multiline_text(screen, font0, royal, (255, 255, 255),200, 425)
         backButton.draw(screen)
         backButton.check_hover(mouse_pos)

         cursor_img = pygame.image.load('resources/images/Sans titre.png')
         cursor_img = pygame.transform.scale(cursor_img, (40, 40))  # Resize cursor image
         cursor_pos = pygame.mouse.get_pos()
         screen.blit(cursor_img, cursor_pos)
         pygame.mouse.set_visible(False)

         pygame.display.update()
         pygame.display.flip()
     return True


def Grimrushers(screen, sound_allowed):
    pygame.init()
    pygame.display.set_caption("Beyond The Sanctum")
    screen = pygame.display.set_mode((1238, 700), pygame.RESIZABLE)
    font1 = pygame.font.Font("resources/fonts/Cinzel-VariableFont_wght.ttf", 23)
    font2 = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 25)
    background = pygame.image.load("resources/images/BG4.png")
    king = pygame.image.load("resources/images/KingGrim.png")
    king_msg = """
     King Of Grimrushers 
     """
    Friendly_grim = pygame.image.load("resources/images/GoodGrim2.png")
    grim_msg1 = """ 
     A Friendly Grimrusher
     """
    ferocious_grim = pygame.image.load("resources/images/StrongGrim21.png")
    grim_msg2 = """
     Ferocious Grimrusher
     """
    armyGrim_msg = """ 
     This Picture shows the Brutality 
     and barbarism of Grimrushers 
     They are Savage 
     devoid of  Mercy and Pity
     embodying sheer savagery
     """
    army_Grimrusher = pygame.image.load("resources/images/Army Grim1.png")
    backButton = Button("> Back to the game", (500, 620), 200, 50)
    ContiueBtn = Button("> continue reading about grimrushers", (470, 630), 200, 50)
    Grimrushers_Description1 = """
     Grimrushers, sinister predators, evoke horror and nightmare in the world of human beings.
     Their malicious and bloodthirsty nature is revealed in their imposing appearance,    
     which can measure 2 to 4 meters in height. 
     Once, before their transformation  by an inexplicable phenomenon into monsters 
     devoid of compassion, these creatures were ordinary humans These titanic and monstrous
     beings possess prodigious agility as well as impressive strength 
     their sharp claws being able to easily pierce even the strongest armor. 
     Their mere presence generates an aura of terror freezing anyone who crosses their path
     in a state of intense fear.
     """
    ButtonGRim1 = Button("> Continue Reading", (180, 480), 200, 50)
    ButtonGrimPics = Button("> click to see Grimrushers", (200, 500), 200, 50)
    Grimrushers_Description2 = """

     Their skin, like a macabre canvas, comes in two distinct shades : 
     
     some Grimrushers have ghostly white skin, while others have putrid green skin. 
     This chromatic difference adds to their mystery and horror, symbolizing the 
     diversity of their evil species  Due to their exceptional intelligence,
     these creatures used this asset as a tool  of domination, allowing 
     them to establish a ruthless reign  and subjugate the sanctum for decades
     """
    anotherGrim = pygame.image.load("resources/images/shortGrim.png")
    running = True
    Donediscription1 = False
    grimWindow = False
    armyGrim = False
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_click_sound(sound_allowed)
                if ButtonGRim1.check_click(mouse_pos):
                    Donediscription1 = True
                elif ButtonGrimPics.check_click(mouse_pos):
                    grimWindow = True
                elif ContiueBtn.check_click(mouse_pos):
                    armyGrim = True
                elif backButton.check_click(mouse_pos):
                     return True

        # First description
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))  # Fill screen with black
        draw_text_box(screen, (90, 90), (1040, 480), (50, 50, 50), (109, 69, 38), 130)
        display_multiline_text(screen, font2, Grimrushers_Description1, (255, 255, 255), 120, 110)
        ButtonGRim1.draw(screen)
        ButtonGRim1.check_hover(mouse_pos)

        # Second Description
        if Donediscription1:
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))  # Fill screen with black
            draw_text_box(screen, (90, 90), (1040, 520), (50, 50, 50), (109, 69, 38), 130)
            display_multiline_text(screen, font2, Grimrushers_Description2, (255, 255, 255), 110, 120)
            ButtonGrimPics.draw(screen)
            ButtonGrimPics.check_hover(mouse_pos)
            screen.blit(anotherGrim, (840, 240))

        # Screen that contain grimrushers Pics
        if grimWindow:
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))  # Fill screen with black
            draw_text_box(screen, (90, 90), (1040, 520), (50, 50, 50), (109, 69, 38), 130)
            screen.blit(king, (110, 80))
            display_multiline_text(screen, font1, king_msg, (64, 224, 208), 110, 530)
            screen.blit(Friendly_grim, (460, 100))
            display_multiline_text(screen, font1, grim_msg1, (64, 224, 208), 410, 530)
            screen.blit(ferocious_grim, (750, 150))
            display_multiline_text(screen, font1, grim_msg2, (64, 224, 208), 750, 530)
            ContiueBtn.draw(screen)
            ContiueBtn.check_hover(mouse_pos)
        # Army Grimrushers

        if armyGrim:
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            draw_text_box(screen, (150, 90), (900, 500), (50, 50, 50), (109, 69, 38), 130)
            screen.blit(army_Grimrusher, (154, 107))
            display_multiline_text(screen, font2, armyGrim_msg, (255,255,255), 670, 200)
            backButton.draw(screen)
            backButton.check_hover(mouse_pos)
        cursor_img = pygame.image.load('resources/images/Sans titre.png')
        cursor_img = pygame.transform.scale(cursor_img, (40, 40))  # Resize cursor image
        cursor_pos = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_pos)
        pygame.mouse.set_visible(False)

        pygame.display.update()
        pygame.display.flip()
    return True


def EndScreen():
    pygame.init()

    def display_multiline_text(window, font, text, color, x, y, timeSleep=2):
        lines = text.split('\n')
        rendered_lines = [font.render(line, True, color) for line in lines]
        for i, rendered_line in enumerate(rendered_lines):
            window.blit(rendered_line, (x, y + i * font.get_linesize()))

    def typewriter_effect(surface, font, message, position, color=(255, 255, 255), delay=0.05, callback=None):
        lines = message.split('\n')
        x, y = position
        for line in lines:
            for char in line:
                surface.blit(font.render(char, True, color), (x, y))
                pygame.display.update()
                pygame.time.wait(int(delay * 1000))  # Delay in milliseconds
                x += font.size(char)[0]
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
            x = position[0]  # Reset x position to the beginning of the line
            y += font.get_linesize()  # Move to the next line
        if callback:
            callback()

    pygame.display.set_caption("Beyond The Sanctum")
    screen = pygame.display.set_mode((1238, 700), pygame.RESIZABLE)
    font3 = pygame.font.Font("resources/fonts/CinzelDecorative-Regular.ttf", 60)
    font4 = pygame.font.Font("resources/fonts/CinzelDecorative-Regular.ttf", 27)
    background = pygame.image.load("resources/images/BG4.png")
    running = True
    button50 = Button(" BACK TO MENU ", (500, 630), 200, 50)
    msg1 = """
 Congratulation 
 """
    msg2 = """    
                                           Dear adventurer : 
 congratulations on reaching the end of the game.

 Thank you for playing our game. 
 We hope you loved the story and interacted well with it. 
 It is an honor that you have chosen to experience this 
 adventure with us.

 Your adventure here may end, but we hope this is just 
 the beginning of many more to come
                                                                        made with love , Team 9
"""
    done = False
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))  # Fill screen with black
    display_multiline_text(screen, font3, msg1, (128, 0, 0), 300, 20)
    typewriter_effect(screen, font4, msg2, (150, 180), (255, 255, 255))

    pygame.display.flip()
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button50.check_click(mouse_pos):
                    done = True

        button50.check_hover(mouse_pos)
        button50.draw(screen)
        if done:
            import my_game
            my_game.main_menu()

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def BethStory(screen,sound_allowed):
    pygame.init()
    screen = pygame.display.set_mode((1238, 700), pygame.RESIZABLE)
    #pygame.display.set_caption("My First Test")
    background = pygame.image.load("resources/images/BG4.png")
    continueButton = Button("> Contiue Reading the Story", (220, 450), 200, 50)
    continue2 = Button("> Contiue Reading the Story", (220, 400), 200, 50)
    font2 = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 25)
    font1T = pygame.font.Font("resources/fonts/Cinzel-VariableFont_wght.ttf", 25)
    backButton = Button("> Back to the game", (200, 400), 200, 50)
    msg = """
 Story Of Beth :
 """
    Story = """
 tracing back to a time where women gifted  with vision and wisdom were
 carefully chosen. 
Since the creation of monsters, women from the Soliar tribe were selected 
for their potential to safeguard the world's secrets. 
Only the strongest and most competent among them was designated by the Guardian 
of Ancient Secrets,
 """

    Story2 = """
a mystical entity ensuring the preservation of knowledge for the greater good. 
Beth explained that this rigorous selection ensured that the scripts,
knowledge, and research left by the creators of monsters didn't fall 
into wrong hands She continued by describing the fundamental principles 
inscribed in ancient writings.According to these texts, 
serum was the key to controlling some of the most powerful elements """

    Story3 = """fire, light, and even intelligence itself. 
But that wasn't all. There was also a more enigmatic power: 
that of the voice, capable of manipulating minds and controlling thoughts. 
This last gift, though formidable, 

had to be wielded with great caution and unwavering wisdom.
"""

    DoneStory1 = False
    DoneStory2 = False

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_click_sound(sound_allowed)
                if continueButton.check_click(mouse_pos):
                    DoneStory1 = True
                elif continue2.check_click(mouse_pos):
                    DoneStory2 = True
                elif backButton.check_click(mouse_pos):
                    return True

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        draw_text_box(screen, (90, 90), (1040, 460), (50, 50, 50), (109, 69, 38), 130)
        display_multiline_text(screen, font1T, msg, (212, 175, 55), 120, 100)
        display_multiline_text(screen, font2, Story, (255, 255, 255), 120, 170)
        continueButton.draw(screen)
        continueButton.check_hover(mouse_pos)

        if DoneStory1:
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            draw_text_box(screen, (90, 90), (1040, 460), (50, 50, 50), (109, 69, 38), 130)
            display_multiline_text(screen, font2, Story2, (255, 255, 255), 120, 120)
            continue2.draw(screen)
            continue2.check_hover(mouse_pos)

        if DoneStory2:
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            draw_text_box(screen, (90, 90), (1040, 450), (50, 50, 50), (109, 69, 38), 130)
            display_multiline_text(screen, font2, Story3, (255, 255, 255), 150, 150)
            backButton.draw(screen)
            backButton.check_hover(mouse_pos)

        cursor_img = pygame.image.load('resources/images/Sans titre.png')
        cursor_img = pygame.transform.scale(cursor_img, (40, 40))  # Resize cursor image
        cursor_pos = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_pos)
        pygame.mouse.set_visible(False)

        pygame.display.update()
    return True








