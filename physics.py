import pygame
import random

pygame.init()

WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
"""
xrAbricot = int(random.choice([90,240,480,640,800,990]))
yrAbricot = 0
xrBanane = int(random.choice([180,360,540,720,900,1080]))
yrBanane = 0

xrFigue = 0 
yrFigue = int(random.choice([90,180,480,640]))
xrFraise = 0
yrFraise = int(random.choice([180,360,540,720]))

xrMangue = int(random.choice([90,240,480,640,800,990]))
yrMangue = 720
xrOrange = int(random.choice([180,360,540,720,900,1080]))
yrOrange = 720

xrPasteque = 1080
yrPasteque = int(random.choice([90,180,480,640]))
xrPoire = 1080
yrPoire = int(random.choice([180,360,540,720]))

abricot = pygame.Rect(xrAbricot,yrAbricot,50,50)
banane = pygame.Rect(xrBanane,yrBanane,50,50)
figue = pygame.Rect(xrFigue,yrFigue,50,50)
fraise = pygame.Rect(xrFraise,yrFraise,50,50)
mangue = pygame.Rect(xrMangue,yrMangue,50,50)
orange = pygame.Rect(xrOrange,yrOrange,50,50)
pasteque = pygame.Rect(xrPasteque,yrPasteque,50,50)
poire = pygame.Rect(xrPoire,yrPoire,50,50)
"""

"""
xRandTOP = int(random.choice([0,180,360,540,720,900,1080]))
yRandTOP = 0
xRandDOWN = int(random.choice([0,180,360,540,720,900,1080]))
yRandDOWN = 720
xRandLEFT = 0
yRandLEFT = int(random.choice([0,180,360,540,720]))
xRandRIGHT = 1080
yRandRIGHT = int(random.choice([0,180,360,540,720]))

abricot = pygame.Rect(xRandTOP,yRandTOP,50,50)
banane = pygame.Rect(xRandTOP,yRandTOP,50,50)
figue = pygame.Rect(xRandLEFT,yRandLEFT,50,50)
fraise = pygame.Rect(xRandLEFT,yRandLEFT,50,50)
mangue = pygame.Rect(xRandDOWN,yRandDOWN,50,50)
orange = pygame.Rect(xRandDOWN,yRandDOWN,50,50)
pasteque = pygame.Rect(xRandRIGHT,yRandRIGHT,50,50)
poire = pygame.Rect(xRandRIGHT,yRandRIGHT,50,50)

colliders = [abricot,banane,figue,fraise,mangue,orange,pasteque,poire]

xRandom = 0
yRandom = 0
"""
xAbricot = -2
yAbricot = -2
xBanane = -2
yBanane = 2
xFigue = 2
yFigue = 0
xFraise = 1
yFraise = 2
xMangue = 2
yMangue = 2
xOrange = 2
yOrange = 1
xPasteque = -2
yPasteque = 2
xPoire = -1
yPoire = -1


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    xrAbricot = int(random.choice([200,400,600,800]))
    yrAbricot = 0
    xrBanane = int(random.choice([300,500,700,900]))
    yrBanane = 0

    xrFigue = 0 
    yrFigue = int(random.choice([100,400,600]))
    xrFraise = 0
    yrFraise = int(random.choice([200,300,500]))

    xrMangue = int(random.choice([200,400,600,800]))
    yrMangue = 670
    xrOrange = int(random.choice([300,500,700,900]))
    yrOrange = 670

    xrPasteque = 1030
    yrPasteque = int(random.choice([100,400,600]))
    xrPoire = 1030
    yrPoire = int(random.choice([200,300,500]))

    abricot = pygame.Rect(xrAbricot,yrAbricot,50,50)
    banane = pygame.Rect(xrBanane,yrBanane,50,50)
    figue = pygame.Rect(xrFigue,yrFigue,50,50)
    fraise = pygame.Rect(xrFraise,yrFraise,50,50)
    mangue = pygame.Rect(xrMangue,yrMangue,50,50)
    orange = pygame.Rect(xrOrange,yrOrange,50,50)
    pasteque = pygame.Rect(xrPasteque,yrPasteque,50,50)
    poire = pygame.Rect(xrPoire,yrPoire,50,50)


    colliders = [abricot,banane,figue,fraise,mangue,orange,pasteque,poire]

    xRandom = 0
    yRandom = 0
    """
    xAbricot = -2
    yAbricot = -2
    xBanane = -2
    yBanane = 2
    xFigue = 2
    yFigue = 0
    xFraise = 1
    yFraise = 2
    xMangue = 2
    yMangue = 2
    xOrange = 2
    yOrange = 1
    xPasteque = -2
    yPasteque = 2
    xPoire = -1
    yPoire = -1
    """
    screen.fill((0,0,0))
               
    if abricot.collidelist([banane,figue,fraise,mangue,orange,pasteque,poire]) != -1:
        print("CONTACT TOP")
        xAbricot = -xAbricot
        yAbricot = -yAbricot
    
    if banane.collidelist([abricot,figue,fraise,mangue,orange,pasteque,poire]) != -1:
        print("CONTACT TOP")
        xBanane = -xBanane
        yBanane = -yBanane
    
    if figue.collidelist([abricot,banane,fraise,mangue,orange,pasteque,poire]) != -1:
        print("CONTACT LEFT")
        xFigue = -xFigue
        yFigue = -yFigue

    if fraise.collidelist([abricot,banane,figue,mangue,orange,pasteque,poire]) != -1:
        print("CONTACT LEFT")
        xFraise = -xFraise
        yFraise = -yFraise

    if mangue.collidelist([abricot,banane,figue,fraise,orange,pasteque,poire]) != -1:
        print("CONTACT DOWN")
        xMangue = -xMangue
        yMangue = -yMangue

    if orange.collidelist([abricot,banane,figue,fraise,mangue,pasteque,poire]) != -1:
        print("CONTACT DOWN")
        xOrange = -xOrange
        yOrange = -yOrange

    if pasteque.collidelist([abricot,banane,figue,fraise,mangue,orange,poire]) != -1:
        print("CONTACT RIGHT")
        xPasteque = -xPasteque
        yPasteque = -yPasteque
        
    if poire.collidelist([abricot,banane,figue,fraise,mangue,orange,pasteque]) != -1:
        print("CONTACT RIGHT")
        xPoire = -xPoire
        yPoire = -yPoire
    
    abricot.move_ip(xAbricot,yAbricot)
    banane.move_ip(xBanane,yBanane)
    figue.move_ip(xFigue,yFigue)
    fraise.move_ip(xFraise,yFraise)
    mangue.move_ip(xMangue,yMangue)
    orange.move_ip(xOrange,yOrange)
    pasteque.move_ip(xPasteque,yPasteque)
    poire.move_ip(xPoire,yPoire)

    pygame.draw.rect(screen,(255,100,0),abricot,2)
    pygame.draw.rect(screen,(255,255,0),banane,2)
    pygame.draw.rect(screen,(255,0,100),figue,2)
    pygame.draw.rect(screen,(200,0,0),fraise,2)
    pygame.draw.rect(screen,(0,200,100),mangue,2)
    pygame.draw.rect(screen,(0,255,0),orange,2)
    pygame.draw.rect(screen,(0,0,255),pasteque,2)
    pygame.draw.rect(screen,(0,150,250),poire,2)

    clock = pygame.time.Clock()
    clock.tick(30)

    pygame.display.update()

pygame.quit()