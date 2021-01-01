import pygame
# Creer classe qui represente notre jeu
from Player import Player
from Monster import Monster, Mummy, Alien
from comet_event import CometFallEvent


class Game:

    def __init__(self):
        self.is_playing = False
        # Génération de notre joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        # Générer l'évènement
        self.comet_event = CometFallEvent(self)
        # groupe de monstres
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        # Remettre le jeu a zéro.
        self.all_monster = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False

    def update(self, screen):
        # Appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        # actualiser la barre d'évènement du jeu
        self.comet_event.update_bar(screen)

        # actualiser l'animation du joueur
        self.player.update_animation()

        # Recupereer les projectile du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Recuperer les projectile du joueur
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # Recuperer les cometes du joueur
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Applique l'image du projectile
        self.player.all_projectiles.draw(screen)

        # Appliquer l'ensemble des images de monstre
        self.all_monster.draw(screen)

        # Appliquer l'ensemble des image du goupe comete
        self.comet_event.all_comets.draw(screen)

        # Verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >= 0:
            self.player.move_left()

    def check_collision(self, sprinte, group):
        return pygame.sprite.spritecollide(sprinte, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        monster = Mummy(self)
        self.all_monster.add(monster_class_name.__call__(self))
