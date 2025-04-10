import pygame
import sys


pygame.init()

# The window
resolution = (1200, 900)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Red Rectangle Game")

# The rectangle
rect_width, rect_height = 25, 70
rect_x = (resolution[0] - rect_width) // 2
rect_y = (resolution[1] - rect_height) // 2
rect_color = (255, 0, 0)
rect_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit(0)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
