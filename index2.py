import pygame
import random
import glob

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruity Slicer")

# Charger les frames du GIF comme une animation
background_frames = [pygame.image.load(frame) for frame in sorted(glob.glob("assets/gifs/I_Can_Woman_*.png"))]
current_frame = 0
frame_delay = 5
frame_counter = 0

fruit_images = [
    pygame.image.load("assets/assets_2/apricot.png"), 
    pygame.image.load("assets/assets_2/banana.png"),
    pygame.image.load("assets/assets_2/mango.png"),
    pygame.image.load("assets/assets_2/orange.png"),
    pygame.image.load("assets/assets_2/pear.png"),
    pygame.image.load("assets/assets_2/strawberry.png"),
    pygame.image.load("assets/assets_2/watermelon.png")
]

ice_image = pygame.image.load("assets/pictures/asset.ice.png")
bomb_image = pygame.image.load("assets/assets_2/fig.png")

clock = pygame.time.Clock()
fruits = []
score = 0
running = True



def create_fruit():
    image = random.choice(fruit_images + [ice_image, bomb_image])
    x = random.randint(100, WIDTH - 100)
    y = HEIGHT
    speed = random.randint(5, 10)
    rect = image.get_rect(center=(x, y))
    return [image, x, y, speed, rect]

def display_score():
    font = pygame.font.SysFont('Arial', 30)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    

while running:
    frame_counter += 1
    if frame_counter >= frame_delay:
        frame_counter = 0
        current_frame = (current_frame + 1) % len(background_frames)
    
    screen.blit(background_frames[current_frame], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        for fruit in fruits[:]:
            image, x, y, speed, rect = fruit
            if rect.collidepoint(mouse_x, mouse_y):
                fruits.remove(fruit)
                # global score
                score += 1

    if random.random() < 0.02:
        fruits.append(create_fruit())

    for fruit in fruits[:]:
        image, x, y, speed, rect = fruit
        y -= speed
        rect.center = (x, y)

        if y < 0:
            fruits.remove(fruit)
            score = max(0, score - 1)
        else:
            fruit[2] = y
            fruit[4] = rect

        screen.blit(image, rect)

    display_score()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
