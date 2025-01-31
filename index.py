import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("assets/gifs/I Can Woman GIF.gif")

clock = pygame.time.Clock()

fruit_images = {
    "a" : pygame.image.load("assets/assets_2/apricot.png"), 
    "z" : pygame.image.load("assets/assets_2/banana.png"),
    "e" : pygame.image.load("assets/assets_2/mango.png"),
    "r" : pygame.image.load("assets/assets_2/mango.png"),
    "t" : pygame.image.load("assets/assets_2/orange.png"),
    "y" : pygame.image.load("assets/assets_2/pear.png"),
    "u" : pygame.image.load("assets/assets_2/strawberry.png"),
    "i" : pygame.image.load("assets/assets_2/watermelon.png")
    }

#special fruits:
ice_image = pygame.image.load("assets/pictures/asset.ice.png")
bomb_image = pygame.image.load("assets/assets_2/fig.png")

#resize:
fruit_images = [pygame.transform.scale(img, (50, 50)) for img in fruit_images]
ice_image = pygame.transform.scale(ice_image, (50, 50))
bomb_image = pygame.transform.scale(bomb_image, (50, 50))


# ------------
fruits = []
ices = []
bombs = []
speed = 5
score = 0
running = True
# --------------

for _ in range(9):
    
    fruits.append ([random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), random.choice(fruit_images)])
    
    bombs.append ([random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)])
    
    ices.append ([random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)])

player_x, player_y = WIDTH // 2, HEIGHT // 2
player_size = 50

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    for fruit in fruits[:]:
        screen.blit(fruit[2], (fruit[0], fruit[1]))
        if abs(player_x - fruit[0]) < player_size and abs(player_y - fruit[1]) < player_size:
            fruits.remove(fruit)
            score += 1
    
    for bomb in bombs:
        screen.blit(bomb_image, (bomb[0], bomb[1]))
        if abs(player_x - bomb[0]) < player_size and abs(player_y - bomb[1]) < player_size:
            running = False
    
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_size, player_size))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
