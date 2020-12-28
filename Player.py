import pygame

# Creation de la classe joueur
from Projectile import Projectile
import animation


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 5
        # self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.all_projectiles = pygame.sprite.Group()

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # le joueur n'a plus point de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # definir une couleur pour la jauge de vie
        bar_color = (0, 4, 255)
        back_bar_color = (50, 50, 50)

        # definir la position de la jauge de vie
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 5]
        # definition de l'arriere plan
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 5]

        # dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        # Création nouvelle instance de projectile
        self.all_projectiles.add(Projectile(self))
        self.start_anmation()

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
