import pygame


# Definir la classe projectile
class Projectile(pygame.sprite.Sprite):

    # definition du constructeur
    def __init__(self, player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origine_image = self.image
        self.angle = 0

    def rotate(self):
        # faire tourner le projectile
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            # supprimer le projectile
            monster.remove()
            # infliger des dégats
            monster.damage(self.player.attack)


        # Verifie si le projectil n'est plus présent sur l'ecran
        if self.rect.x > 1080:
            # Supprimer
            self.remove()
