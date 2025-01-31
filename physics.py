import pygame
import random

pygame.init()

WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))

collicount = 0

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
        collicount += 1
        print(collicount)
        xAbricot = -xAbricot
        yAbricot = -yAbricot
    
    if banane.collidelist([abricot,figue,fraise,mangue,orange,pasteque,poire]) != -1:
        collicount += 1
        print(collicount)
        xBanane = -xBanane
        yBanane = -yBanane
    
    if figue.collidelist([abricot,banane,fraise,mangue,orange,pasteque,poire]) != -1:
        collicount += 1
        print(collicount)
        xFigue = -xFigue
        yFigue = -yFigue

    if fraise.collidelist([abricot,banane,figue,mangue,orange,pasteque,poire]) != -1:
        collicount += 1
        print(collicount)
        xFraise = -xFraise
        yFraise = -yFraise

    if mangue.collidelist([abricot,banane,figue,fraise,orange,pasteque,poire]) != -1:
        collicount += 1
        print(collicount)
        xMangue = -xMangue
        yMangue = -yMangue

    if orange.collidelist([abricot,banane,figue,fraise,mangue,pasteque,poire]) != -1:
        collicount += 1
        print(collicount)
        xOrange = -xOrange
        yOrange = -yOrange

    if pasteque.collidelist([abricot,banane,figue,fraise,mangue,orange,poire]) != -1:
        collicount += 1
        print(collicount)
        xPasteque = -xPasteque
        yPasteque = -yPasteque
        
    if poire.collidelist([abricot,banane,figue,fraise,mangue,orange,pasteque]) != -1:
        collicount += 1
        print(collicount)
        xPoire = -xPoire
        yPoire = -yPoire

    """---------------------------- M O V E M E N T S --------------------------------"""    

    abricot.move_ip(xAbricot,yAbricot)
    banane.move_ip(xBanane,yBanane)
    figue.move_ip(xFigue,yFigue)
    fraise.move_ip(xFraise,yFraise)
    mangue.move_ip(xMangue,yMangue)
    orange.move_ip(xOrange,yOrange)
    pasteque.move_ip(xPasteque,yPasteque)
    poire.move_ip(xPoire,yPoire)

    """----------------- D I S P L A Y I N G   R E C T A N G L E S ------------------"""

    pygame.draw.rect(screen,(255,100,0),abricot,2)
    pygame.draw.rect(screen,(255,255,0),banane,2)
    pygame.draw.rect(screen,(255,0,100),figue,2)
    pygame.draw.rect(screen,(200,0,0),fraise,2)
    pygame.draw.rect(screen,(0,200,100),mangue,2)
    pygame.draw.rect(screen,(0,255,0),orange,2)
    pygame.draw.rect(screen,(0,0,255),pasteque,2)
    pygame.draw.rect(screen,(0,150,250),poire,2)

    """------------------- S P A W N I N G  M A N A G E M E N T ---------------------"""

    if abricot.x > 1330 or abricot.y > 970 or abricot.x < -250 or abricot.y < -250:
        abricot.x = int(random.choice([200,400,600,800]))
        abricot.y = 0
        xAbricot = -xAbricot
        yAbricot = -yAbricot
    if banane.x > 1330 or banane.y > 970 or banane.x < -250 or banane.y < -250:
        banane.x = int(random.choice([300,500,700,900]))
        banane.y = 0
        xBanane = -xBanane
        yBanane = -yBanane
    if figue.x > 1330 or figue.y > 970 or figue.x < -250 or figue.y < -250:
        figue.x = 0
        figue.y = int(random.choice([100,400,600]))
        xFigue = -xFigue
        yFigue = -yFigue
    if fraise.x > 1330 or fraise.y > 970 or fraise.x < -250 or fraise.y < -250:
        fraise.x = 0
        fraise.y = int(random.choice([200,300,500]))
        xFraise = -xFraise
        yFraise = -yFraise
    if mangue.x > 1330 or mangue.y > 970 or mangue.x < -250 or mangue.y < -250:
        mangue.x = int(random.choice([200,400,600,800]))
        mangue.y = 670
        xMangue = -xMangue
        yMangue = -yMangue
    if orange.x > 1330 or orange.y > 970 or orange.x < -250 or orange.y < -250:
        orange.x =  int(random.choice([300,500,700,900]))
        orange.y = 670
        xOrange = -xOrange
        yOrange = -yOrange
    if pasteque.x > 1330 or pasteque.y > 970 or pasteque.x < -250 or pasteque.y < -250:
        pasteque.x = 1030
        pasteque.y = int(random.choice([200,300,500]))
        xPasteque = -xPasteque
        yPasteque = -yPasteque
    if poire.x > 1330 or poire.y > 970 or poire.x < -250 or poire.y < -250:
        poire.x = 1030
        poire.y = int(random.choice([100,400,600]))
        xPoire = -xPoire
        yPoire = -yPoire

    """------------------------- R E L I A B I L I T Y --------------------------------
     E N S U R I N G  T W O  A S S E T S  D O N'T  S T A Y  B L O C K E D  T O G H E T E R
    """

    if collicount > 100:
        abricot.x = int(random.choice([200,400,600,800]))
        abricot.y = 0
        banane.x = int(random.choice([300,500,700,900]))
        banane.y = 0
        figue.x = 0
        figue.y = int(random.choice([100,400,600]))
        fraise.x = 0
        fraise.y = int(random.choice([200,300,500]))
        mangue.x = int(random.choice([200,400,600,800]))
        mangue.y = 670
        orange.x =  int(random.choice([300,500,700,900]))
        orange.y = 670
        pasteque.x = 1030
        pasteque.y = int(random.choice([200,300,500]))
        poire.x = 1030
        poire.y = int(random.choice([100,400,600]))
        collicount = 0

    clock = pygame.time.Clock()
    clock.tick(120)

    pygame.display.update()

pygame.quit()