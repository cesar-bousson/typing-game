import pygame
import random

pygame.init()

WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("assets/bg/mixer.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
bg_width, bg_height = background.get_width(), background.get_height()
center_x = (bg_width - WIDTH) // 4
center_y = (bg_height - HEIGHT) // 4

# Fonction pour afficher l'arrière-plan
def draw_background():
    screen.blit(background, (0, 0))

# Fonction pour initialiser les positions et objets
def init_fruits():
    fruits = {
        "apricot": pygame.Rect(random.choice([200, 400, 600, 800]), 0, 100, 100),
        "banana": pygame.Rect(random.choice([300, 500, 700, 900]), 0, 100, 100),
        "fig": pygame.Rect(0, random.choice([100, 400, 600]), 100, 100),
        "strawberry": pygame.Rect(0, random.choice([200, 300, 500]), 100, 100),
        "mango": pygame.Rect(random.choice([200, 400, 600, 800]), 670, 100, 100),
        "orange": pygame.Rect(random.choice([300, 500, 700, 900]), 670, 100, 100),
        "watermelon": pygame.Rect(1030, random.choice([100, 400, 600]), 100, 100),
        "pear": pygame.Rect(1030, random.choice([200, 300, 500]), 100, 100),
    }
    
    images = {
        "apricot": pygame.transform.scale(pygame.image.load("assets/assets_2/apricot.png"), (100, 100)),
        "banana": pygame.transform.scale(pygame.image.load("assets/assets_2/banana.png"), (100, 100)),
        "fig": pygame.transform.scale(pygame.image.load("assets/assets_2/fig.png"), (100, 100)),
        "strawberry": pygame.transform.scale(pygame.image.load("assets/assets_2/strawberry.png"), (100, 100)),
        "mango": pygame.transform.scale(pygame.image.load("assets/assets_2/mango.png"), (100, 100)),
        "orange": pygame.transform.scale(pygame.image.load("assets/assets_2/orange.png"), (100, 100)),
        "watermelon": pygame.transform.scale(pygame.image.load("assets/assets_2/watermelon.png"), (100, 100)),
        "pear": pygame.transform.scale(pygame.image.load("assets/assets_2/pear.png"), (100, 100)),
    }
    
    return fruits, images

def check_key_press(key):
    score = 0
    fruits =[]
    key = pygame.key.name(key)
    if key in fruits:
        fruit = fruits[key]
        if fruit["rect"].colliderect(pygame.Rect(0, 0, WIDTH, HEIGHT)):
            score += 1  # Maintenant, score est bien reconnu comme global
            fruit["rect"] = pygame.Rect(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50), 50, 50)  # Repositionne le fruit


# Fonction pour gérer le mouvement des fruits
def move_fruits(fruits, velocities):
    for fruit, rect in fruits.items():
        rect.move_ip(velocities[fruit][0], velocities[fruit][1])

# Fonction pour gérer les collisions
def handle_collisions(fruits, velocities, collicount):
    for fruit, rect in fruits.items():
        if rect.collidelist([f for name, f in fruits.items() if name != fruit]) != -1:
            collicount += 1
            velocities[fruit][0] = -velocities[fruit][0]
            velocities[fruit][1] = -velocities[fruit][1]
    return collicount

# Fonction pour afficher les fruits
def draw_fruits(fruits, images):
    for fruit, rect in fruits.items():
        screen.blit(images[fruit], rect.topleft)

# Fonction pour vérifier si un fruit est hors de l'écran et le réinitialiser
def respawn_fruit(fruit, rect, velocities):
    if rect.x > 1330 or rect.y > 970 or rect.x < -250 or rect.y < -250:
        rect.x = random.choice([200, 400, 600, 800]) if fruit != "fig" else 0
        rect.y = 0 if fruit != "fig" else random.choice([100, 400, 600])
        velocities[fruit][0] = -velocities[fruit][0]
        velocities[fruit][1] = -velocities[fruit][1]

# Fonction principale du jeu
def main():
    # Initialisation
    fruits, images = init_fruits()
    velocities = {
        "apricot": [-2, -2],
        "banana": [-2, 2],
        "fig": [2, 0],
        "strawberry": [1, 2],
        "mango": [2, 2],
        "orange": [2, 1],
        "watermelon": [-2, 2],
        "pear": [-1, -1],
    }
    collicount = 0
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mise à jour de l'écran
        screen.fill((0, 0, 0))  # Fond noir
        draw_background()

        # Gérer les collisions
        collicount = handle_collisions(fruits, velocities, collicount)

        # Déplacer les fruits
        move_fruits(fruits, velocities)

        # Afficher les fruits
        draw_fruits(fruits, images)

        # Vérifier si un fruit est hors écran et respawn
        for fruit, rect in fruits.items():
            respawn_fruit(fruit, rect, velocities)

        # Mettre à jour l'affichage
        pygame.display.update()

        # Contrôler le FPS
        clock.tick(1000)

    pygame.quit()

if __name__ == "__main__":
    main()
