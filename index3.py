import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Mixer")

background = pygame.image.load("assets/bg/mixer.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Fonction pour afficher l'arrière-plan
def draw_background():
    screen.blit(background, (0, 0))

# Fonction pour charger les fruits et leurs images
def init_fruits():
    positions_x = [100, 200, 300, 400]
    positions_y = [100, 200, 300, 400, 500]

    fruits = {
        "apricot": pygame.Rect(random.choice(positions_x), 0, 100, 100),
        "banana": pygame.Rect(random.choice(positions_x), 0, 100, 100),
        "fig": pygame.Rect(0, random.choice(positions_y), 100, 100),
        "strawberry": pygame.Rect(0, random.choice(positions_y), 100, 100),
        "mango": pygame.Rect(random.choice(positions_x), HEIGHT - 100, 100, 100),
        "orange": pygame.Rect(random.choice(positions_x), HEIGHT - 100, 100, 100),
        "watermelon": pygame.Rect(WIDTH, random.choice(positions_y), 100, 100),
        "pear": pygame.Rect(WIDTH, random.choice(positions_y), 100, 100),
    }
    
    images = {fruit: pygame.transform.scale(pygame.image.load(f"assets/assets_2/{fruit}.png"), (100, 100)) for fruit in fruits}

    return fruits, images

# Fonction pour déplacer les fruits
def move_fruits(fruits, velocities):
    for fruit, rect in fruits.items():
        rect.move_ip(*velocities[fruit])

# Gérer les collisions entre les fruits
def handle_collisions(fruits, velocities, collicount):
    for fruit, rect in fruits.items():
        if rect.collidelist([f for name, f in fruits.items() if name != fruit]) != -1:
            collicount += 1
            velocities[fruit] = (-velocities[fruit][0], -velocities[fruit][1])
    return collicount

# Afficher les fruits à l'écran
def draw_fruits(fruits, images):
    for fruit, rect in fruits.items():
        screen.blit(images[fruit], rect.topleft)

# Vérifier si un fruit sort de l'écran
def respawn_fruit(fruit, rect, velocities):
    if rect.x > WIDTH or rect.y > HEIGHT or rect.x < -100 or rect.y < -100:
        rect.x = random.choice([100, 200, 300, 400]) if fruit != "fig" else 0
        rect.y = 0 if fruit != "fig" else random.choice([100, 200, 300, 400])
        velocities[fruit] = (random.choice([-2, 2]), random.choice([-2, 2]))

# Détecter une touche pressée pour capturer un fruit
def check_key_press(event, fruits, score):
    key_map = {
        pygame.K_a: "apricot",
        pygame.K_b: "banana",
        pygame.K_f: "fig",
        pygame.K_s: "strawberry",
        pygame.K_m: "mango",
        pygame.K_o: "orange",
        pygame.K_w: "watermelon",
        pygame.K_p: "pear"
    }

    if event.key in key_map:
        fruit_name = key_map[event.key]
        if fruit_name in fruits:
            del fruits[fruit_name]
            score += 1

    return score

# Afficher le score
def draw_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (20, 20))

# Fonction principale du jeu
def main():
    fruits, images = init_fruits()
    velocities = {fruit: (random.choice([-2, 2]), random.choice([-2, 2])) for fruit in fruits}
    collicount = 0
    score = 0
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill((0, 0, 0))  # Fond noir
        draw_background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                score = check_key_press(event, fruits, score)

        # Gérer les collisions et les déplacements
        collicount = handle_collisions(fruits, velocities, collicount)
        move_fruits(fruits, velocities)

        # Affichage des fruits et score
        draw_fruits(fruits, images)
        draw_score(score)

        # Vérifier si un fruit sort de l'écran et le réinitialiser
        for fruit, rect in fruits.items():
            respawn_fruit(fruit, rect, velocities)

        pygame.display.update()
        clock.tick(60)  # 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
