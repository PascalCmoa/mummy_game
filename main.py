# all imports

import pygame
import math
from Game import Game

pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("Cometes fall game")
screen = pygame.display.set_mode((1080, 720))

# importer l'arriere plan
background = pygame.image.load('assets/bg.jpg')

# importer la banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer le bouton
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger notre jeu
game = Game()

running = True

# boucle tant que running est vrai
while running:

    # Appliquer l'arriere plan à notre jeu
    screen.blit(background, (0, -200))

    # Vérifier si le jeu a commence ou pas
    if game.is_playing:
        # déclencher les instructions de la partie
        game.update(screen)
    # verifier si le jeu n'a pas comencer
    else:
        # ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre a jour l'ecran
    pygame.display.flip()

    # Si le jeu ferme la fenetre
    for event in pygame.event.get():
        # Verifier que l'évènement de fermeture fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Detection lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Détecter si SPACE est utilisée
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifie si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancé
                game.start()
