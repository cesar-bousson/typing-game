import pygame
from PIL import Image, ImageSequence
pygame.init()


# window
WIDTH, HEIGHT = 600, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fond d'écran GIF avec Pygame")

# BACKGROUND-----------------------------------------------------------------------------------------------------

# load gif frames
gif_path = "assets/gifs/I Can Woman GIF.gif"
image = Image.open(gif_path)
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
    
    display_fruit()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
                
                
        # ---------------------------------
        # Afficher la frame actuelle
        screen.blit(pygame.transform.scale(frames[frame_index], (WIDTH, HEIGHT)), (0, 0))
        # Mettre à jour l'index de la frame
        frame_index = (frame_index + 1) % len(frames)
        # ---------------------------------
        
        
        
        # Rafraîchir l'affichage
        pygame.display.flip()
        clock.tick(10)  # Ajuste la vitesse d'animation (FPS)

    pygame.quit()
    
main_loop()