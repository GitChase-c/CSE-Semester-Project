import pygame, sys

pygame.init()

display_surface = pygame.display.set_mode((1200,900))
display_surface.fill((255,255,255))


def menu():
    onMenu = True
    background = pygame.Rect(0,0,1200,900)
    logo = pygame.Rect(0,0,600,450)
    logo.center = 600,450
    pygame.draw.rect(display_surface,(0,0,193), background)
    pygame.draw.rect(display_surface,(0,0,0), logo)
    pygame.display.flip()
    while(onMenu):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                onMenu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    onMenu = False
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
    display_surface.fill((0,0,193))
    pygame.display.flip()

floatPlat1 = pygame.Rect(0,0,550,50)
floatPlat1.center = 600,450

floatPlat2 = pygame.Rect(200,0,200,50)
floatPlat2.bottomleft = 0,300

floatPlat3 = pygame.Rect(200,0,200,50)
floatPlat3.bottomright = 1200,300

Hero = pygame.Rect(0,0,50,110)
Hero.center = 600,700


menu()
running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False




    pygame.draw.rect(display_surface,(0,0,0), floatPlat1)
    pygame.draw.rect(display_surface,(255,0,0), floatPlat2)
    pygame.draw.rect(display_surface,(255,0,0), floatPlat3)
    pygame.draw.rect(display_surface,(255,255,255), Hero)
    pygame.display.flip()

    