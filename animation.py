import pygame


class AnimateSprite(pygame.sprite.Sprite):

    # Définir les elements a faire a la création de l'entite
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0  # Commence l'animation a l'image 0
        self.images = animation.get(sprite_name)
        self.animation = False

    #
    def start_anmation(self):
        self.animation = True

    # definir une méthode pour animer le sprite
    def animate(self, loop=False):

        if self.animation:

            # passer à l'image suivante
            self.current_image += 1
            # A-t'on atteint la dernière images
            if self.current_image >= len(self.images):
                self.current_image = 0
                self.animation = False

                if loop is False:
                    # modifier l'image de l'animation prev -> next
                    self.image = self.images[self.current_image]
                    self.image = pygame.transform.scale(self.image, self.size)

# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les images du sprite
    images = []
    # recupérer le chemein du dossier
    path = f"assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque images du dossier
    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu
    return images


# definir un dico contenant les images chargées de chaque sprites
animation = {
    "mummy": load_animation_images("mummy"),
    "player": load_animation_images("player"),
    "alien": load_animation_images("alien"),
}
