import pygame
import random

pygame.init()

# window & backgrounds:
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("assets/bg/mixer.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

alt_background = pygame.image.load("assets/bg/explosion.jpg")
alt_background = pygame.transform.scale(alt_background, (WIDTH, HEIGHT))
ice_background = pygame.image.load("assets/bg/Ice.jpg")
ice_background = pygame.transform.scale(ice_background, (WIDTH, HEIGHT))

# variables ---------------------------------------------------------------------------------

# load sounds:
fruit_sound = pygame.mixer.Sound("assets/sounds/zapsplat.cut.mp3")
fig_sound = pygame.mixer.Sound("assets/sounds/zapsplat.bomb.mp3")
ice_sound = pygame.mixer.Sound("assets/sounds/ice.mp3")

# associate fruits to keyboards:
keys = [pygame.K_a, pygame.K_b, pygame.K_f, pygame.K_s, pygame.K_m, pygame.K_o, pygame.K_w, pygame.K_p, pygame.K_i]
fruit_names = ["apricot", "banana", "fig", "strawberry", "mango", "orange", "watermelon", "pear", "ice"]
fruit_keys = dict(zip(keys, fruit_names))

# Fruit respawn timers
fruit_respawn_timers = {fruit: 0 for fruit in fruit_names}


# features ------------------------------------------------------------------------------------

def draw_background(current_bg):
    screen.blit(current_bg, (0, 0))

def init_fruits():
    fruits = {}
    images = {}
    positions_x = [100, 200, 300, 400]
    for fruit in fruit_names:
        rect = pygame.Rect(random.choice(positions_x), random.randint(50, HEIGHT - 100), 100, 100)
        fruits[fruit] = rect
        images[fruit] = pygame.transform.scale(pygame.image.load(f"assets/assets_2/{fruit}.png"), (100, 100))
    return fruits, images

def move_fruits(fruits, velocities):
    for fruit, rect in fruits.items():
        rect.move_ip(velocities[fruit])

def draw_fruits(fruits, images):
    font = pygame.font.Font(None, 36)
    for fruit, rect in fruits.items():
        screen.blit(images[fruit], rect.topleft)
        text = font.render(fruit[0].upper(), True, (255, 255, 255))
        screen.blit(text, (rect.x + 40, rect.y + 40))

def respawn_fruit(fruit):
    '''respawn fruit after delay'''
    fruit_respawn_timers[fruit] = pygame.time.get_ticks() + random.randint(2000, 5000)  # 2 / 5 seconds

def check_fruit_respawn(fruits):
    """add fruit erased after a while"""
    current_time = pygame.time.get_ticks()
    for fruit, respawn_time in fruit_respawn_timers.items():
        if respawn_time > 0 and current_time >= respawn_time:
            fruits[fruit] = pygame.Rect(random.choice([100, 200, 300, 400]), random.randint(50, HEIGHT - 100), 100, 100)
            fruit_respawn_timers[fruit] = 0  # init timer

def draw_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (20, 20))
    

# main loop ------------------------------------------------------------------------------------------------

def main():
    fruits, images = init_fruits()
    velocities = {fruit: [random.choice([-2, 2]), random.choice([-2, 2])] for fruit in fruit_names}
    score = 0
    running = True
    clock = pygame.time.Clock()
    current_bg = background
    fig_hit = False
    fig_timer = 0
    # fig_count = 0 to debug
    ice_hit = False
    ice_timer = 0

    while running:
        screen.fill((0, 0, 0))
        draw_background(current_bg)
        draw_fruits(fruits, images)
        draw_score(score)

        if fig_hit:
            fig_timer += 1
            fig_count += 1
            if fig_timer > 30:
                current_bg = background
                fig_hit = False
                fig_timer = 0

        if ice_hit:
            ice_timer += 1
            if ice_timer == 2:
                pygame.time.delay(5000)
                ice_hit = False
                ice_timer = 0
                current_bg = background
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key in fruit_keys:
                    fruit_name = fruit_keys[event.key]
                    if fruit_name in fruits:
                        del fruits[fruit_name]  # erase fruit for a while
                        respawn_fruit(fruit_name)  # init timer for respawn

                        if fruit_name == "ice":
                            current_bg = ice_background
                            ice_hit = True
                            ice_sound.play()
                        elif fruit_name == "fig":
                            score -= 3
                            current_bg = alt_background
                            fig_hit = True
                            fig_sound.play()
                            #if fig_count == 3: need to fix bug here for exit game after losing game with bombs
                                #running = False
                        else:
                            score += 1
                            fruit_sound.play()

        move_fruits(fruits, velocities)
        
        # check if fruits need to respawn
        check_fruit_respawn(fruits)

        # check if a fruit exit the screen
        for fruit in list(fruits.keys()):
            rect = fruits[fruit]
            if rect.x < -100 or rect.x > WIDTH or rect.y < -100 or rect.y > HEIGHT:
                del fruits[fruit]  # erased fruit for a while
                respawn_fruit(fruit)  # init timer of respawn

        pygame.display.update()
        clock.tick(40)

    pygame.quit()

if __name__ == "__main__":
    main()
