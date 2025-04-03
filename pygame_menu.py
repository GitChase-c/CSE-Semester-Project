import pygame

pygame.init()

display_surface = pygame.display.set_mode((800,800))


def playing():
    pass


def menu():
    onMenu = True
    logo = pygame.image.load('Logo.png')
    background = pygame.image.load('realsky.png')
    transparent = (0,0,0,0)
    display_surface.blit(background, (0,0))
    display_surface.blit(logo, (250,100))
    pygame.display.flip()
    while(onMenu):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                onMenu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    onMenu = False
    display_surface.fill((0,204,255))
    logo.fill(transparent)
    background.fill(transparent)
    display_surface.blit(background, (0,0))
    display_surface.blit(logo, (250,100))
    pygame.display.flip()
                

menu()
running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False