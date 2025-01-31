import pygame
import random

pygame.init()

WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))

collicount = 0

"""----------------------- S P A W N I N G  M A N A G E M E N T ----------------------------"""

xrApricot = int(random.choice([200,400,600,800]))
yrApricot = 0
xrBanana = int(random.choice([300,500,700,900]))
yrBanana = 0

xrFig = 0 
yrFig = int(random.choice([100,400,600]))
xrStrawberry = 0
yrStrawberry = int(random.choice([200,300,500]))

xrMango = int(random.choice([200,400,600,800]))
yrMango = 670
xrOrange = int(random.choice([300,500,700,900]))
yrOrange = 670

xrWatermelon = 1030
yrWatermelon = int(random.choice([100,400,600]))
xrPear= 1030
yrPear= int(random.choice([200,300,500]))

"""------------------- R E C T   I N I T A L I Z A T I O N -------------------------"""

apricot = pygame.Rect(xrApricot,yrApricot,100,100)
banana = pygame.Rect(xrBanana,yrBanana,100,100)
fig = pygame.Rect(xrFig,yrFig,100,100)
strawberry = pygame.Rect(xrStrawberry,yrStrawberry,100,100)
mango = pygame.Rect(xrMango,yrMango,100,100)
orange = pygame.Rect(xrOrange,yrOrange,100,100)
watermelon = pygame.Rect(xrWatermelon,yrWatermelon,100,100)
pear= pygame.Rect(xrPear,yrPear,100,100)

imgApricot = pygame.image.load("assets/assets_2/apricot.png")
imgBanana = pygame.image.load("assets/assets_2/banana.png")
imgFig = pygame.image.load("assets/assets_2/fig.png")
imgStrawberry = pygame.image.load("assets/assets_2/strawberry.png")
imgMango = pygame.image.load("assets/assets_2/mango.png")
imgOrange = pygame.image.load("assets/assets_2/orange.png")
imgWatermelon = pygame.image.load("assets/assets_2/watermelon.png")
imgPear = pygame.image.load("assets/assets_2/pear.png")

imgApricot = pygame.transform.scale(imgApricot, (apricot.width, apricot.height))
imgBanana = pygame.transform.scale(imgBanana, (banana.width, banana.height))
imgFig = pygame.transform.scale(imgFig, (fig.width, fig.height))
imgStrawberry = pygame.transform.scale(imgStrawberry, (strawberry.width, strawberry.height))
imgMango = pygame.transform.scale(imgMango, (mango.width, mango.height))
imgOrange = pygame.transform.scale(imgOrange, (orange.width, orange.height))
imgWatermelon = pygame.transform.scale(imgWatermelon, (watermelon.width, watermelon.height))
imgPear = pygame.transform.scale(imgPear, (pear.width, pear.height))


colliders = [apricot,banana,fig,strawberry,mango,orange,watermelon,pear]

xRandom = 0
yRandom = 0

"""---------------------------- M O V E M E N T  M A N A G E M E N T --------------------------------"""

xApricot = -2
yApricot = -2
xBanana = -2
yBanana = 2
xFig = 2
yFig = 0
xStrawberry = 1
yStrawberry = 2
xMango = 2
yMango = 2
xOrange = 2
yOrange = 1
xWatermelon = -2
yWatermelon = 2
xPear= -1
yPear= -1

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

    if apricot.collidelist([banana,fig,strawberry,mango,orange,watermelon,pear]) != -1:
        collicount += 1
        print(collicount)
        xApricot = -xApricot
        yApricot = -yApricot
    
    if banana.collidelist([apricot,fig,strawberry,mango,orange,watermelon,pear]) != -1:
        collicount += 1
        print(collicount)
        xBanana = -xBanana
        yBanana = -yBanana
    
    if fig.collidelist([apricot,banana,strawberry,mango,orange,watermelon,pear]) != -1:
        collicount += 1
        print(collicount)
        xFig = -xFig
        yFig = -yFig

    if strawberry.collidelist([apricot,banana,fig,mango,orange,watermelon,pear]) != -1:
        collicount += 1
        print(collicount)
        xStrawberry = -xStrawberry
        yStrawberry = -yStrawberry

    if mango.collidelist([apricot,banana,fig,strawberry,orange,watermelon,pear]) != -1:
        collicount += 1
        print(collicount)
        xMango = -xMango
        yMango = -yMango

    if orange.collidelist([apricot,banana,fig,strawberry,mango,watermelon,pear]) != -1:
        collicount += 1
        print(collicount)
        xOrange = -xOrange
        yOrange = -yOrange

    if watermelon.collidelist([apricot,banana,fig,strawberry,mango,orange,pear]) != -1:
        collicount += 1
        print(collicount)
        xWatermelon = -xWatermelon
        yWatermelon = -yWatermelon
        
    if pear.collidelist([apricot,banana,fig,strawberry,mango,orange,watermelon]) != -1:
        collicount += 1
        print(collicount)
        xPear= -xPear
        yPear= -yPear
    

    """---------------------------- M O V E M E N T S --------------------------------"""    

    apricot.move_ip(xApricot,yApricot)
    banana.move_ip(xBanana,yBanana)
    fig.move_ip(xFig,yFig)
    strawberry.move_ip(xStrawberry,yStrawberry)
    mango.move_ip(xMango,yMango)
    orange.move_ip(xOrange,yOrange)
    watermelon.move_ip(xWatermelon,yWatermelon)
    pear.move_ip(xPear,yPear)

    """------------ ---- D I S P L A Y I N G   R E C T A N G L E S ------------------"""
    
    screen.blit(imgApricot, apricot.topleft)
    screen.blit(imgBanana, banana.topleft)
    screen.blit(imgFig, fig.topleft)
    screen.blit(imgStrawberry, strawberry.topleft)
    screen.blit(imgMango, mango.topleft)
    screen.blit(imgOrange, orange.topleft)
    screen.blit(imgWatermelon, watermelon.topleft)
    screen.blit(imgPear, pear.topleft)


    """
    pygame.draw.rect(screen,(255,100,0),apricot,2)
    pygame.draw.rect(screen,(255,255,0),banana,2)
    pygame.draw.rect(screen,(255,0,100),fig,2)
    pygame.draw.rect(screen,(200,0,0),Strawberry,2)
    pygame.draw.rect(screen,(0,200,100),mango,2)
    pygame.draw.rect(screen,(0,255,0),orange,2)
    pygame.draw.rect(screen,(0,0,255),Watermelon,2)
    pygame.draw.rect(screen,(0,150,250),pear,2)
    """
    
    # banana = pygame.image.load("Assets/banana.png")
    # fig = pygame.image.load("Assets/fig.png")
    # strawberry = pygame.image.load("Assets/mango.png")
    # mango = pygame.image.load("Assets/orange.png")
    # orange = pygame.image.load("Assets/pear.png")
    # watermelon = pygame.image.load("Assets/strawberry.png")
    # pear = pygame.image.load("Assets/watermelon.png")
    
    
    
    """------------------- S P A W N I N G  M A N A G E M E N T ---------------------"""

    if apricot.x > 1330 or apricot.y > 970 or apricot.x < -250 or apricot.y < -250:
        apricot.x = int(random.choice([200,400,600,800]))
        apricot.y = 0
        xApricot = -xApricot
        yApricot = -yApricot
    if banana.x > 1330 or banana.y > 970 or banana.x < -250 or banana.y < -250:
        banana.x = int(random.choice([300,500,700,900]))
        banana.y = 0
        xBanana = -xBanana
        yBanana = -yBanana
    if fig.x > 1330 or fig.y > 970 or fig.x < -250 or fig.y < -250:
        fig.x = 0
        fig.y = int(random.choice([100,400,600]))
        xFig = -xFig
        yFig = -yFig
    if strawberry.x > 1330 or strawberry.y > 970 or strawberry.x < -250 or strawberry.y < -250:
        strawberry.x = 0
        strawberry.y = int(random.choice([200,300,500]))
        xStrawberry = -xStrawberry
        yStrawberry = -yStrawberry
    if mango.x > 1330 or mango.y > 970 or mango.x < -250 or mango.y < -250:
        mango.x = int(random.choice([200,400,600,800]))
        mango.y = 670
        xMango = -xMango
        yMango = -yMango
    if orange.x > 1330 or orange.y > 970 or orange.x < -250 or orange.y < -250:
        orange.x =  int(random.choice([300,500,700,900]))
        orange.y = 670
        xOrange = -xOrange
        yOrange = -yOrange
    if watermelon.x > 1330 or watermelon.y > 970 or watermelon.x < -250 or watermelon.y < -250:
        watermelon.x = 1030
        watermelon.y = int(random.choice([200,300,500]))
        xWatermelon = -xWatermelon
        yWatermelon = -yWatermelon
    if pear.x > 1330 or pear.y > 970 or pear.x < -250 or pear.y < -250:
        pear.x = 1030
        pear.y = int(random.choice([100,400,600]))
        xPear= -xPear
        yPear= -yPear

    """------------------------- R E L I A B I L I T Y --------------------------------
     E N S U R I N G  T W O  A S S E T S  D O N'T  S T A Y  B L O C K E D  T O G H E T E R
    """

    if collicount > 100:
        apricot.x = int(random.choice([200,400,600,800]))
        apricot.y = 0
        banana.x = int(random.choice([300,500,700,900]))
        banana.y = 0
        fig.x = 0
        fig.y = int(random.choice([100,400,600]))
        strawberry.x = 0
        strawberry.y = int(random.choice([200,300,500]))
        mango.x = int(random.choice([200,400,600,800]))
        mango.y = 670
        orange.x =  int(random.choice([300,500,700,900]))
        orange.y = 670
        watermelon.x = 1030
        watermelon.y = int(random.choice([200,300,500]))
        pear.x = 1030
        pear.y = int(random.choice([100,400,600]))
        collicount = 0

    clock = pygame.time.Clock()
    clock.tick(500)

    pygame.display.update()

pygame.quit()