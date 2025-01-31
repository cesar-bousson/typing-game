import pygame
import random
import sys

pygame.init()

"""pseudo code
1)
- initialiser la fenêtre
- afficher une fenêtre  pygame : dimension / ecran / affichage /titre / lancement
2)
- générer un backgrund : image / adapter l'image (position * centrer * dimensions/ afficher l'image trouver un moyen pour adapter l'image

"""
# definition window

WIDTH = 640
HEIGHT = 480


background = pygame.image.load("assets/pictures/bg/bg_1.png")

# Obtenir les dimensions originales de l'image
img_width, img_height = background.get_size()

# Calculer le facteur de mise à l'échelle
ratio_width = WIDTH / img_width
ratio_height = WIDTH / img_height
scale_ratio = min(ratio_width, ratio_height)

# Calculer les nouvelles dimensions
new_width = int(img_width * scale_ratio)
new_height = int(img_height * scale_ratio)

screen = pygame.display.set_mode((new_width,HEIGHT))
pygame.display.set_caption("fruitx slicer")

# Redimensionner l'image tout en préservant les proportions
background = pygame.transform.scale(background, (new_width, new_height))

# Boucle principale du jeu
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))


    # Mettre à jour l'écran
    pygame.display.flip()

    # Limiter le nombre de frames par seconde
    clock.tick(60)







# Quitter Pygame proprement
pygame.quit()
sys.exit()