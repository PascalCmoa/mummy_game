import pygame
from comet import Comet

# créer une classe pour gerer l'évènement
class CometFallEvent:

    # lors du chargement, créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        # définir un groupe de sprite
        self.all_comets = pygame.sprite.Group()
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 10

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        for i in range(1, 10):
            # FAire apparaitre les boules de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge est pleine
        if self.is_full_loaded() and len(self.game.all_monster) == 0:
            self.meteor_fall()
            self.fall_mode = True #Activer l'évènement


    def update_bar(self, surface):

        # ajout poucentage
        self.add_percent()

        # barre noire en bg
        pygame.draw.rect(surface, (0, 0, 0), [
            0  # l'axe des x
            , surface.get_height() - 20  # l'axe des y
            , surface.get_width()  # la longueur de la fenetre
            , 10  # la hauteur de la barre
        ])
        # barre rouge en fg
        pygame.draw.rect(surface, (189, 11, 11), [
            0  # l'axe des x
            , surface.get_height() - 20  # l'axe des y
            , (surface.get_width() / 100) * self.percent # la longueur de la fenetre
            , 10  # la hauteur de la barre
        ])
