import pygame
import random

pygame.init()

# Configuration de la fenêtre
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Collision Simulation")

# Variables globales
collicount = 0
clock = pygame.time.Clock()

# Liste de positions initiales pour les fruits
spawn_positions = {
    "top": [(200, 0), (400, 0), (600, 0), (800, 0)],
    "left": [(0, 100), (0, 400), (0, 600)],
    "bottom": [(200, 670), (400, 670), (600, 670), (800, 670)],
    "right": [(1030, 100), (1030, 400), (1030, 600)]
}

# Définition des fruits et de leurs propriétés
apricot_image = pygame.image.load("assets/assets_2/apricot.png")

fruits = {
    "apricot": {"pos": random.choice(spawn_positions["top"]), apricot_image, "speed": [-2, -2]},
    "banana": {"pos": random.choice(spawn_positions["top"]), "color": (255, 255, 0), "speed": [-2, 2]},
    "fig": {"pos": random.choice(spawn_positions["left"]), "color": (255, 0, 100), "speed": [2, 0]},
    "strawberry": {"pos": random.choice(spawn_positions["left"]), "color": (200, 0, 0), "speed": [1, 2]},
    "mango": {"pos": random.choice(spawn_positions["bottom"]), "color": (0, 200, 100), "speed": [2, 2]},
    "orange": {"pos": random.choice(spawn_positions["bottom"]), "color": (0, 255, 0), "speed": [2, 1]},
    "watermelon": {"pos": random.choice(spawn_positions["right"]), "color": (0, 0, 255), "speed": [-2, 2]},
    "pear": {"pos": random.choice(spawn_positions["right"]), "color": (0, 150, 250), "speed": [-1, -1]}
}

# Création des objets Rect
for fruit in fruits.values():
    fruit["rect"] = pygame.Rect(fruit["pos"][0], fruit["pos"][1], 50, 50)

# Liste des colliders
colliders = [fruits[name]["rect"] for name in fruits]

running = True

while running:
    screen.fill((0, 0, 0))

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des collisions
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

        # Dessin des fruits
        pygame.draw.rect(screen, fruit["color"], rect, 2)

        # Réinitialisation si hors écran
        if rect.x > 1330 or rect.y > 970 or rect.x < -250 or rect.y < -250:
            fruit["rect"].x, fruit["rect"].y = random.choice(spawn_positions[random.choice(["top", "left", "bottom", "right"])])
            fruit["speed"][0] = -fruit["speed"][0]
            fruit["speed"][1] = -fruit["speed"][1]

    # Réinitialisation si trop de collisions
    if collicount > 100:
        for name, fruit in fruits.items():
            fruit["rect"].x, fruit["rect"].y = random.choice(spawn_positions[random.choice(["top", "left", "bottom", "right"])])
        collicount = 0

    pygame.display.update()
    clock.tick(60)

pygame.quit()
