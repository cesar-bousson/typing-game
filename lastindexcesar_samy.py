import pygame
import random

pygame.init()

# Configuration de la fenêtre
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Collision Simulation")

# Variables globales
collicount = 0
clock = pygame.time.Clock()

# Chargement des images et redimensionnement
fruit_images = {
    "apricot": pygame.transform.scale(pygame.image.load("assets/assets_2/apricot.png"), (50, 50)),
    "banana": pygame.transform.scale(pygame.image.load("assets/assets_2/banana.png"), (50, 50)),
    "fig": pygame.transform.scale(pygame.image.load("assets/assets_2/fig.png"), (50, 50)),
    "strawberry": pygame.transform.scale(pygame.image.load("assets/assets_2/strawberry.png"), (50, 50)),
    "mango": pygame.transform.scale(pygame.image.load("assets/assets_2/mango.png"), (50, 50)),
    "orange": pygame.transform.scale(pygame.image.load("assets/assets_2/orange.png"), (50, 50)),
    "watermelon": pygame.transform.scale(pygame.image.load("assets/assets_2/watermelon.png"), (50, 50)),
    "pear": pygame.transform.scale(pygame.image.load("assets/assets_2/pear.png"), (50, 50))
}

# Positions de départ des fruits
fruit_positions = {
    "apricot": pygame.Rect(200, 0, 50, 50),
    "banana": pygame.Rect(300, 0, 50, 50),
    "fig": pygame.Rect(0, 100, 50, 50),
    "strawberry": pygame.Rect(0, 200, 50, 50),
    "mango": pygame.Rect(200, 670, 50, 50),
    "orange": pygame.Rect(300, 670, 50, 50),
    "watermelon": pygame.Rect(500, 100, 50, 50),
    "pear": pygame.Rect(500, 200, 50, 50)
}

# Création des objets fruits
fruits = {}
for name, rect in fruit_positions.items():
    fruits[name] = {
        "rect": rect,
        "speed": [random.choice([-2, 2]), random.choice([-2, 2])]
    }

running = True
while running:
    screen.fill((0, 0, 0))

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des collisions et des mouvements
    for name, fruit in fruits.items():
        rect = fruit["rect"]
        speed = fruit["speed"]

        # Vérification des collisions
        other_rects = [fruits[k]["rect"] for k in fruits if k != name]  # Exclure le fruit lui-même
        if rect.collidelist(other_rects) != -1:
            collicount += 1
            print(f"Collision {collicount}: {name}")
            speed[0] = -speed[0]
            speed[1] = -speed[1]

        # Déplacement des fruits
        rect.move_ip(speed[0], speed[1])

        # Réinitialisation si hors écran
        if rect.x > WIDTH or rect.y > HEIGHT or rect.x < -50 or rect.y < -50:
            new_pos = random.choice(list(fruit_positions.values()))
            rect.topleft = (new_pos.x, new_pos.y)
            fruit["speed"][0] = -fruit["speed"][0]
            fruit["speed"][1] = -fruit["speed"][1]

        # Affichage des images
        screen.blit(fruit_images[name], (rect.x, rect.y))

    # Réinitialisation si trop de collisions
    if collicount > 100:
        for name, fruit in fruits.items():
            new_pos = random.choice(list(fruit_positions.values()))
            fruit["rect"].topleft = (new_pos.x, new_pos.y)
        collicount = 0

    pygame.display.update()
    clock.tick(60)

pygame.quit()
