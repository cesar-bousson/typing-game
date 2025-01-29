import pygame

pygame.init()

WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))

abricot = pygame.Rect(200,700,50,50)
banane = pygame.Rect(800,100,50,50)
figue = pygame.Rect(400,100,50,50)
fraise = pygame.Rect(400,600,50,50)
mangue = pygame.Rect(100,700,50,50)
orange = pygame.Rect(700,100,50,50)
pasteque = pygame.Rect(350,500,50,50)
poire = pygame.Rect(900,150,50,50)

colliders = [abricot,banane,figue,fraise,mangue,orange,pasteque,poire]

xAbricot = 2
yAbricot = -2
xBanane = -2
yBanane = 2

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
               
    if abricot.colliderect(banane):
        print("CONTACT")
        xAbricot = -xAbricot
        yAbricot = -yAbricot
        xBanane = -xBanane
        yBanane = -yBanane

    abricot.move_ip(xAbricot,yAbricot)
    banane.move_ip(xBanane,yBanane)

    pygame.draw.rect(screen,(255,100,0),abricot,2)
    pygame.draw.rect(screen,(255,255,0),banane,2)
    pygame.draw.rect(screen,(205,0,100),figue,2)
    pygame.draw.rect(screen,(200,0,0),fraise,2)
    pygame.draw.rect(screen,(255,200,0),mangue,2)
    pygame.draw.rect(screen,(255,255,0),orange,2)
    pygame.draw.rect(screen,(0,255,0),pasteque,2)
    pygame.draw.rect(screen,(0,255,50),poire,2)

    clock = pygame.time.Clock()
    clock.tick(60)

    pygame.display.update()

pygame.quit()