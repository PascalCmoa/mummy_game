import pygame
import random
import animation


# definir la classe qui va générer notre monstre
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        # self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.start_anmation()
        self.loot_amount = 10

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        self.health -= amount

        # vérfier si la vie est inérieur ou égale a 0
        if self.health <= 0:
            # réapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = self.default_speed
            self.health = self.max_health
            self.game.add_score(self.loot_amount)

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


# définir une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(10)


# définir une classe pour la momie
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(50)