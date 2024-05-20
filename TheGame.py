import pygame
import sys
pygame.init()
import CharactersDetails
pygame.mouse.set_visible(False)


def play_click_sound():
    click_sound.play()
click_sound = pygame.mixer.Sound("resources/sounds/mouse-click-153941.mp3")
def play_game():
    global scroll_speed

    WIDTH, HEIGHT = 1238, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Beyond The Sanctum")
    background = pygame.image.load('resources/images/BG4.png')
    font = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 25)
    font0 = pygame.font.Font("resources/fonts/times new roman italic.ttf", 20)
    font2 = pygame.font.Font("resources/fonts/CinzelDecorative-Regular.ttf", 60)
    font3 = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 70)
    timer = pygame.time.Clock()

    scroll_offset = 0
    scroll_speed = 30
    line_visible = True

    text0 = "you feel the cold ground beneath your back, surrounded by the unfamiliar sounds and sights, confusion grips you as you struggle to recall how you ended up here.\n\n“Where ..am I? The outside world!” you gasp\n\nA scrap of paper flutters down beside you, catching your attention."
    text1 = "Aiden's Father (voice echoing in your mind): ”Hello, Aiden. Look at yourself, If you are still a human, it means the serum worked as planned. The Serenyl serum has granted you powers beyond imagination. Powers you'll need to save us all.”\n\nyou see a river few meters away."
    text2 = "You look at your reflection.. \n\n“I am still a human! But what is that serum? How did I end up here and.. save them from what or who?” you say reassured and confused."
    text2_1 = "“this must be a joke, I will keep walking until I find the sanctum” you murmured. \n\nthalos: “you! Oh you! We have been waiting for you for so long you finally came!” \n\nconfused you respond “ oh no please, it’s a misunderstanding, Im just trying to go back to the sanctum” \n\nthalos : “ aren’t you aiden?” \n\n“ I am.. how do you know my name?” \n\n thalos: “oh aiden.. son of Dr. Marcus Evergreen, I’m thalos ,an old friend of your father, you know me  very well” "
    text2_2 = "You look around to find the answers to your question, when you suddenly catch a weird creature."
    text3_1 = "“I am sorry this is all a misundersanding, it was nice talking to you thalos” \n\nthalos : “nice to meet you thalos, take care” \n\n you hear thalos murmuring “ he will come back..” \n\n you pursue your journey to go back to the sanctum..\n\nand when everything seemed to be flowing perfectly, you catch sight of the familiar sanctum walls, you blink. \n\n“WHAT?! How am I being brought here again? “ you are brought back to where you were first,and you see thalos again.. "
    text3_2 = "«Hey sir? What is this place I have never seen anything like it» you ask Thalos \n\n Thalos : “ this is « behind the walls » you are outside of the sanctum, aren’t you aiden? » \n\n“ I am.. how do you know my name?” \n\n thalos: “oh aiden.. son of Dr. Marcus Evergreen, I’m thalos ,an old friend of your father, you know me very well” "
    text4_1 = "Fine.. what is this all about? What is happening to me? What is it!”\n\n Thalos:“ Haven’t you seen any paper, letter..?“\n\nYou: “Yes I did! But I thought it was a joke and forgot about it! In fact I didn’t read it..“\n\nThalos:“ Pick it up.“"
    text4_2 = "Fine.. what is this all about? What is happening to me? What is it!”\n\n Thalos:“ Haven’t you seen any paper, letter..?“\n\nYou: “Yes I did! But I thought it was a joke and forgot about it! In fact I didn’t read it..“\n\nThalos:“ Pick it up.“"
    text5_1 = "\n“here..” you say.\nThalos picks the letter and reads it out loud for you .. "
    text5_2 = "“The world outside the Sanctum is not as we once believed. It teems with dangers beyond our comprehension. The GrimRushers, as we've come to know them. They possess intelligence, cunning, and a kingdom of their own. They threaten not only our existence but the very fabric of our society within the Sanctum.\nYou, my son, are our hope. You must venture beyond the safety of our walls, confront the GrimRushers, and discover the secrets of their kingdom. Only then can we hope to secure our future. But be warned, Aiden, the path ahead is treacherous, and the challenges you'll face are formidable.\nI wish I could have joined you on this adventure, but I'm unable to because I'm embarking on an important mission for the next few months. Take care of yourself, my treasure.“"
    text5_3 = "A fragment of memory suddenly resurfaces, transporting him back to a dimly lit corner of the Sanctum's library. "
    text5_4 = "FIVE YEARS AGO..."
    text5_5 = "you are cross-legged in the Sanctum's library, a majestic chamber filled with towering shelves of books. Despite its serene atmosphere, the library is hinting at forbidden knowledge lurking within its depths.\nYou are frightened by the sound of a heavy book falling from a shelf."
    text5_6 = "THE LETTER"
    text6_1 = "“there is something !”\nyou read out loud "
    text6_2 = "“In shadows deep, where whispers creep, \nThe GrimRushers dwell, their secrets keep.\nTo know their truth, one must dare to seek, \nBeyond the veil, where answers sleep.”"
    text6_3 = "an old man yells at you “Put it back right now! Or I will kick you out of the library!”"
    text6_4 = "you put the book back in its place and continue working.\nFocused on your work you hear murmurs of your classmates having an inaudible dialogue, yet heard “GrimRushers” and some weird description along the phrases.\n\nAiden: “Hey there! I somehow heard you talk about ..GrimRushers?”\n\n“yes! The monsters of behind the walls!”\n\nyou are interrupted by an old man yelling at you “Don’t ever talk about the GrimRushers again! It’s an old legend! Go back to your work now”"
    text7_1 = "the curiosity is unbearable that you reach your father Marcus as soon as you can to ask him.\n\n“Father! I want to ask you something”\n\nMarcus : “sure son! Is it some math question, or is it about philosophy? I was good at it !”\n\n“no.. it’s about  GrimRushers, monsters of behind the walls or..”\n\n“yes, it’s a legend.” you father interrupted nervously.\n\nyou leave with even more questions.. but with a great feeling of joy and mystery."
    text7_2 = "BACK TO NOW"
    text7_3 = "“ now I remember!! I knew there was something strange!”, you said with lots of excitement to Thalos\n\nThalos : “ Aiden, you remember the book that fell in the library?”\n\n“oh yes I do!”\n\nthalos : “ it was me. And before you ask, I will explain everything.\n\nI was a regular human, just like you, full of life, excitement and curiosity. I heard about the grimrushers, I made lots of researches, asked many people, only one helped me through, your father Marcus. He was as passionated as me, he helped me as a brother, but also as a doctor.\n\nYour father  had a grimrusher in his laboratory that they captured to make experiments on. He made the first version of the Serum Serenly and gave It to me in an attempt to know the Grimrushers and win a final battle with them, to restore the peace in the sanctum”.\n\n“but why aren’t you a human anymore?”\n\nThalos : “ the serum had some problems, it didn’t work as expected, it gave me some powers, which allowed me to communicate with you by controlling objects, it made me stronger, but it also turned me as a Centaur..”"
    text7_4 = "Press on Centaur to know more about Centaurs!"
    text8_1 = "“and so.. What shall I do now?“\n\nThalos : “I will help you through your journey Aiden, just like your father helped me, you have to save the human race by overcoming plenty of obstacles obstacles through your adventure. “"
    text8_2 = "Thalos: “I've been tracking a bunch of Grimrushers for a while now, and I've noticed they enter a basement every day, carrying boxes. We need to find out what's in those boxes and uncover the secret of the basement. Your first mission is to confront the Grimrusher guarding the basement door and secure our entry. “"
    text8_3 = "you are in front of the basement and the grimrusher is approaching you, you must kill it."
    text9_1 = "As the grimrusher approaches, Aiden's mind flashes back to what his father told him about the serenly serum. He focuses on tapping into his latent powers. Suddenly, Aiden's hands begin to glow with a brilliant light."
    text9_2 = "Aiden channels his energy into a powerful burst of light emanating from his hands. The blinding beam strikes the monster, causing it to recoil in pain and die.\n\n“that.. was Amazing! What else can I do thalos?” you ask excitingly \n\nThalos : “we will see, it’s just the beginning!”\n\nWith the Grimrusher dead, you turn your attention to the sealed entrance of the basement, knowing that the answers you seek lie within its depths.\n\nYou stand before the locked entrance to the basement.\nWhat will you do?"
    text9_2_1 = "You approach the fallen Grimrusher and find a tiny, ornate key nestled inside."
    text9_2_2 = "You continue searching the area, you notice a shining spot on the floor.\n\nIt’s the sun’s reflection on a key the guard held. The key of the basement.\nYou approach the locked basement door and insert the key into the lock. With a satisfying click, the lock disengages, and the door swings open"
    text9_3 = "You approach the locked basement door and insert the key into the lock. With a satisfying click, the lock disengages, and the door swings open."
    text10 = "You stand before the entrance to the basement, a looming abyss of darkness that beckons you forward. Just in front of you lies an old oil lamp."
    text10_1 = "You pick up the lamp and light it, The area is illuminated lit enough for you to see where you're heading. \n\n“where do you think those boxes are thalos? Won’t you use your powers for god’s sake.. I bet I’m better than you!” you say sarcastically.\n\nThalos : “ oh you are better than me, we will see that, now keep moving forward, I see something there”"
    text11 = "You step cautiously into the darkness of the basement. As you descend the staircase, you find yourself in a small chamber with a solid stone wall directly in front of you."
    text11_1 = "You approach the stone wall and run your hands over its rough surface. It feels solid and unyielding, with no visible cracks or openings."
    text11_2 = "your powers are too weak to break the wall."
    text11_3 = "“I can’t see a thing! Where do these monsters go!”\n\nThalos “ the wall is very high, we didn’t see up, give me that lamp I can use my levitating powers to see higher.”"
    text12 = "Thalos:“ Ha see! A rope”\n\n“can you pull it from here?”\n\nThalos : “show some respect please, I took that bloody serum too mind you!”\n\nThalos uses his power to pull the rope and a secret passage appears on the ground.\n\n“you got some nice moves mate! I respect you now for sure” \n\nThalos : “ yeah whatever”"
    text13 = "you and Thalos go down the stairs of the secret passage and slip into the gathering chamber of the GrimRushers where you see them gathered around a central dais, murmuring in an unknown tongue.\n\nWith cautious steps, you navigate the chamber's perimeter, eyes trained on the passage leading deeper into the lair. Aware of the peril ahead, they steel themselves for the mission ahead, knowing the fate of the Sanctum hangs in the balance.\n“this chamber is full of boxes! What do you think they are for?” you whisper to thalos.\n\nThalos : “ here, there is a box at your place”"
    text14 = "you see a bunch of scripts. \n“it seems like these are recipes” you say delightfuly\n\n A Grimrusher getting closer to you!! "
    text14_1 = "“did you hear that?!” you say worried\n\nThalos : “ aiden, take all of those scripts and let’s leave right now.”"
    text14_2 = "you and thalos move slowly out of the chamber, but right before, a weird map catches your attention. \n\n“it seems to be the map of their kingdom” you think "
    text14_3 = "Now, the map is  in your inventory.\n\n You and thalos leave hastily the basement. After a long hour of walking, you look for some nice place to sit, you see a tree not too far from you.\nThalos : “let’s take a look at those scripts”\n“here..”\nThalos reads..\nThalos : “aiden, it’s a crypted, see..”"
    msg = "Press Scripts to see a crypted Script!!"
    text15 = "you sit in frustration, staring at the indecipherable script, you feel a sense cluelessness creeping up. \n\nThalos : “this reminds me a lot of an ancient text I saw once, expose it to a sunbeam aiden”"
    hint = "” The sun's warmth lacks the intensity, think of another source of heat.”\n\n  Be smart and choose the right source of heat."
    oil_lamp = "you carefully position the script closer to the flame of the oil lamp, allowing its heat to envelop the script. To your amazement, the letters begin to dance and writhe, their forms twisting and reshaping. you understand—the heat of the lamp's flame is causing the ink to react, unveiling the hidden messages within the script. \n\n“i’m starting to know why you worked with my father”\n\nThalos : “ I’ll take that as a compliment, so, what does it say?”"
    fire = "You used your powers but they are too weak to make fire. Think of another way."
    text15_5 = "a veroccusom extract\na shivereana extract\nand a crystalline mineral."
    text15_6 = "Note: Handle the ingredients with utmost care, as their volatile nature demands re-spect and caution. Only those with knowledge of botanical arts and mastery over mineral should attempt to brew this elixir. We owe it our most precious”"
    text15_7 = "Thalos: “ seems to be a list of ingredients”\n“what for?” you wonder..\nThalos : “ we have to go to the village to know more, you remember the map you found at the chamber.take it.”"
    text15_8 = "As Thalos studied the cryptic symbols on the map, a sense of unease gnawed at him. The village, marked as a distant point on the map, held the answers they sought—but also un-told dangers.\n\n“So, what's our next destination?“ you ask.\n\nThalos : “According to this, we need to pass through the forest. It seems the forest is our next destination, the Eerie forest.“ he replied.\n“okay, let’s go then..”"
    text16 = "“As you and Thalos continue your journey through the eerily forest, the silence makes you aware of subtle signs of disturbance.. you feel like the forest floor hint at the pres-ence of an unseen entity moving with calculated steps. precision. \n\n“These disturbances are not the work of grimrushers!”\n\nthalos whispers.. “they are deliberate, calculated...”\n\nyou nod in agreement, your gaze scanning the surrounding foliage for any hint of move-ment. ”It's like they know we're here”, you murmur"
    text16_1 = "thalos: look in the ground maybe you find something. \n\nthere is a thick carpet of foliage, where leaves and vines intertwine to form a tangled mass upon the floor."
    text16_2 = "as you clear it away, you uncover something hidden beneath. It's a grating, tucked away beneath the forest floor."
    text16_3 = "“Ooooooh it is locked ,I can’t open it“.\n\nThalos :“Look at these patterns, I believe we've already seen them during our jour-ney. We need to apply all our intelligence to decode them.“"
    text16_4 = "Aiden : “what are these signes ?”\nThalos :“Aiden, these signs on the grating are ancient symbols. They are part of a riddle, a test left behind by those who built this grating, perhaps to protect them-selves from what lies beyond.“\n\nAiden furrows his brow... “What kind of test?“ you ask.\n\nThalos : gestures toward the symbols etched into the grating.\n “The riddle challenges us to find a hidden word,“ he continues. \n“Once we uncover the word, we must arrange the letters in the correct order to unlock the grating.“"

    tex = "your fierce battle catches the attention of other Grimrushers lurking nearby and you find yourselves surrounded by a horde of snarling creatures, despite your best efforts, the sheer number of Grimrushers overwhelms you, with a heavy heart, you realize that victory is beyond your grasp and your journey comes to a premature end."

    def button_click_action2():
        CharactersDetails.BethDescreption(screen)
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
                #self.clicked = True
                self.color = self.clicked_color
                #self.visible = False  # Button is no longer visible
                return True
            return False

        def reset_click(self):
            self.clicked = False

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

    def button_click_action():
        CharactersDetails.centaurs(screen)
    def button_click_action3():
        CharactersDetails.CryptedLetter(screen)
    def button_click_action1():
        CharactersDetails.RoyalCeremony(screen)

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

    def draw_line(surface, x1, y1, x2, y2, width, color, scroll_offset, visible=True):
        if visible:
            pygame.draw.line(surface, color, (x1, y1 + scroll_offset), (x2, y2 + scroll_offset), width)


    class TextField:
        def __init__(self, position, size, border_color, text_color, max_chars, correct_word, callback=None,  wrong_callback=None):
            self.rect = pygame.Rect(position, size)
            self.border_color = border_color
            self.text_color = text_color
            self.max_chars = max_chars
            self.text = ""
            self.active = False
            self.correct_word = correct_word
            self.callback = callback
            self.wrong_callback = wrong_callback
            self.gameover = False
            self.cursor_visible = True
            self.cursor_timer = 0



        def draw(self, surface, scroll_offset):
            # Adjust the position of the text field based on the scroll offset
            adjusted_y = self.rect.y + scroll_offset

            # Draw the text field at the adjusted position
            adjusted_rect = pygame.Rect(self.rect.x, adjusted_y, self.rect.width, self.rect.height)
            pygame.draw.rect(surface, self.border_color, adjusted_rect, 1)
            font = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 25)
            text_surface = font.render(self.text, True, self.text_color)
            surface.blit(text_surface, (self.rect.x + 5, adjusted_y + 5))

            # Draw cursor if active
            if self.active and self.cursor_visible:
                cursor_x = self.rect.x + 5 + font.size(self.text)[0]
                cursor_y = adjusted_y + 5
                pygame.draw.line(surface, self.text_color, (cursor_x, cursor_y),
                                 (cursor_x, cursor_y + font.size("A")[1]))

            # Display message if any

        def handle_event(self, event, scroll_offset):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if mouse click is inside the text field
                if self.rect.collidepoint((event.pos[0], event.pos[1] - scroll_offset)):
                    self.active = True
                else:
                    self.active = False
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        # Check if entered text is correct
                        if self.text == self.correct_word:
                            # Execute callback function if provided
                            if self.callback:
                                self.callback()
                        else:
                            if self.wrong_callback:
                                self.wrong_callback()
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif len(self.text) < self.max_chars:
                        self.text += event.unicode

        def update_cursor(self, dt):
            # Update cursor visibility every 500 milliseconds
            self.cursor_timer += dt
            if self.cursor_timer >= 500:
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer %= 500



    done = False
    done1 = False
    done2_1 = False
    done2_2 = False
    done3_1 = False
    done3_2 = False
    done4_1 = False
    done4_2 = False
    done4_3 = False
    done5_1 = False
    done5_2 = False
    done5_3 = False
    done5_4 = False
    done6_1 = False
    done6_2 = False
    done1_0 = True
    done7_1 = False
    done7_3 = False
    done8_1 = False
    done8_2 = False
    centaur = False
    done8_3 = False
    done9_1 = False
    done9_2 = False
    done9_2_2 = False
    done10_1 = False
    done9_3 = False
    done10_2 = False
    done10 = False
    done10_3 = False
    done11_1 = False
    done11_2 = False
    done12 = False
    done12_1 = False
    done12_2 = False
    done13 = False
    done13_1 = False
    done13_2 = False
    done14_1 = False
    done14_2 = False
    done14_3 = False
    done15 = False
    done15_1 = False
    done15_2 = False
    done15_4 = False
    done15_5 = False
    done15_6 = False
    done15_7 = False
    done15_8 = False
    done16 = False
    done16_1 = False
    done16_2 = False
    done16_3 = False
    done16_4 = False
    done60 = False
    done37_1 = False




    button0 = Button("> Pick it up.", (120, 520), 200, 50)
    button1 = Button("> Reach the river. ", (120, 450), 200, 50)
    button2_1 = Button(" > 1- Drop the paper and find your way back to the Sanctum.", (120, 440), 630, 50)
    button2_2 = Button(" > 2- Ask for guidance and try to understand.", (120, 500), 480, 50)
    button3_1 =Button(" > 1- Leave him.", (120, 820), 200, 50)
    button3_2 =Button(" > 2- Ask for more details.", (120, 880), 310, 50)
    button4_1 = Button(" > Approach him.", (150, 370), 200, 50)
    button4_3 = Button("> Continue.", (120, 570), 200, 50)
    button4_2 = Button(" >  More details.", (150, 870), 200, 50)
    button5_1 = Button("> Pick it up.", (120, 690), 200, 50)
    button5_2 = Button(" →", (960, 590), 200, 50)
    button5_3 = Button("> Open it.", (120, 575), 200, 50)
    button5_4 = Button("> Put it back.", (135, 630), 200, 50)
    button6_1 = Button(" →", (960, 570), 200, 50)
    button6_2 = Button(" →", (960, 710), 200, 50)
    button7_1 = Button(" →", (960, 760), 200, 50)
    button7_2 = Button("> Press on centaur to know more.", (120, 900), 480, 50)
    button7_3 = Button("> Continue.", (120, 1450), 200, 50)
    button8_1 = Button("> Continue.", (120, 430), 200, 50)
    button8_2 = Button("> Go to the basement.", (150, 420), 200, 50)
    button8_3 = Button(" > Use your powers.", (150, 230), 200, 50)
    button9_1 = Button(" > Use that Light.", (150, 500), 200, 50)
    button9_2 = Button(" > 1- Check on the dying grimrusher.", (150, 790), 370, 50)
    button9_2_2 = Button(" > 2- Look around the area.", (150, 850), 280, 50)
    button10_1 = Button(" > Take the key and use it to unlock the door", (150, 380), 400, 50)
    button10_2 = Button(" →", (960, 450), 200, 50)
    button9_3 = Button(" →", (960, 400), 200, 50)
    button10 = Button(" > Take the lamp. ", (150, 400), 200, 50)
    button10_3 = Button(" > Continue", (120, 520), 200, 50)
    button11_1 = Button("> 1- Inspect the stone wall.", (120, 410), 320, 50)
    button11_2 = Button("> 2- Use your power to break the wall.", (120, 460), 420, 50)
    button12 = Button(" →", (960, 400), 200, 50)
    button12_1 = Button("> Continue. ", (120, 425), 200, 50)
    button12_2 = Button(" > Continue", (120, 700), 200, 50)
    button13 = Button(" > Open the box.", (120, 600), 200, 50)
    button13_1 = Button(" > 1- Fight him. ", (140, 450), 200, 50)
    button13_2 = Button(" > 2- Hide and wait.", (140, 510), 230, 50)
    button02 = Button("  Menu.", (500, 450), 200, 50)
    button01 = Button("  quit.", (500, 530), 200, 50)
    button14_1 = Button(" > Take.", (120, 405), 200, 50)
    button14_2 = Button(" > Pick.", (120, 405), 200, 50)
    button14_3 = Button(" → ", (960, 615), 200, 50)
    button15 = Button(" > Expose ", (120, 420), 200, 50)
    button15_1 = Button(" > Hint ", (120, 310), 200, 50)
    button15_2 = Button(" > Fire ", (120, 380), 190, 50)
    button15_4 = Button(" > Oil lamp ", (120, 440), 220, 50)
    button60 =  Button(" > Oil lamp ", (120, 440), 220, 50)
    button15_5 = Button(" > Read. ", (120, 600), 200, 50)
    button15_6 = Button(" > Take. ", (120, 720), 200, 50)
    button15_7 = Button(" > Continue. ", (1020, 580), 200, 50)
    button15_8 = Button(" > Continue.", (120, 610), 200, 50)
    button16 = Button(" > Hint.", (120, 700), 200, 50)
    button16_1 = Button(" →", (960, 380), 200, 50)
    button16_2 = Button(" > Open.", (120, 340), 200, 50)
    button16_3 = Button(" > Examine the grating more.", (120, 410), 300, 50)
    button16_4 = Button(" > Ask him about the riddle.", (120, 620), 300, 50)
    button37_1 = Button(" MENU ", (500, 580), 200, 50)

    centaurs = CharButton(" Centaur", (73, 1285), 200, 50, button_click_action)
    Script = CharButton(" scripts", (368, 296), 200, 50, button_click_action3)


    while True:

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()

            if events.type == pygame.MOUSEBUTTONDOWN:
                play_click_sound()
                if button0.check_click(mouse_pos) :
                    done = True
                    scroll_offset = 0
                elif  button1.check_click(mouse_pos) and done:
                    done1 = True
                    scroll_offset = 0
                elif button2_1.check_click(mouse_pos) and done1 :
                    done2_1 = True
                    scroll_offset = 0
                elif button2_2.check_click(mouse_pos) and done1:
                    done2_2 = True
                    scroll_offset = 0
                elif button3_1.check_click(mouse_pos) and done2_1:
                    done3_1 = True
                    scroll_offset = 0
                elif button3_2.check_click(mouse_pos) and done2_1:
                    done3_2 = True
                    scroll_offset = 0
                elif button4_1.check_click(mouse_pos) and done2_2:
                    done4_1 = True
                    scroll_offset = 0
                elif button4_2.check_click(mouse_pos) and done3_1:
                    done4_2 = True
                    scroll_offset = 0
                elif button4_3.check_click(mouse_pos) and done4_1:
                    done4_3 = True
                    scroll_offset = 0
                elif button5_1.check_click(mouse_pos) and done4_2:
                    done5_1 = True
                    scroll_offset = 0
                elif button5_2.check_click(mouse_pos)and done5_1:
                    done5_2 = True
                    scroll_offset = 0
                elif button5_3.check_click(mouse_pos) and done5_2 :
                    done5_3 = True
                    scroll_offset = 0
                elif button5_4.check_click(mouse_pos)  and done5_2:
                    done5_4 = True
                    scroll_offset = 0
                elif button6_1.check_click(mouse_pos) and done5_3:
                    done6_1 = True
                    scroll_offset = 0
                elif button6_2.check_click(mouse_pos) and done5_4:
                    done6_2 = True
                    scroll_offset = 0
                elif button7_1.check_click(mouse_pos) and done6_1:
                    done7_1 = True
                    scroll_offset = 0
                elif button7_2.check_click(mouse_pos) and done7_1:
                    done7_2 = True
                    scroll_offset = 0
                elif button7_3.check_click(mouse_pos) and done7_1:
                    done7_3 = True
                    scroll_offset = 0
                elif button8_1.check_click(mouse_pos) and done7_3:
                    done8_1 = True
                    scroll_offset = 0
                elif button8_2.check_click(mouse_pos) and done8_1:
                    done8_2 = True
                    scroll_offset = 0
                elif centaurs.check_click(mouse_pos):
                    centaurs.clicked = False
                    centaurs.visible = True
                elif button8_3.check_click(mouse_pos) and done8_2:
                    done8_3 = True
                    scroll_offset = 0
                elif button9_1.check_click(mouse_pos) and done8_3:
                    done9_1 = True
                    scroll_offset = 0
                elif button9_2.check_click(mouse_pos) and done9_1:
                    done9_2 = True
                    scroll_offset = 0
                elif button9_2_2.check_click(mouse_pos) and done9_1:
                    done9_2_2 = True
                    scroll_offset = 0
                elif button10_1.check_click(mouse_pos) and done9_2:
                    done10_1 = True
                    scroll_offset = 0
                elif button10_2.check_click(mouse_pos) and done9_2_2:
                    done10_2 = True
                    scroll_offset = 0
                elif button9_3.check_click(mouse_pos) and done10_1:
                    done9_3 = True
                    scroll_offset = 0
                elif button10.check_click(mouse_pos) and done9_3:
                    done10 = True
                    scroll_offset = 0
                elif button10_3.check_click(mouse_pos) and done10:
                    done10_3 = True
                    scroll_offset = 0
                elif button11_1.check_click(mouse_pos) and done10_3:
                    done11_1 = True
                    scroll_offset = 0
                elif button11_2.check_click(mouse_pos) and done10_3:
                    done11_2 = True
                    scroll_offset = 0
                elif button12.check_click(mouse_pos) and (done11_1 or done11_2):
                    done12 = True
                    scroll_offset = 0
                elif button12_1.check_click(mouse_pos) and done12:
                    done12_1 = True
                    scroll_offset = 0
                elif button12_2.check_click(mouse_pos) and done12_1:
                    done12_2 = True
                    scroll_offset = 0
                elif button13.check_click(mouse_pos) and done12_2:
                    done13 = True
                    scroll_offset = 0
                elif button13_1.check_click(mouse_pos) and done13:
                    done13_1 = True
                    scroll_offset = 0
                elif button13_2.check_click(mouse_pos) and done13:
                    done13_2 = True
                    scroll_offset = 0

                elif button14_1.check_click(mouse_pos) and done13_2:
                    done14_1 = True
                    scroll_offset = 0
                elif button14_2.check_click(mouse_pos) and done14_1:
                    done14_2 = True
                    scroll_offset = 0
                elif button14_3.check_click(mouse_pos) and done14_2:
                    done14_3 = True
                    scroll_offset = 0
                elif button15.check_click(mouse_pos) and done14_3:
                    done15 = True
                    scroll_offset = 0
                elif button15_1.check_click(mouse_pos) and done15:
                    done15_1 = True
                    scroll_offset = 0
                elif button15_2.check_click(mouse_pos) and done15_1 :
                    done15_2 = True
                    scroll_offset = 0
                elif button15_4.check_click(mouse_pos) and done15_1:
                    done15_4 = True
                    scroll_offset = 0
                elif button15_5.check_click(mouse_pos) and done15_4:
                    done15_5 = True
                    scroll_offset = 0
                elif button15_6.check_click(mouse_pos) and done15_5:
                    done15_6 = True
                    scroll_offset = 0
                elif button15_7.check_click(mouse_pos) and done15_6:
                    done15_7 = True
                    scroll_offset = 0
                elif button15_8.check_click(mouse_pos) and done15_7:
                    done15_8 = True
                    scroll_offset = 0
                elif button16.check_click(mouse_pos) and done15_8:
                    done16 = True
                    scroll_offset = 0
                elif button16_1.check_click(mouse_pos) and done16:
                    done16_1 = True
                    scroll_offset = 0
                elif button16_2.check_click(mouse_pos) and done16_1:
                    done16_2 = True
                    scroll_offset = 0
                elif button16_3.check_click(mouse_pos) and done16_2:
                    done16_3 = True
                    scroll_offset = 0
                elif button16_4.check_click(mouse_pos) and done16_3:
                    done16_4 = True
                    scroll_offset = 0

                elif Script.check_click(mouse_pos):
                    Script.clicked = False  # Reset the clicked flag
                    Script.visible = True  # Make the button visible again

                elif button37_1.check_click(mouse_pos) and done13_1 :
                    done37_1 = True
                    scroll_offset = 0
                elif button60.check_click(mouse_pos) and done15_2 :
                    done60 = True
                    scroll_offset = 0


        button0.check_hover(mouse_pos)
        button1.check_hover(mouse_pos)
        button2_1.check_hover(mouse_pos)
        button2_2.check_hover(mouse_pos)
        centaurs.check_hover(mouse_pos)
        button3_1.check_hover(mouse_pos)
        button3_2.check_hover(mouse_pos)
        button4_1.check_hover(mouse_pos)
        button4_2.check_hover(mouse_pos)
        button4_3.check_hover(mouse_pos)
        button5_1.check_hover(mouse_pos)
        button5_2.check_hover(mouse_pos)
        button5_3.check_hover(mouse_pos)
        button5_4.check_hover(mouse_pos)
        button6_1.check_hover(mouse_pos)
        button7_1.check_hover(mouse_pos)
        button7_3.check_hover(mouse_pos)
        button7_2.check_hover(mouse_pos)
        button8_1.check_hover(mouse_pos)
        button8_2.check_hover(mouse_pos)
        button8_3.check_hover(mouse_pos)
        button9_1.check_hover(mouse_pos)
        button9_2.check_hover(mouse_pos)
        button9_2_2.check_hover(mouse_pos)
        button10_1.check_hover(mouse_pos)
        button10_2.check_hover(mouse_pos)
        button9_3.check_hover(mouse_pos)
        button10.check_hover(mouse_pos)
        button10_3.check_hover(mouse_pos)
        button11_1.check_hover(mouse_pos)
        button11_2.check_hover(mouse_pos)
        button12.check_hover(mouse_pos)
        button12_1.check_hover(mouse_pos)
        button12_2.check_hover(mouse_pos)
        button13.check_hover(mouse_pos)
        button13_1.check_hover(mouse_pos)
        button13_2.check_hover(mouse_pos)
        button02.check_hover(mouse_pos)
        button01.check_hover(mouse_pos)
        button14_1.check_hover(mouse_pos)
        button14_2.check_hover(mouse_pos)
        button14_3.check_hover(mouse_pos)
        button15.check_hover(mouse_pos)
        button15_1.check_hover(mouse_pos)
        button15_2.check_hover(mouse_pos)
        button15_4.check_hover(mouse_pos)
        button15_5.check_hover(mouse_pos)
        button15_6.check_hover(mouse_pos)
        button15_7.check_hover(mouse_pos)
        button15_8.check_hover(mouse_pos)
        button16.check_hover(mouse_pos)
        button16_1.check_hover(mouse_pos)
        button16_2.check_hover(mouse_pos)
        button16_3.check_hover(mouse_pos)
        button16_4.check_hover(mouse_pos)
        button60.check_hover(mouse_pos)
        centaurs.check_hover(mouse_pos)
        Script.check_hover(mouse_pos)
        button37_1.check_hover(mouse_pos)


        if done1_0:
            draw_text_box(screen, (90, 90), (1060, 520), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text0, (120, 150), font, (255,255,255), scroll_offset)
            draw_line(screen, 130, HEIGHT -200, WIDTH - 130, HEIGHT -200, 1, (109, 69, 38), scroll_offset, line_visible)
            button0.draw(screen, scroll_offset)

        if done :
            done1_0 = False
            button0.clicked = True
            draw_text_box(screen, (90, 120), (1060, 420), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text1, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 270, WIDTH - 130, HEIGHT - 270, 1, (109, 69, 38), scroll_offset, line_visible)
            button1.draw(screen, scroll_offset)

        if done1:
            done = False
            button1.clicked = True
            draw_text_box(screen, (90, 90), (1060, 500), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text2, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 300, WIDTH - 130, HEIGHT - 300, 1, (109, 69, 38), scroll_offset,line_visible)
            button2_1.draw(screen, scroll_offset)
            button2_2.draw(screen, scroll_offset)

        if done2_1:
            done = False
            done1 = False
            button2_1.clicked = True
            button2_2.clicked = True
            draw_text_box(screen, (90, 60), (1060, 900), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text2_1, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 90, WIDTH - 130, HEIGHT + 90, 1, (109, 69, 38), scroll_offset,line_visible)
            button3_1.draw(screen, scroll_offset)
            button3_2.draw(screen, scroll_offset)
        if done3_1:
            done = False
            done2_1 = False

            draw_text_box(screen, (90, 60), (1060, 900), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text3_1, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 130, WIDTH - 130, HEIGHT + 130, 1, (109, 69, 38), scroll_offset,line_visible)
            button4_2.draw(screen, scroll_offset)
        if done4_2:
            done = False
            done3_1 = False

            draw_text_box(screen, (90, 60), (1060, 720), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text4_1, (120, 110), font, (255, 255, 255), scroll_offset)
            display_text(screen, text5_1, (120, 470), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 30, WIDTH - 130, HEIGHT -30, 1, (109, 69, 38), scroll_offset, line_visible)
            button5_1.draw(screen, scroll_offset)
        if done5_1:
            done = False
            done4_2 = False
            display_text(screen, text5_6, (420, 90), font2, (168, 127, 71), scroll_offset)
            display_text(screen, text5_2, (150, 230), font0, (255, 255, 255), scroll_offset)
            button5_2.draw(screen, scroll_offset)
        if done5_2:
            done5_1 = False
            draw_text_box(screen, (90, 60), (1060, 655), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text5_3, (120, 110), font, (255, 255, 255), scroll_offset)
            display_text(screen, text5_4, (340, 230), font2, (168, 127, 71), scroll_offset)
            display_text(screen, text5_5, (120, 370), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 150, WIDTH - 130, HEIGHT - 150, 1, (109, 69, 38), scroll_offset, line_visible)
            button5_3.draw(screen, scroll_offset)
            button5_4.draw(screen, scroll_offset)

        if done5_3:
            done5_2 = False
            draw_text_box(screen, (90, 90), (1060, 560), (50, 50, 50), (109, 69, 38), 130,scroll_offset)
            display_text(screen, text6_1, (120, 120), font, (255, 255, 255), scroll_offset)
            display_text(screen, text6_2, (130, 260), font0, (255,255,255), scroll_offset)
            display_text(screen, text6_3, (120, 460), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 160, WIDTH - 130, HEIGHT - 160, 1,(109, 69, 38), scroll_offset, line_visible)
            button6_1.draw(screen, scroll_offset)
        if done6_1:
            done5_3 = False

            draw_text_box(screen, (90, 90), (1060, 750), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text7_1, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT +40, WIDTH - 130, HEIGHT +40, 1, (109, 69, 38), scroll_offset, line_visible)
            button7_1.draw(screen, scroll_offset)
        if done7_1:
            done6_1 = False
            draw_text_box(screen, (90, 60), (1060, 1470), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text7_2, (380, 90), font2, (168, 127, 71), scroll_offset)
            display_text(screen, text7_3, (120, 230), font, (255, 255, 255), scroll_offset)
            display_text(screen, text7_4, (120, 1370), font0, (205, 210, 155), scroll_offset)
            draw_line(screen, 130, HEIGHT + 740, WIDTH - 130, HEIGHT + 740, 1, (109, 69, 38), scroll_offset, line_visible)
            button7_3.draw(screen, scroll_offset)
            centaurs.draw(screen, scroll_offset)
        if done7_3:
            done7_1 = False
            centaurs.clicked = True
            draw_text_box(screen, (90, 120), (1060, 400), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text8_1, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 300, WIDTH - 130, HEIGHT -300, 1, (109, 69, 38), scroll_offset,line_visible)
            button8_1.draw(screen, scroll_offset)
        if done8_1:
            done7_3 = False
            draw_text_box(screen, (90, 120), (1060, 380), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text8_2, (120, 160), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 310, WIDTH - 130, HEIGHT - 310, 1, (109, 69, 38), scroll_offset,line_visible)
            button8_2.draw(screen, scroll_offset)
        if done8_2:
            done8_1 = False
            draw_text_box(screen, (90, 90), (1060, 500), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text8_3, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 500, WIDTH - 130, HEIGHT - 500, 1, (109, 69, 38), scroll_offset,line_visible)
            button8_3.draw(screen, scroll_offset)
        if done8_3:
            #done8_2 = False
            display_text(screen, text9_1, (120, 300), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 220, WIDTH - 130, HEIGHT - 220, 1, (109, 69, 38), scroll_offset,line_visible)
            button9_1.draw(screen, scroll_offset)
        if done9_1:
            done8_3 = False
            done8_2 = False
            draw_text_box(screen, (90, 90), (1060, 850), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text9_2, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 70, WIDTH - 130, HEIGHT + 70, 1, (109, 69, 38), scroll_offset, line_visible)
            button9_2.draw(screen, scroll_offset)
            button9_2_2.draw(screen, scroll_offset)
        if done9_2:
            done9_1 = False
            draw_text_box(screen, (90, 200), (1060, 270), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text9_2_1, (120, 250), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 350, WIDTH - 130, HEIGHT - 350, 1, (109, 69, 38), scroll_offset, line_visible)
            button10_1.draw(screen, scroll_offset)
        elif done9_2_2:
            done9_1 = False
            draw_text_box(screen, (90, 120), (1060, 400), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text9_2_2, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 270, WIDTH - 130, HEIGHT - 270, 1, (109, 69, 38), scroll_offset, line_visible)
            button10_2.draw(screen, scroll_offset)


        if done10_1:
            done9_2 = False
            draw_text_box(screen, (90, 200), (1060, 270), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text9_3, (120, 250), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 320, WIDTH - 130, HEIGHT - 320, 1, (109, 69, 38), scroll_offset, line_visible)
            button9_3.draw(screen, scroll_offset)
        if done9_3:
            done10_1 = False
            draw_text_box(screen, (90, 200), (1060, 270), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text10, (120, 250), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 320, WIDTH - 130, HEIGHT - 320, 1, (109, 69, 38), scroll_offset, line_visible)
            button10.draw(screen, scroll_offset)

        if done10:
            done9_3 = False
            draw_text_box(screen, (90, 150), (1060, 450), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text10_1, (120, 180), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 200, WIDTH - 130, HEIGHT - 200, 1, (109, 69, 38), scroll_offset,line_visible)
            button10_3.draw(screen, scroll_offset)
        if done10_3:
            done10 = False
            draw_text_box(screen, (90, 200), (1060, 340), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text10, (120, 250), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 320, WIDTH - 130, HEIGHT - 320, 1, (109, 69, 38), scroll_offset, line_visible)
            button11_1.draw(screen, scroll_offset)
            button11_2.draw(screen, scroll_offset)
        if done11_1:
            done10_3 = False
            draw_text_box(screen, (90, 200), (1060, 280), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text11_1, (120, 250), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 320, WIDTH - 130, HEIGHT - 320, 1, (109, 69, 38), scroll_offset, line_visible)
            button12.draw(screen, scroll_offset)
        elif done11_2:
            done10_3 = False
            draw_text_box(screen, (90, 250), (1060, 220), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text11_2, (150, 300), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 320, WIDTH - 130, HEIGHT - 320, 1, (109, 69, 38), scroll_offset,line_visible)
            button12.draw(screen, scroll_offset)
        if done12 :
            done11_2 = False
            done11_1 = False
            draw_text_box(screen, (90, 150), (1060, 350), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text11_3, (120, 180), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 290, WIDTH - 130, HEIGHT - 290, 1, (109, 69, 38), scroll_offset,line_visible)
            button12_1.draw(screen, scroll_offset)
        if done12_1:
            done12 = False
            draw_text_box(screen, (90, 60), (1060, 720), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text12, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 20, WIDTH - 130, HEIGHT - 20, 1, (109, 69, 38), scroll_offset, line_visible)
            button12_2.draw(screen, scroll_offset)

        if done12_2:
            done12_1 = False
            draw_text_box(screen, (90, 60), (1060, 620), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text13, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 120, WIDTH - 130, HEIGHT - 120, 1, (109, 69, 38), scroll_offset, line_visible)
            button13.draw(screen, scroll_offset)
        if done13:
            done12_2 = False
            draw_text_box(screen, (90, 150), (1060, 450), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text14, (120, 180), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 280, WIDTH - 130, HEIGHT - 280, 1, (109, 69, 38), scroll_offset,line_visible)
            button13_1.draw(screen, scroll_offset)
            button13_2.draw(screen, scroll_offset)
        if done13_1:
            screen.fill((0, 0, 0))
            display_text(screen, "GAME OVER", (430, 120), font3, (255, 0, 0), scroll_offset)
            display_text(screen, tex, (160, 270), font, (255, 255, 255), scroll_offset)
            button37_1.draw(screen, scroll_offset)

        if done37_1:
            break
            #import my_game
            #my_game.main_menu()

        elif done13_2:
            done13 = False
            draw_text_box(screen, (90, 150), (1060, 340), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text14_1, (120, 180), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 330, WIDTH - 130, HEIGHT - 330, 1, (109, 69, 38), scroll_offset,line_visible)
            button14_1.draw(screen, scroll_offset)
        if done14_1:
            done13_2 = False
            draw_text_box(screen, (90, 150), (1060, 340), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text14_2, (120, 180), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 330, WIDTH - 130, HEIGHT - 330, 1, (109, 69, 38), scroll_offset,line_visible)
            button14_2.draw(screen, scroll_offset)
        if done14_2:
            done14_1 = False
            draw_text_box(screen, (90, 60), (1060, 620), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text14_3, (120, 90), font, (255, 255, 255), scroll_offset)
            display_text(screen, msg, (140, 550), font0, (205, 210, 155), scroll_offset)
            draw_line(screen, 130, HEIGHT - 95, WIDTH - 130, HEIGHT - 95, 1, (109, 69, 38), scroll_offset, line_visible)
            button14_3.draw(screen, scroll_offset)
            Script.draw(screen, scroll_offset)

        if done14_3:
            done14_2 = False
            Script.clicked = True
            draw_text_box(screen, (90, 150), (1060, 360), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text15, (120, 180), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 320, WIDTH - 130, HEIGHT - 320, 1, (109, 69, 38), scroll_offset,line_visible)
            button15.draw(screen, scroll_offset)
        if done15:
            done14_3 = False
            draw_text_box(screen, (90, 180), (1060, 220), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, "“nothing really changed thalos..”", (120, 210), font, (255, 255, 255),scroll_offset)
            draw_line(screen, 130, HEIGHT - 420, WIDTH - 130, HEIGHT - 420, 1, (109, 69, 38), scroll_offset,line_visible)
            button15_1.draw(screen, scroll_offset)


        if done15_4:
            done15_1 = False
            done15_2 = False
            button15_2.clicked = True
            draw_text_box(screen, (90, 90), (1060, 600), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, oil_lamp, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 140, WIDTH - 130, HEIGHT - 140, 1, (109, 69, 38), scroll_offset, line_visible)
            button15_5.draw(screen, scroll_offset)
        if done15_5:
            done15_4 = False
            draw_text_box(screen, (90, 90), (1060, 720), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text15_5, (480, 140), font0, (250, 205, 155), scroll_offset)
            display_text(screen, text15_6, (140, 300), font0, (250, 205, 155), scroll_offset)
            display_text(screen, text15_7, (120, 430), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 10, WIDTH - 130, HEIGHT - 10, 1, (109, 69, 38), scroll_offset,line_visible)
            button15_6.draw(screen, scroll_offset)
        if done15_6:
            done60 = False
            done15_5 = False
            done15_4 = False
            draw_text_box(screen, (200, 60), (810, 605), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            original_image = pygame.image.load("resources/images/map.png")
            resized_image = pygame.transform.scale(original_image, (800, 595))
            screen.blit(resized_image, (205, 65 + scroll_offset))
            button15_7.draw(screen, scroll_offset)
        if done15_7:
            done15_6 = False
            done15_4 = False
            draw_text_box(screen, (90, 90), (1060, 600), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text15_8, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 110, WIDTH - 130, HEIGHT - 110, 1, (109, 69, 38), scroll_offset,line_visible)
            button15_8.draw(screen, scroll_offset)
        if done15_8:
            done15_7 = False
            done15_4 = False
            draw_text_box(screen, (90, 90), (1060, 700), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text16, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 30, WIDTH - 130, HEIGHT - 30, 1, (109, 69, 38), scroll_offset, line_visible)
            button16.draw(screen, scroll_offset)
        if done16:
            done15_8 = False
            done15_4 = False
            draw_text_box(screen, (90, 120), (1060, 350), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text16_1, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 350, WIDTH - 130, HEIGHT - 350, 1, (109, 69, 38), scroll_offset,line_visible)
            button16_1.draw(screen, scroll_offset)
        if done16_1:
            done16 = False
            done15_2 = False
            done15_4 = False
            draw_text_box(screen, (90, 150), (1060, 290), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text16_2, (120, 180), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 400, WIDTH - 130, HEIGHT - 400, 1, (109, 69, 38), scroll_offset, line_visible)
            button16_2.draw(screen, scroll_offset)
        if done16_2:
            done16_1 = False
            done15_4 = False
            draw_text_box(screen, (90, 120), (1060, 380), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text16_3, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 320, WIDTH - 130, HEIGHT - 320, 1, (109, 69, 38), scroll_offset,  line_visible)
            button16_3.draw(screen, scroll_offset)
        if done16_3:
            done16_2 = False
            done15_4 = False
            draw_text_box(screen, (90, 60), (1060, 650), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text16_4, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 100, WIDTH - 130, HEIGHT - 100, 1, (109, 69, 38), scroll_offset,line_visible)
            button16_4.draw(screen, scroll_offset)
        if done16_4:
            import TheGame_2
            TheGame_2.play_game2()

        if done10_2:
            done9_2_2 = False
            done9_2 = False
            done10 = True
            done10_2 = False

        elif done5_4:
            done5_2 = False
            draw_text_box(screen, (90, 90), (1060, 700), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text6_4, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 20, WIDTH - 130, HEIGHT - 20, 1,(109, 69, 38), scroll_offset, line_visible)
            button6_2.draw(screen, scroll_offset)
        if done6_2:
            done5_4 = False
            done6_2 = False
            done6_1 = True

        elif done3_2:
            done2_1 = False
            done = False
            done3_2= False
            done4_2 = True

        elif done2_2:
            done1 = False
            button2_1.clicked = True
            button2_2.clicked = True
            draw_text_box(screen, (90, 180), (1060, 300), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text2_2, (130, 230), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 380, WIDTH - 130, HEIGHT - 380, 1, (109, 69, 38), scroll_offset, line_visible)
            button4_1.draw(screen, scroll_offset)
        if done4_1:
            done2_2 = False
            draw_text_box(screen, (90, 60), (1060, 600), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text3_2, (120, 110), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 150, WIDTH - 130, HEIGHT - 150, 1, (109, 69, 38), scroll_offset, line_visible)
            button4_3.draw(screen, scroll_offset)
        if done4_3:
            done4_1 = False
            done4_3 = False
            done4_2 = True

        if done15_1:
            done15 = False
            draw_text_box(screen, (90, 150), (1060, 360), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, hint, (120, 180), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 340, WIDTH - 130, HEIGHT - 340, 1, (109, 69, 38), scroll_offset,  line_visible)
            button15_2.draw(screen, scroll_offset)
            button15_4.draw(screen, scroll_offset)

        if done15_2:
            done15_1 = False
            draw_text_box(screen, (90, 180), (1060, 360), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, fire, (120, 250), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 350, WIDTH - 130, HEIGHT - 350, 1, (109, 69, 38), scroll_offset, line_visible)
            button60.draw(screen, scroll_offset)
        if done60 :
            done15_4 = True
            done15_2 = False
            button15_2.clicked = True
        if done60 and done15_5:
            done15_4 = False

        # Draw the cursor
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

