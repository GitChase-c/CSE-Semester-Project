import pygame, sys, random

pygame.init()

width = 1200
height = 900
display_surface = pygame.display.set_mode((width, height))
Clock = pygame.time.Clock()
final_score = 0


def end_display_surface(display_surface, width, height, final_score):
    font = pygame.font.SysFont(None, 48)
    font2 = pygame.font.SysFont(None, 36)
    button_font = pygame.font.SysFont(None, 36)

    # shared button props
    button_width = 200
    button_height = 50
    button_y = height - button_height - 200

    # retry button
    button_text = button_font.render("Retry Game", True, (255, 255, 255))
    button_x = (width // 2) - button_width - 10

    # exit button
    button2_text = button_font.render("Exit Game", True, (255, 255, 255))
    button2_x = (width // 2) + 10
    button2_y = button_y

    while True:
        display_surface.fill((0, 0, 0))

        # title
        title_text = font.render("Game Over!", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(width // 2, height // 4))
        display_surface.blit(title_text, title_rect)

        # final score
        score_text = font2.render(f"Score: {final_score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(width // 2, title_rect.bottom + 30))
        display_surface.blit(score_text, score_rect)

        # retry button
        pygame.draw.rect(display_surface, (250, 0, 0), (button_x, button_y, button_width, button_height))
        button_text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        display_surface.blit(button_text, button_text_rect)

        # exit button
        pygame.draw.rect(display_surface, (250, 0, 0), (button2_x, button2_y, button_width, button_height))
        button2_text_rect = button2_text.get_rect(
            center=(button2_x + button_width // 2, button2_y + button_height // 2))
        display_surface.blit(button2_text, button2_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # retry button clicked
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    main()

                # exit button clicked
                if button2_x <= mouse_x <= button2_x + button_width and button2_y <= mouse_y <= button2_y + button_height:
                    print("Closing game.")
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()


def CreateEnemy(x, y):
    enemy = pygame.Rect(0, 0, 50, 110)
    enemy.center = x, y
    enemy_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return enemy, enemy_color


def MoveEnemyTowardsHero(hero, enemy, speed=2):
    if hero.x < enemy.x:
        enemy.move_ip(-speed, 0)
    elif hero.x > enemy.x:
        enemy.move_ip(speed, 0)

    if hero.y < enemy.y:
        enemy.move_ip(0, -speed)
    elif hero.y > enemy.y:
        enemy.move_ip(0, speed)

def CreateHero(imageOrColor, X, Y, width, height):
    hero = pygame.Rect(X, Y, width, height)
    pygame.draw.rect(display_surface, imageOrColor, hero)
    return hero


def menu():
    onMenu = True
    background = pygame.Rect(0, 0, 1200, 900)
    logo = pygame.Rect(0, 0, 500, 350)
    logo.center = 500, 350
    pygame.draw.rect(display_surface, (0, 0, 193), background)
    pygame.draw.rect(display_surface, (0, 0, 0), logo)
    pygame.display.flip()
    while (onMenu):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                onMenu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    onMenu = False
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
    display_surface.fill((0, 0, 193))
    pygame.display.flip()

'''
def teleportUp():

    if hero.colliderect(bottomPort):
        hero.x = midPort.centerx
        hero.y = midPort.centery
    if hero.colliderect(midPort):
        if facing_direction == "right":
            hero.x = midRight.centerx
            hero.y = midRight.centery
        else:
            hero.x = midLeft.centerx
            hero.y = midLeft.centery
    if hero.colliderect(midLeft):
        hero.x = topMid.centerx
        hero.y = topMid.centery
    if hero.colliderect(midRight):
        hero.x = topMid.centerx
        hero.y = topMid.centery
    if hero.colliderect(topMid):
        if facing_direction == "right":
            hero.x = topRight.centerx
            hero.y = topRight.centery
        else:
            hero.x = topLeft.centerx
            hero.y = topLeft.centery




def teleportDown():

    if hero.colliderect(midPort):
        hero.x = bottomPort.centerx
        hero.y = bottomPort.centery
    if hero.colliderect(midLeft):
        hero.x = midPort.centerx
        hero.y = midPort.centery
    if hero.colliderect(midRight):
        hero.x = midPort.centerx
        hero.y = midPort.centery
    if hero.colliderect(topMid):
        if facing_direction == "right":
            hero.x = midRight.centerx
            hero.y = midRight.centery
        else:
            hero.x = midLeft.centerx
            hero.y = midLeft.centery
    if hero.colliderect(topLeft):
        hero.x = topMid.centerx
        hero.y = topMid.centery
    if hero.colliderect(topRight):
        hero.x = topMid.centerx
        hero.y = topMid.centery
'''
def teleportUp(hero, facing_direction):
    if hero.colliderect(bottomPort):
        hero.center = midPort.center
    elif hero.colliderect(midPort):
        if facing_direction == "right":
            hero.center = midRight.center
        else:
            hero.center = midLeft.center
    elif hero.colliderect(midLeft) or hero.colliderect(midRight):
        hero.center = topMid.center
    elif hero.colliderect(topMid):
        if facing_direction == "right":
            hero.center = topRight.center
        else:
            hero.center = topLeft.center
    return hero

def teleportDown(hero, facing_direction):
    if hero.colliderect(midPort):
        hero.center = bottomPort.center
    elif hero.colliderect(midLeft) or hero.colliderect(midRight):
        hero.center = midPort.center
    elif hero.colliderect(topMid):
        if facing_direction == "right":
            hero.center = midRight.center
        else:
            hero.center = midLeft.center
    elif hero.colliderect(topLeft) or hero.colliderect(topRight):
        hero.center = topMid.center
    return hero


enemy1, enemy1_color = CreateEnemy(100, 100)
enemy2, enemy2_color = CreateEnemy(200, 100)
enemy3, enemy3_color = CreateEnemy(300, 100)

floatPlat1 = pygame.Rect(0, 0, 425, 40)
floatPlat1.center = 600, 350

floatPlat2 = pygame.Rect(0, 0, 400, 40)
floatPlat2.bottomleft = 0, 170

floatPlat3 = pygame.Rect(0, 0, 400, 40)
floatPlat3.bottomright = 1200, 170

# purp mid lower
floatStair1 = pygame.Rect(0, 0, 425, 40)
floatStair1.center = 600, 690

# white
floatStair3 = pygame.Rect(0, 0, 360, 40)
floatStair3.topleft = 0, 520

# white
floatStair4 = pygame.Rect(0, 0, 360, 40)
floatStair4.topright = 1200, 520

# brown
floorPlat = pygame.Rect(0, 0, 1200, 100)
floorPlat.center = 600, 900

platforms = [floatPlat1, floatPlat2, floatPlat3, floatStair1, floatStair3, floatStair4, floorPlat]

bottomPort = pygame.Rect(0, 0, 75, 100)
bottomPort.center = 600, 800

midPort = pygame.Rect(0, 0, 75, 100)
midPort.center = 600, 620

midLeft = pygame.Rect(0, 0, 75, 100)
midLeft.center = 300, 470

midRight = pygame.Rect(0, 0, 75, 100)
midRight.center = 900, 470

topMid = pygame.Rect(0, 0, 75, 100)
topMid.center = 600, 280

topLeft = pygame.Rect(0, 0, 75, 100)
topLeft.center = 300, 80

topRight = pygame.Rect(0, 0, 75, 100)
topRight.center = 900, 80


def main():
    rect_width, rect_height = 50, 100
    hero_x = 600
    hero_y = 750
    hero_color = (255, 0, 0)
    hero_speed = 5
    facing_direction = "right"
    hitbox = None
    hitbox_timer = 0
    HITBOX_DURATION = 10
    HITBOX_WIDTH = 50
    HITBOX_HEIGHT = 100
    hitbox_color = (255, 255, 0)
    attack_delay = 30
    attack_timer = 0
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                end_display_surface(display_surface, width, height, final_score)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    hero = teleportUp(hero, facing_direction)
                    hero_x, hero_y = hero.topleft

                if event.key == pygame.K_DOWN:
                    hero = teleportDown(hero, facing_direction)
                    hero_x, hero_y = hero.topleft

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            hero_x -= hero_speed
            facing_direction = "left"
        if keys[pygame.K_RIGHT]:
            hero_x += hero_speed
            facing_direction = "right"


        if keys[pygame.K_a] and hitbox_timer == 0 and attack_timer == 0:
            if facing_direction == "right":
                hb_x = hero_x + rect_width
            else:
                hb_x = hero_x - HITBOX_WIDTH
            hb_y = hero_y
            hitbox = pygame.Rect(hb_x, hb_y, HITBOX_WIDTH, HITBOX_HEIGHT)
            hitbox_timer = HITBOX_DURATION
            attack_timer = attack_delay

        if attack_timer > 0:
            attack_timer -= 1

        display_surface.fill((0, 0, 0))

        pygame.draw.rect(display_surface, enemy1_color, enemy1)
        pygame.draw.rect(display_surface, enemy2_color, enemy2)
        pygame.draw.rect(display_surface, enemy3_color, enemy3)
        pygame.draw.rect(display_surface, (100, 100, 255), floatPlat1)
        pygame.draw.rect(display_surface, (100, 255, 255), floatPlat2)
        pygame.draw.rect(display_surface, (100, 255, 255), floatPlat3)
        pygame.draw.rect(display_surface, (100, 100, 255), floatStair1)
        pygame.draw.rect(display_surface, (255, 255, 255), floatStair3)
        pygame.draw.rect(display_surface, (255, 255, 255), floatStair4)
        pygame.draw.rect(display_surface, (150, 75, 0), floorPlat)
        pygame.draw.rect(display_surface, (155, 155, 255), bottomPort)
        pygame.draw.rect(display_surface, (155, 155, 255), midPort)
        pygame.draw.rect(display_surface, (155, 155, 255), midLeft)
        pygame.draw.rect(display_surface, (155, 155, 255), midRight)
        pygame.draw.rect(display_surface, (155, 155, 255), topMid)
        pygame.draw.rect(display_surface, (155, 155, 255), topLeft)
        pygame.draw.rect(display_surface, (155, 155, 255), topRight)

        # made the hero rect callable as a function that draws a rect and names it as "hero"
        hero = CreateHero(hero_color, hero_x, hero_y, rect_width, rect_height)

        # pygame.draw.rect(display_surface, hero_color, (hero_x, hero_y, rect_width, rect_height))

        if hitbox_timer > 0 and hitbox:
            pygame.draw.rect(display_surface, hitbox_color, hitbox)
            hitbox_timer -= 1
        else:
            hitbox = None

        pygame.display.flip()
        Clock.tick(60)


menu()
main()