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

# Liste des positions initiales pour les fruits
spawn_positions = {
    "top": [(200, 0), (400, 0), (600, 0), (800, 0)],
    "left": [(0, 100), (0, 400), (0, 600)],
    "bottom": [(200, 670), (400, 670), (600, 670), (800, 670)],
    "right": [(1030, 100), (1030, 400), (1030, 600)]
}

# Chargement des images
fruit_images = {
    "apricot": pygame.image.load("assets/assets_2/apricot.png"),
    "banana": pygame.image.load("assets/assets_2/banana.png"),
    "fig": pygame.image.load("assets/assets_2/fig.png"),
    "strawberry": pygame.image.load("assets/assets_2/strawberry.png"),
    "mango": pygame.image.load("assets/assets_2/mango.png"),
    "orange": pygame.image.load("assets/assets_2/orange.png"),
    "watermelon": pygame.image.load("assets/assets_2/watermelon.png"),
    "pear": pygame.image.load("assets/assets_2/pear.png")
}


# Définition des fruits et de leurs propriétés

fruits = {
    "apricot": {"pos": random.choice(spawn_positions["top"]), "speed": [-2, -2]},
    "banana": {"pos": random.choice(spawn_positions["top"]), "speed": [-2, 2]},
    "fig": {"pos": random.choice(spawn_positions["left"]), "speed": [2, 0]},
    "strawberry": {"pos": random.choice(spawn_positions["left"]), "speed": [1, 2]},
    "mango": {"pos": random.choice(spawn_positions["bottom"]), "speed": [2, 2]},
    "orange": {"pos": random.choice(spawn_positions["bottom"]), "speed": [2, 1]},
    "watermelon": {"pos": random.choice(spawn_positions["right"]), "speed": [-2, 2]},
    "pear": {"pos": random.choice(spawn_positions["right"]), "speed": [-1, -1]}
}
#resize image
for key in fruit_images:
    fruit_images[key] = pygame.transform.scale(fruit_images[key], (100, 100))
    
# Création des objets Rect en fonction de la taille des images
for name, fruit in fruits.items():
    img = fruit_images[name]
    fruit["rect"] = pygame.Rect(fruit["pos"][0], fruit["pos"][1], img.get_width(), img.get_height())

# Liste des colliders
colliders = [fruits[name]["rect"] for name in fruits]

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

        if rect.collidelist(colliders) != -1:
            collicount += 1
            print(collicount)
            speed[0] = -speed[0]
            speed[1] = -speed[1]

        # Déplacement des fruits
        rect.move_ip(speed[0], speed[1])

        # Affichage des images
        screen.blit(fruit_images[name], (rect.x, rect.y))

        # Réinitialisation si hors écran
        if rect.x > 950 or rect.y > 500 or rect.x < -250 or rect.y < -250:
            fruit["rect"].x, fruit["rect"].y = random.choice(spawn_positions[random.choice(["top", "left", "bottom", "right"])])
            fruit["speed"][0] = -fruit["speed"][0]
            fruit["speed"][1] = -fruit["speed"][1]

    # Réinitialisation si trop de collisions
    if collicount > 100:
        for name, fruit in fruits.items():
            fruit["rect"].x, fruit["rect"].y = random.choice(spawn_positions[random.choice(["top", "left", "bottom", "right"])])
        collicount = 0

    pygame.display.update()
    clock.tick(120)

pygame.quit()
