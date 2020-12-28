import pygame
import random
import animation


# definir la classe qui va générer notre monstre
class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        # self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 5)
        self.start_anmation()

    def damage(self, amount):
        self.health -= amount

        # vérfier si la vie est inérieur ou égale a 0
        if self.health <= 0:
            # réapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 5)
            self.health = self.max_health

            # si la barre d'evènement est a son maxi
            if self.game.comet_event.is_full_loaded():
                self.game.all_monster.remove(self)

                # Appel de la méthode pour essayer de déclencher la pluie de comete
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # definir une couleur pour la jauge de vie => Rouge
        bar_color = (190, 249, 179)
        back_bar_color = (50, 50, 50)

        # definir la position de la jauge de vie
        bar_position = [self.rect.x + 10, self.rect.y - 15, self.health, 5]
        # definition de l'arriere plan
        back_bar_position = [self.rect.x + 10, self.rect.y - 15, self.max_health, 5]

        # dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # Pas de collision avec un joueur
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        else:
            # infliger des dégats au joueur
            self.game.player.damage(self.attack)
