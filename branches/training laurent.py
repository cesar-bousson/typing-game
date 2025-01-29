import pygame
import random

pygame.init()

""" pseudo code 
1) 
- initialiser la fenetre
- afficher la fenetre pygame : titre - dimensions / ecran / affichage / lancement 

2) generer un background : image / adapter l'image (position * centrer * dimensions) / afficher ( trouver moyen de trouver la dimension image pour adapter a lecran.)

3) creer boucle principale

4) afficher fruit """

WIDTH = 3310
HEIGHT = 1080


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruitix Slicer")
background = pygame.image("assets/pictures/bg/bg_1.png")

def main_loop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


pygame.quit()
