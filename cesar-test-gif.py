import pygame
from PIL import Image, ImageSequence
pygame.init()

# window
WIDTH, HEIGHT = 600, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FRUITIX SLICER")
clock = pygame.time.Clock()

# BACKGROUND-----------------------------------------------------------------------------------------------------

# load gif frames
image = Image.open("assets/gifs/Glow Digital Art GIF by time.gif")
frames = [pygame.image.fromstring(frame.convert("RGBA").tobytes(), frame.size, "RGBA")
          for frame in ImageSequence.Iterator(image)]

#-------------------------------------------------------------------------------------------------

def display_fruit():
    
    fruit_pictures = {
        
        "ice" : pygame.image.load("assets/pictures/asset.ice.png"),}
    #     "watermelon": pygame.image.load(""),
    #     "peach" : pygame.image.load(""),
    #     "figue" : pygame.image.load(""),
    #     "mango" : pygame.image.load(""),
    #     "bomb" : pygame.image.load(""),
    #     "none" : pygame.image.load("")
    # }
    
    
    for fruit, image in fruit_pictures.items(): # > for key, value in ...<
        pic_sizes = pygame.transform.scale(image, (200, 300))
    
        screen.blit(pic_sizes, (100,100))
        pygame.display.flip()

#loop main  
def main_loop():
    clock = pygame.time.Clock()
    frame_index = 0
    running = True
    key = pygame.key.get_pressed()
    
    cut_orange = pygame.image.load("")
    cut_watermelon = pygame.image.load("")
    cut_figue = pygame.image.load("")
    cut_mango = pygame.image.load("")
    cut_peach = pygame.image.load("")
    cut_ice = pygame.image.load("")
    cut_bomb = pygame.image.load("")
    
    display_fruit()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN: 
                
                if key [pygame.K_a]:
                    #si la touche est a , alors coupe le fruit pastheque et affiche l'image splash. rafraichis et enleve le splash. score +1
                    screen.fill(image)
                    pygame.display.flip(cut_figue)
                    pygame.display.update()
                    clock.tick(60)
                    
                    
                elif key [pygame.K_z]:
                    pass
                    
                
                elif key [pygame.K_e]:
                    pass
                    
                
                elif key [pygame.K_r]:
                    pass
                    
                elif key [pygame.K_y]:
                    pass
                
                
        # ---------------------------------
        # Afficher la frame actuelle
        screen.blit(pygame.transform.scale(frames[frame_index], (WIDTH, HEIGHT)), (0, 0))
        # Mettre à jour l'index de la frame
        frame_index = (frame_index + 1) % len(frames)
        # ---------------------------------
        
        
        
        # reload
        pygame.display.flip()
        clock.tick(10)  # Ajuste la vitesse d'animation (FPS)

    pygame.quit()
    
main_loop()