import pygame
import random


pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("assets/gifs/I Can Woman GIF.gif")
bg_width, bg_height = background.get_size()
x_pos = (WIDTH - bg_width) // 2
y_pos = (HEIGHT- bg_height) // 2

pygame.display.set_caption("Fruity Slicer")

# ------------------------------------------------------------
fruit_images = [
    pygame.image.load("assets/assets_2/apricot.png"), 
    pygame.image.load("assets/assets_2/banana.png"),
    pygame.image.load("assets/assets_2/mango.png"),
    pygame.image.load("assets/assets_2/mango.png"),
    pygame.image.load("assets/assets_2/orange.png"),
    pygame.image.load("assets/assets_2/pear.png"),
    pygame.image.load("assets/assets_2/strawberry.png"),
    pygame.image.load("assets/assets_2/watermelon.png")
]

#special fruits:
ice_image = pygame.image.load("assets/pictures/asset.ice.png")
bomb_image = pygame.image.load("assets/assets_2/fig.png")

fruit_images = [pygame.transform.scale(img, (50, 50)) for img in fruit_images]
ice_image = pygame.transform.scale(ice_image, (50, 50))
bomb_image = pygame.transform.scale(bomb_image, (50, 50))

#---------------------------------------------------------------

clock = pygame.time.Clock()
fruits = []
score = 0
running = True

# ---------------------------------


def create_fruit():
    image = random.choice(fruit_images + [ice_image, bomb_image])
    x = random.randint(100, WIDTH - 100)
    y = HEIGHT
    speed = random.randint(5, 10)
    rect = image.get_rect(center=(x, y))
    
    return image, x, y, speed, rect

def display_score():
    font = pygame.font.SysFont('Arial', 30)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
# -------------------------------------------------------------------

#main loop
while running:
    screen.blit(background,(x_pos, y_pos))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        for fruit in fruits:
            image, x, y, speed, rect = fruit
            if rect.collidepoint(mouse_x, mouse_y):
                fruits.remove(fruit)
                score += 1

    if random.random() < 0.02:
        fruits.append(create_fruit())

    for fruit in fruits[:]:
        image, x, y, speed, rect = fruit
        y -= speed
        rect.center = (x, y)

        if y < 0:
            fruits.remove(fruit)
            score -= 1

        screen.blit(image, rect)

    
    display_score()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

