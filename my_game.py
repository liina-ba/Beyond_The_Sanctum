import sys
import TheGame
import time
import pygame
from bottons import Button
# Load the image
icon = pygame.image.load('resources/images/LOGOsanctum.png')

# Set the window icon
pygame.display.set_icon(icon)

# Initialisation de Pygame
pygame.init()

# Définition de la variable globale allowed pour la musique de fond
music_allowed = True

# Définition de la variable globale allowed pour les sons des boutons
sound_allowed = True

# Création de la fenêtre d'affichage
SCREEN = pygame.display.set_mode((1238, 700))
pygame.display.set_caption("Menu")
# Chargement de l'image du curseur personnalisé
cursor_img = pygame.image.load('resources/images/Sans titre.png')
# Redimensionner l'image du curseur
cursor_img = pygame.transform.scale(cursor_img, (40, 40))  # Réglage de la taille du curseur personnalisé
cursor_rect = cursor_img.get_rect()

# Masquer le curseur par défaut
pygame.mouse.set_visible(False)

# Chargement de l'image de fond du menu

bg_image = pygame.image.load("resources/images/bgMenu1.png")
BG = pygame.transform.scale(bg_image, (1280, 720))  # Resize to match window size
font3 = pygame.font.Font("resources/fonts/EBGaramond-VariableFont_wght.ttf", 50)


click_sound = pygame.mixer.Sound("resources/sounds/mouse-click-153941.mp3")
# Définition de la fonction pour obtenir une police avec une taille spécifique
def get_font(size):
    return pygame.font.Font("resources/fonts/CinzelDecorative-Regular (1).ttf", size)



# Définition de la fonction principale pour l'écran des options
def options():
    global sound_allowed, music_allowed
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        pygame.mouse.set_visible(False)

        OPTIONS_BACK = Button(image=None, pos=(610, 600), text_input="BACK", font=get_font(55), base_color="white", hovering_color="Gray")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Bouton pour contrôler la musique de fond
        MUSIC_BUTTON = Button(image=None, pos=(590,250), text_input=" Music", font=get_font(35), base_color=(168, 127, 71), hovering_color="White")

        # Bouton pour contrôler les sons des boutons
        SOUND_BUTTON = Button(image=None, pos=(590, 400),  text_input=" Sound", font=get_font(35), base_color=(168, 127, 71),hovering_color="White")

        # Affichage des boutons
        for button in [OPTIONS_BACK, MUSIC_BUTTON, SOUND_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        # Dessin du curseur
        SCREEN.blit(cursor_img, OPTIONS_MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_click_sound()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    if sound_allowed:
                        back_sound = pygame.mixer.Sound("resources/sounds/mouse-click-153941.mp3")
                        back_sound.play()
                    main_menu()
                elif MUSIC_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    music_allowed = not music_allowed
                    if music_allowed:
                        pygame.mixer.music.unpause()  # Reprendre la musique
                    else:
                        pygame.mixer.music.pause()  # Mettre en pause la musique
                elif SOUND_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    sound_allowed = not sound_allowed

        pygame.display.update()

def play_click_sound():
    global sound_allowed
    if sound_allowed:
        click_sound.play()
# Définition de la fonction principale pour le menu principal
def main_menu():
    global music_allowed, sound_allowed
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # After updating the mouse position, iterate over your buttons and check for hover states:

        MENU_TEXT = get_font(60).render("BEYOND", True, "black")
        MENU_TEXT2 = get_font(60).render("THE SANCTUM", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(topleft=(680, 80))
        MENU_RECT2 = MENU_TEXT2.get_rect(topleft=(580, 150))
        PLAY_BUTTON = Button(image=None, pos=(300, 380),
                             text_input="PLAY", font=get_font(55), base_color="#d7fcd4", hovering_color="Black")

        OPTIONS_BUTTON = Button(image=None, pos=(300, 500),
                                text_input="Settings", font=get_font(55), base_color="#d7fcd4", hovering_color="Black")

        QUIT_BUTTON = Button(image=None, pos=(300, 600),
                             text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="Black")

        SCREEN.blit(cursor_img, MENU_MOUSE_POS)
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(MENU_TEXT2, MENU_RECT2)

        # Affichage des boutons
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            # Récupération de la position de la souris
            mouse_pos = pygame.mouse.get_pos()

            # Dessin du curseur

            SCREEN.blit(cursor_img, mouse_pos)
            # Mise à jour de l'affichage
            pygame.display.flip()
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_click_sound()

                # Placez ici le reste de votre logique de clic pour les autres boutons
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):

                    TheGame.play_game()

                elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):

                    options()
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):

                    time.sleep(0.3)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


pygame.mixer.music.load("resources/sounds/Fantasy Music - Northwind.mp3")
pygame.mixer.music.play(-1)  # Play indefinitely

main_menu()