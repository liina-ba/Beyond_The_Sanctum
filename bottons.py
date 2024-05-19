
class Button():
    # Constructeur de la classe
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image  # L'image du bouton
        self.x_pos = pos[0]  # La position x du bouton
        self.y_pos = pos[1]  # La position y du bouton
        self.font = font  # La police du texte sur le bouton
        self.base_color, self.hovering_color = base_color, hovering_color  # Les couleurs du texte
        self.text_input = text_input  # Le texte sur le bouton
        # Rendu du texte avec la couleur de base
        self.text = self.font.render(self.text_input, True, self.base_color)
        # Si aucune image n'est fournie, utilise le texte comme image
        if self.image is None:
            self.image = self.text
        # Obtention du rectangle de l'image et du texte
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    # Méthode pour mettre à jour l'affichage du bouton
    def update(self, screen):
        # Affiche l'image du bouton si elle existe
        if self.image is not None:
            screen.blit(self.image, self.rect)
        # Affiche le texte du bouton
        screen.blit(self.text, self.text_rect)

    # Méthode pour vérifier si le bouton est cliqué
    def checkForInput(self, position):
        # Vérifie si la position de la souris est dans le rectangle du bouton
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    # Méthode pour changer la couleur du texte lorsque la souris est sur le bouton
    def changeColor(self, position):
        # Si la souris est sur le bouton, change la couleur du texte en couleur de survol
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        # Sinon, change la couleur du texte en couleur de base
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
