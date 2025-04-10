import pygame, sys, random

pygame.init()


display_surface = pygame.display.set_mode((1200, 900))
Clock = pygame.time.Clock()


def CreateEnemy(x, y):
    enemy = pygame.Rect(0, 0, 50, 110)
    enemy.center = x, y
    enemy_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return enemy, enemy_color


def CreateHero():
    hero = pygame.Rect(0, 0, 50, 110)
    hero.center = 600, 810
    hero_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return hero, hero_color


def MoveEnemyTowardsHero(hero, enemy, speed=2):
    if hero.x < enemy.x:
        enemy.move_ip(-speed, 0)
    elif hero.x > enemy.x:
        enemy.move_ip(speed, 0)

    if hero.y < enemy.y:
        enemy.move_ip(0, -speed)
    elif hero.y > enemy.y:
        enemy.move_ip(0, speed)


enemy1, enemy1_color = CreateEnemy(100, 100)
enemy2, enemy2_color = CreateEnemy(200, 100)
enemy3, enemy3_color = CreateEnemy(300, 100)
hero, hero_color = CreateHero()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    display_surface.fill((255, 255, 255))

    MoveEnemyTowardsHero(hero, enemy1)
    MoveEnemyTowardsHero(hero, enemy2)
    MoveEnemyTowardsHero(hero, enemy3)

    pygame.draw.rect(display_surface, enemy1_color, enemy1)
    pygame.draw.rect(display_surface, enemy2_color, enemy2)
    pygame.draw.rect(display_surface, enemy3_color, enemy3)
    pygame.draw.rect(display_surface, hero_color, hero)

    pygame.display.flip()
    Clock.tick(60)
