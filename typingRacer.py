import copy
import sys
import pygame
import random


def typing_racer_game():
    global high_score
    global word_index
    pygame.init()

    list_words = ["aiden", "wisdom", "is",  "the", "solution"]
    wordlist = list_words
    word_index = 0
    len_indexes = []
    length = 1

    WIDTH = 1238
    HEIGHT = 700
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('Typing Racer!')
    surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    timer = pygame.time.Clock()
    fps = 60

    score = 0
    correct_taps = 0

    header_font = pygame.font.Font('assets/fonts/Square.ttf', 50)
    header_font1 = pygame.font.Font('assets/fonts/Square.ttf', 40)
    pause_font = pygame.font.Font('assets/fonts/1up.ttf', 38)
    banner_font = pygame.font.Font('assets/fonts/1up.ttf', 28)
    font = pygame.font.Font('assets/fonts/AldotheApache.ttf', 48)
    # music and sounds
    click = pygame.mixer.Sound('assets/sounds/click.mp3')
    woosh = pygame.mixer.Sound('assets/sounds/Swoosh.mp3')
    wrong = pygame.mixer.Sound('assets/sounds/wrong.mp3')
    click.set_volume(0.3)
    woosh.set_volume(0.2)
    wrong.set_volume(0.3)
    background_image = pygame.image.load('assets/images/gamebg.png')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    # game variables
    level = 1
    lives = 1
    word_objects = []
    file = open('high_score.txt', 'r')
    read = file.readlines()
    high_score = int(read[0])
    file.close()
    pz = True
    new_level = True
    submit = ''
    active_string = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    class Word:
        def __init__(self, text, speed, y_pos, x_pos):
            self.text = text
            self.speed = speed
            self.y_pos = y_pos
            self.x_pos = x_pos

        def draw(self):
            color = 'white'
            screen.blit(font.render(self.text, True, color), (self.x_pos, self.y_pos))
            act_len = len(active_string)
            if active_string == self.text[:act_len]:
                screen.blit(font.render(active_string, True, 'green'), (self.x_pos, self.y_pos))

        def update(self):
            self.x_pos -= self.speed

    class Button:
        def __init__(self, x_pos, y_pos, text, clicked, surf):
            self.x_pos = x_pos
            self.y_pos = y_pos
            self.text = text
            self.clicked = clicked
            self.surf = surf

        def draw(self):
            cir = pygame.draw.circle(self.surf, (45, 89, 135), (self.x_pos, self.y_pos), 35)
            if cir.collidepoint(pygame.mouse.get_pos()):
                butts = pygame.mouse.get_pressed()
                if butts[0]:
                    pygame.draw.circle(self.surf, (190, 35, 35), (self.x_pos, self.y_pos), 35)
                    self.clicked = True
                else:
                    pygame.draw.circle(self.surf, (190, 89, 135), (self.x_pos, self.y_pos), 35)
            pygame.draw.circle(self.surf, 'white', (self.x_pos, self.y_pos), 35, 3)
            self.surf.blit(pause_font.render(self.text, True, 'white'), (self.x_pos - 15, self.y_pos - 25))

    def draw_screen():
        # screen outlines for main game window and 'header' section
        pygame.draw.rect(screen, 'white', [0, 0, WIDTH, HEIGHT], 5)
        pygame.draw.line(screen, 'white', (0, HEIGHT - 100), (WIDTH, HEIGHT - 100), 2)

        # text for showing current level, player's current string, high score and pause options
        screen.blit(header_font.render(f'"{active_string}"', True, 'white'), (270, HEIGHT - 75))
        pause_btn = Button(1150, HEIGHT - 52, 'II', False, screen)
        pause_btn.draw()
        # draw lives, score, and high score on top of screen
        screen.blit(banner_font.render(f'Score: {score}', True, 'white'), (480, 10))
        screen.blit(banner_font.render(f'Best: {high_score}', True, 'white'), (820, 10))
        screen.blit(banner_font.render(f'Lives: {lives}', True, 'white'), (170, 10))
        return pause_btn.clicked

    def draw_pause():
        surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surface, (0, 0, 0, 100), [320, 150, 600, 370], 0, 5)
        pygame.draw.rect(surface, (0, 0, 0, 200), [320, 150, 600, 370], 5, 5)

        resume_btn = Button(510, 320, '>', False, surface)
        if correct_taps < 7:
          resume_btn.draw()
        quit_btn = Button(510, 430, 'X', False, surface)
        quit_btn.draw()

        # Draw the "PLAY" button only if the user has not won
        if correct_taps < 7:
            surface.blit(header_font.render('MENU', True, 'white'), (550, 200))
            surface.blit(header_font.render('PLAY', True, 'white'), (570, 300))
        surface.blit(header_font.render('QUIT', True, 'white'), (570, 410))
        if correct_taps == 7:
            surface.blit(header_font.render('You win!', True, 'green'), (500, 170))
            surface.blit(header_font1.render('Now Go solve the riddle', True, 'white'), (380, 300))

        screen.blit(surface, (0, 0))
        return resume_btn.clicked, quit_btn.clicked

    def generate_level():
        global word_index
        word_objs = []
        vertical_spacing = (HEIGHT - 150) // level

        for i in range(level):
            speed = random.randint(2, 3)
            y_pos = random.randint(10 + (i * vertical_spacing), (i + 1) * vertical_spacing)
            x_pos = random.randint(WIDTH, WIDTH + 1000)
            index = word_index  # Use the current word index
            text = wordlist[index].lower()
            new_word = Word(text, speed, y_pos, x_pos)
            word_objs.append(new_word)
            word_index = (word_index + 1) % len(wordlist)  # Increment and wrap the index
        return word_objs

    def check_answer(scor):
        for wrd in word_objects:
            if wrd.text == submit:
                points = wrd.speed * len(wrd.text) * 10 * (len(wrd.text) / 4)
                scor += int(points)
                word_objects.remove(wrd)
                woosh.play()
        return scor

    def check_answer(scor):
        for wrd in word_objects:
            if wrd.text == submit:
                points = wrd.speed * len(wrd.text) * 10 * (len(wrd.text) / 4)
                scor += int(points)
                word_objects.remove(wrd)
                woosh.play()
        return scor

    def check_high_score():
        global high_score
        if score > high_score:
            high_score = score
            file = open('high_score.txt', 'w')
            file.write(str(int(high_score)))
            file.close()

    run = True
    while run:
        screen.blit(background_image, (0,0))
        timer.tick(fps)
        pause_butt = draw_screen()
        if pz:
            resume_butt, quit_butt = draw_pause()
            if resume_butt:
                pz = False
            if quit_butt:
                check_high_score()
                import TheGame_2
                TheGame_2.play_game2()

        if new_level and not pz:
            word_objects = generate_level()
            new_level = False
        else:
            for w in word_objects:
                w.draw()
                if not pz:
                    w.update()
                if w.x_pos < -200:
                    word_objects.remove(w)
                    lives -= 1
        if len(word_objects) <= 0 and not pz:
            level += 1
            new_level = True

        if submit != '':
            init = score
            score = check_answer(score)
            submit = ''
            if init == score:
                wrong.play()
            else:
                correct_taps+=1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                check_high_score()
                import TheGame_2
                TheGame_2.play_game2()


            if event.type == pygame.KEYDOWN:
                if not pz:
                    if event.unicode.lower() in letters:
                        active_string += event.unicode
                        click.play()
                    if event.key == pygame.K_BACKSPACE and len(active_string) > 0:
                        active_string = active_string[:-1]
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        submit = active_string
                        active_string = ''
                if event.key == pygame.K_ESCAPE:
                    if pz:
                        pz = False
                    else:
                        pz = True

        if pause_butt:
            pz = True

        if lives < 0:
            pz = True
            level = 1
            lives = 1
            word_objects = []
            new_level = True
            check_high_score()
            score = 0
            correct_taps = 0
        if correct_taps == 7:
            pz = True
            level = 1
            lives = 1
            word_objects = []
            new_level = True
            check_high_score()
            score = 0

        # Draw the cursor
        cursor_img = pygame.image.load('resources/images/Sans titre.png')
        cursor_img = pygame.transform.scale(cursor_img, (40, 40))  # Resize cursor image
        cursor_pos = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_pos)

        pygame.display.flip()
typing_racer_game()
