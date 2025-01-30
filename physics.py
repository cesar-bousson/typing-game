import pygame
import random

pygame.init()

WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))

"""----------------------- S P A W N I N G  M A N A G E M E N T ----------------------------"""

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

"""------------------- R E C T   I N I T A L I Z A T I O N -------------------------"""

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

"""---------------------------- M O V E M E N T  M A N A G E M E N T --------------------------------"""

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

"""------------------------------------ G A M E  L O O P ------------------------------------------"""


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    xRandom = 0
    yRandom = 0

    screen.fill((0,0,0))
    
    """---------------------------- C O N T A C T  M A N A G E M E N T --------------------------------"""

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
    
    print(xrAbricot)

    """---------------------------- M O V E M E N T S --------------------------------"""


    

    abricot.move_ip(xAbricot,yAbricot)
    banane.move_ip(xBanane,yBanane)
    figue.move_ip(xFigue,yFigue)
    fraise.move_ip(xFraise,yFraise)
    mangue.move_ip(xMangue,yMangue)
    orange.move_ip(xOrange,yOrange)
    pasteque.move_ip(xPasteque,yPasteque)
    poire.move_ip(xPoire,yPoire)

    """---------------------------- D I S P L A Y --------------------------------"""


    pygame.draw.rect(screen,(255,100,0),abricot,2)
    pygame.draw.rect(screen,(255,255,0),banane,2)
    pygame.draw.rect(screen,(255,0,100),figue,2)
    pygame.draw.rect(screen,(200,0,0),fraise,2)
    pygame.draw.rect(screen,(0,200,100),mangue,2)
    pygame.draw.rect(screen,(0,255,0),orange,2)
    pygame.draw.rect(screen,(0,0,255),pasteque,2)
    pygame.draw.rect(screen,(0,150,250),poire,2)
    
    if abricot.x > 1230 or abricot.y > 870 or abricot.x < -150 or abricot.y < -150:
        abricot.x = int(random.choice([200,400,600,800]))
        abricot.y = 0
        xAbricot = -xAbricot
        yAbricot = -yAbricot
    if banane.x > 1230 or banane.y > 870 or banane.x < -150 or banane.y < -150:
        banane.x = int(random.choice([300,500,700,900]))
        banane.y = 0
        xBanane = -xBanane
        yBanane = -yBanane
    if figue.x > 1230 or figue.y > 870 or figue.x < -150 or figue.y < -150:
        figue.x = 0
        figue.y = int(random.choice([100,400,600]))
        xFigue = -xFigue
        yFigue = -yFigue
    if fraise.x > 1230 or fraise.y > 870 or fraise.x < -150 or fraise.y < -150:
        fraise.x = 0
        fraise.y = int(random.choice([200,300,500]))
        xFraise = -xFraise
        yFraise = -yFraise
    if mangue.x > 1230 or mangue.y > 870 or mangue.x < -150 or mangue.y < -150:
        mangue.x = int(random.choice([200,400,600,800]))
        mangue.y = 670
        xMangue = -xMangue
        yMangue = -yMangue
    if orange.x > 1230 or orange.y > 870 or orange.x < -150 or orange.y < -150:
        orange.x =  int(random.choice([300,500,700,900]))
        orange.y = 670
        xOrange = -xOrange
        yOrange = -yOrange
    if pasteque.x > 1230 or pasteque.y > 870 or pasteque.x < -150 or pasteque.y < -150:
        pasteque.x = 1030
        pasteque.y = int(random.choice([200,300,500]))
        xPasteque = -xPasteque
        yPasteque = -yPasteque
    if poire.x > 1230 or poire.y > 870 or poire.x < -150 or poire.y < -150:
        poire.x = 1030
        poire.y = int(random.choice([100,400,600]))
        xPoire = -xPoire
        yPoire = -yPoire
    
    clock = pygame.time.Clock()
    clock.tick(60)

    pygame.display.update()

pygame.quit()