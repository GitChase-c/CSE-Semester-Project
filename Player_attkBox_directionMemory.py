import pygame
import sys

pygame.init()
resolution = (1200, 900)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Red Rectangle Game")

clock = pygame.time.Clock()

rect_width, rect_height = 25, 70
rect_x = (resolution[0] - rect_width) // 2
rect_y = (resolution[1] - rect_height) // 2
rect_color = (255, 0, 0)
rect_speed = 5

facing_direction = "right"

hitbox = None
hitbox_timer = 0
HITBOX_DURATION = 10
HITBOX_WIDTH = 40
HITBOX_HEIGHT = 70
hitbox_color = (255, 255, 0)
attack_delay = 30
attack_timer = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit(0)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
        facing_direction = "left"
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
        facing_direction = "right"
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    if keys[pygame.K_a] and hitbox_timer == 0 and attack_timer == 0:
        if facing_direction == "right":
            hb_x = rect_x + rect_width
        else:
            hb_x = rect_x - HITBOX_WIDTH
        hb_y = rect_y
        hitbox = pygame.Rect(hb_x, hb_y, HITBOX_WIDTH, HITBOX_HEIGHT)
        hitbox_timer = HITBOX_DURATION
        attack_timer = attack_delay

    if attack_timer > 0:
        attack_timer -= 1

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    if hitbox_timer > 0 and hitbox:
        pygame.draw.rect(screen, hitbox_color, hitbox)
        hitbox_timer -= 1
    else:
        hitbox = None

    pygame.display.flip()
    clock.tick(60)
