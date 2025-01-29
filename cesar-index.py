import pygame
import time
import random

pygame.init()

#pseudocode: 

#faire un jeu qui decoupe des fruit : 
#- des fruits son [affiché] en mouvement (apparraissent et disparraissent)
#- un fruit peut etre [coupé] lorsqu'on [appui sur clavier] sur sa [lettre] correspondante : definir lettre pour fruit

#define the screen:

pygame.display.set_caption("FRUITIX SLICER")
background = pygame.image.load("assets/pictures/bg/bg_1.png")
background_width, background_height = background.get_size()
screen = pygame.display.set_mode((background_height, background_width))

class Fruit:
    
    def __init__(self, type, value,):
        # slice_fruit()
        self.type = type
        self.value = value 
        
fruit_1 = Fruit("orange",2)
fruit_2 = Fruit("watermelon",1)
fruit_3 = Fruit("mango",4)
fruit_4 = Fruit("peach",2)
fruit_5 = Fruit("banana",1)
fruit_6 = Fruit("bomb",-4)
fruit_7 = Fruit("ice",0)

def display_fruits():
    fruit_pictures = {
        pygame.image.load(""),
        pygame.image.load(""),
        pygame.image.load(""),
        pygame.image.load(""),
        pygame.image.load(""),
        pygame.image.load(""),
        pygame.image.load(""),
}
    
# def display_bomb():
    

#     def slice_fruit():

# print(fruit_1.value)

# def keyboard():
    
# def slice_fruit():
#     while True:
#         if 
        

#main_loop:
running = True

def main_loop():
    
    screen.blit(background(background_width, background_height))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
    
    pygame.display.flip()        

pygame.quit()