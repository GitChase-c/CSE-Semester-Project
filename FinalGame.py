import pygame, sys, random, time

pygame.init()
pygame.mixer.init()

width = 1200
height = 900
display_surface = pygame.display.set_mode((width, height))
Clock = pygame.time.Clock()

spawnEnemy = pygame.USEREVENT + 1
pygame.time.set_timer(spawnEnemy, 4000)

def end_display_surface(display_surface, width, height, final_score):
    font = pygame.font.SysFont(None, 48)
    font2 = pygame.font.SysFont(None, 36)
    button_font = pygame.font.SysFont(None, 36)

    button_width = 200
    button_height = 50
    button_y = height - button_height - 200

    button_text = button_font.render("Retry Game", True, (255, 255, 255))
    button_x = (width // 2) - button_width - 10

    button2_text = button_font.render("Exit Game", True, (255, 255, 255))
    button2_x = (width // 2) + 10
    button2_y = button_y

    while True:
        display_surface.fill((0, 0, 0))
        background = pygame.Rect(0, 0, 1200, 900)
        display_surface.blit(BG, background.topleft)
        title_text = font.render("Game Over!", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(width // 2, height // 4))
        display_surface.blit(title_text, title_rect)

        score_text = font2.render(f"Score: {final_score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(width // 2, title_rect.bottom + 30))
        display_surface.blit(score_text, score_rect)

        pygame.draw.rect(display_surface, (250, 0, 0), (button_x, button_y, button_width, button_height))
        button_text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        display_surface.blit(button_text, button_text_rect)

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
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    main()
                if button2_x <= mouse_x <= button2_x + button_width and button2_y <= mouse_y <= button2_y + button_height:
                    print("Closing game.")
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def CreateEnemy(x, y, enemyList):
    enemy = pygame.Rect(0, 0, 50, 100)
    enemy.center = x, y
    enemyList.append(enemy)
    return enemy

def MoveEnemyTowardsHero(hero, enemy):
    enemylevel = checkLvl(enemy)
    herolevel = checkLvl(hero)
    speed = 5
    if hero.y > enemy.y:
        if herolevel == "mid":
            if enemylevel == "top":
                if enemy.x < 600:
                    if enemy.colliderect(topLeft) == True:
                        enemy.center = topMid.center
                    if enemy.x < 300:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 300:
                        enemy.move_ip(-speed, 0)
                elif enemy.x > 600:
                    if enemy.colliderect(topRight) == True:
                        enemy.center = topMid.center
                    if enemy.x < 900:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 900:
                        enemy.move_ip(-speed, 0)
        if herolevel == "lower":
            if enemylevel == "top":
                if enemy.x < 600:
                    if enemy.colliderect(topLeft) == True:
                        enemy.center = topMid.center
                    if enemy.x < 300:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 300:
                        enemy.move_ip(-speed, 0)
                elif enemy.x > 600:
                    if enemy.colliderect(topRight) == True:
                        enemy.center = topMid.center
                    if enemy.x < 900:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 900:
                        enemy.move_ip(-speed, 0)
            elif enemylevel == "mid":
                if enemy.colliderect(topMid) == True:
                    if hero.x > 600:
                        enemy.center = midLeft.center
                    elif hero.x < 600:
                        enemy.center = midRight.center
                if enemy.x > 600:
                    enemy.move_ip(-speed, 0)
                if enemy.x < 600:
                    enemy.move_ip(speed, 0)
        if herolevel == "bottom":
            if enemylevel == "top":
                if enemy.x < 600:
                    if enemy.colliderect(topLeft) == True:
                        enemy.center = topMid.center
                    if enemy.x < 300:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 300:
                        enemy.move_ip(-speed, 0)
                elif enemy.x > 600:
                    if enemy.colliderect(topRight) == True:
                        enemy.center = topMid.center
                    if enemy.x < 900:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 900:
                        enemy.move_ip(-speed, 0)
            elif enemylevel == "mid":
                if enemy.colliderect(topMid) == True:
                    if hero.x > 600:
                        enemy.center = midLeft.center
                    elif hero.x < 600:
                        enemy.center = midRight.center
                if enemy.x > 600:
                    enemy.move_ip(-speed, 0)
                if enemy.x < 600:
                    enemy.move_ip(speed, 0)
            if enemylevel == "lower":
                if enemy.x < 600:
                    if enemy.colliderect(midLeft) == True:
                        enemy.center = bottomPort.center
                    if enemy.x < 300:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 300:
                        enemy.move_ip(-speed, 0)
                elif enemy.x > 600:
                    if enemy.colliderect(midRight) == True:
                        enemy.center = bottomPort.center
                    if enemy.x < 900:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 900:
                        enemy.move_ip(-speed, 0)
        if herolevel == "floor":
            if enemylevel == "top":
                if enemy.x < 600:
                    if enemy.colliderect(topLeft) == True:
                        enemy.center = topMid.center
                    if enemy.x < 300:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 300:
                        enemy.move_ip(-speed, 0)
                elif enemy.x > 600:
                    if enemy.colliderect(topRight) == True:
                        enemy.center = topMid.center
                    if enemy.x < 900:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 900:
                        enemy.move_ip(-speed, 0)
            elif enemylevel == "mid":
                if enemy.colliderect(topMid) == True:
                    if hero.x > 600:
                        enemy.center = midLeft.center
                    elif hero.x < 600:
                        enemy.center = midRight.center
                if enemy.x > 600:
                    enemy.move_ip(-speed, 0)
                if enemy.x < 600:
                    enemy.move_ip(speed, 0)
            elif enemylevel == "lower":
                if enemy.x < 600:
                    if enemy.colliderect(midLeft) == True:
                        enemy.center = midPort.center
                    if enemy.x < 300:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 300:
                        enemy.move_ip(-speed, 0)
                elif enemy.x > 600:
                    if enemy.colliderect(midRight) == True:
                        enemy.center = midPort.center
                    if enemy.x < 900:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 900:
                        enemy.move_ip(-speed, 0)
            elif enemylevel == "bottom":
                if enemy.colliderect(midPort) == True:
                    enemy.center = bottomPort.center
                if enemy.x > 600:
                    enemy.move_ip(-speed, 0)
                if enemy.x < 600:
                    enemy.move_ip(speed, 0)
            
    elif hero.y < enemy.y:
        if herolevel == "bottom":
            if enemylevel == "floor":
                if enemy.colliderect(bottomPort) == True:
                    enemy.center = midPort.center
                    
                if enemy.x > 600:
                    enemy.move_ip(-speed, 0)
                if enemy.x < 600:
                    enemy.move_ip(speed, 0)
        elif herolevel == "lower":
            if enemylevel == "floor":
                if enemy.colliderect(bottomPort) == True:
                    enemy.center = midPort.center
                if enemy.x > 600:
                    enemy.move_ip(-speed, 0)
                if enemy.x < 600:
                    enemy.move_ip(speed, 0)
            elif enemylevel == "bottom":
                if hero.x < 600:
                    if enemy.colliderect(midPort) == True:
                        enemy.center = midLeft.center
                        
                    if enemy.x > 600:
                        enemy.move_ip(-speed, 0)
                    if enemy.x < 600:
                        enemy.move_ip(speed, 0)
                if hero.x > 600:
                    if enemy.colliderect(midPort) == True:
                        enemy.center = midRight.center
                        
                    if enemy.x > 600:
                        enemy.move_ip(-speed, 0)
                    if enemy.x < 600:
                        enemy.move_ip(speed, 0)
        elif herolevel == "mid":
            if enemylevel == "floor":
                if enemy.colliderect(bottomPort) == True:
                    enemy.center = midPort.center
                    
                if enemy.x > 600:
                    enemy.move_ip(-speed, 0)
                if enemy.x < 600:
                    enemy.move_ip(speed, 0)
            elif enemylevel == "bottom":
                    if enemy.colliderect(midPort) == True:
                        enemy.center = midLeft.center
                        
                    if enemy.x > 600:
                        enemy.move_ip(-speed, 0)
                    if enemy.x < 600:
                        enemy.move_ip(speed, 0)
            elif enemylevel == "lower":
                if enemy.colliderect(midRight) == True or enemy.colliderect(midLeft) == True:
                    enemy.center = topMid.center
                    
                if enemy.x < 600:
                    if enemy.x < 300:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 300:
                        enemy.move_ip(-speed, 0)
                if enemy.x > 600:
                    if enemy.x < 900:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 900:
                        enemy.move_ip(-speed, 0)
        elif herolevel == "top":
            if enemylevel == "floor":
                if enemy.colliderect(bottomPort) == True:
                    enemy.center = midPort.center
                    
                if enemy.x > 600:
                    enemy.move_ip(-speed, 0)
                if enemy.x < 600:
                    enemy.move_ip(speed, 0)
            elif enemylevel == "bottom":
                    if enemy.colliderect(midPort) == True:
                        enemy.center = midLeft.center
                        
                    if enemy.x > 600:
                        enemy.move_ip(-speed, 0)
                    if enemy.x < 600:
                        enemy.move_ip(speed, 0)
            elif enemylevel == "lower":
                if enemy.colliderect(midRight) == True or enemy.colliderect(midLeft) == True:
                    enemy.center = topMid.center
                    
                if enemy.x < 600:
                    if enemy.x < 300:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 300:
                        enemy.move_ip(-speed, 0)
                if enemy.x > 600:
                    if enemy.x < 900:
                        enemy.move_ip(speed, 0)
                    elif enemy.x > 900:
                        enemy.move_ip(-speed, 0)
            elif enemylevel == "mid":
                if hero.x < 600:
                    if enemy.colliderect(topMid) == True:
                        enemy.center = topLeft.center
                        
                    if enemy.x > 600:
                        enemy.move_ip(-speed, 0)
                    if enemy.x < 600:
                        enemy.move_ip(speed, 0)
                if hero.x > 600:
                    if enemy.colliderect(topMid) == True:
                        enemy.center = topRight.center
                        
                    if enemy.x > 600:
                        enemy.move_ip(-speed, 0)
                    if enemy.x < 600:
                        enemy.move_ip(speed, 0)                    

    elif hero.x < enemy.x:
        enemy.move_ip(-speed, 0)
    elif hero.x > enemy.x:
        enemy.move_ip(speed, 0)

def CreateHero(imageOrColor, X, Y, width, height):
    hero = pygame.Rect(X, Y, width, height)
    display_surface.blit(HR, hero.topleft)
    return hero

def menu():
    font2 = pygame.font.SysFont(None, 36)
    onMenu = True
    background = pygame.Rect(0, 0, 1200, 900)
    display_surface.blit(BG, background.topleft)
    logo = pygame.Rect(0, 0, 500, 350)
    logo.center = 600, 450
    display_surface.blit(LG, logo.topleft)
    logo.center = 600, 450
    PlayText = font2.render("Press 'A' To Play", True, (255,255,255))
    display_surface.blit(PlayText, background.topleft)
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

def teleportUp(hero, facing_direction):
    jumpsound = pygame.mixer.Sound("Sound/Jump.mp3")
    jumpsound.play()
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
    jumpsound = pygame.mixer.Sound("Sound/Jump.mp3")
    jumpsound.play()
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

def checkLvl(character):
    level = ""
    if character.y > 570:
        level = "floor"
    if character.y > 420 and character.y <= 570:
        level = "bottom"
    elif character.y > 230 and character.y <= 420:
        level = "lower"
    elif character.y > 30 and character.y <= 230:
        level = "mid"
    elif character.y > 0 and character.y <= 30:
        level = "top" 

    return level

def checkKill(hero , enemy, alive):
    if hero.colliderect(enemy) == True:
        alive = False
    
    return alive

def checkHit(hitbox, enemy, enemyList, final_score):
    slash = pygame.mixer.Sound("Sound/Slash.mp3")
    slash.play()
    if hitbox.colliderect(enemy) == True:
        enemyList.remove(enemy)
        final_score += 100
    return final_score

def drawEnemy(enemy):
    display_surface.blit(EM, enemy.topleft)

#top mid purple
topmidPlat = pygame.Rect(0, 0, 425, 40)
topmidPlat.center = 600, 350
#cyan
topleftPlat = pygame.Rect(0, 0, 400, 40)
topleftPlat.bottomleft = 0, 170
#Cyan
toprightPlat = pygame.Rect(0, 0, 400, 40)
toprightPlat.bottomright = 1200, 170

# purp mid lower
midPlat = pygame.Rect(0, 0, 425, 40)
midPlat.center = 600, 690

# white
lowerLeftPlat = pygame.Rect(0, 0, 360, 40)
lowerLeftPlat.topleft = 0, 520

# white
lowerRightPlat = pygame.Rect(0, 0, 360, 40)
lowerRightPlat.topright = 1200, 520

# brown
floorPlat = pygame.Rect(0, 0, 1200, 100)
floorPlat.center = 600, 900

platforms = [topmidPlat, topleftPlat, toprightPlat, midPlat, lowerLeftPlat, lowerRightPlat, floorPlat]

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



BG = pygame.image.load("img/Background.png")
LG = pygame.image.load("img/logo.png")
threesix = pygame.image.load("img/360x40.png")
fourzero = pygame.image.load("img/400x40.png")
fourtwofie = pygame.image.load("img/425x40.png")
PG = pygame.image.load("img/portal.png")
HR = pygame.image.load("img/hero.png")
EM = pygame.image.load("img/enemy.png")
FP = pygame.image.load("img/floorPlat.png")

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
    alive = True
    enemyList = []
    moveDelay = 25
    LastTime = pygame.time.get_ticks()
    final_score = 0
    

    enemy = CreateEnemy(100, 800, enemyList)
    enemy = CreateEnemy(1100, 800, enemyList)
    #800 is floor level
    

    while running:
        display_surface.fill((0, 0, 0))
        background = pygame.Rect(0, 0, 1200, 900)
        display_surface.blit(BG, background.topleft)
        display_surface.blit(FP, floorPlat.topleft)
        display_surface.blit(fourtwofie, topmidPlat.topleft)
        display_surface.blit(fourzero, toprightPlat.topleft)
        display_surface.blit(fourzero, topleftPlat.topleft)
        display_surface.blit(fourtwofie, midPlat.topleft)
        display_surface.blit(threesix, lowerLeftPlat.topleft)
        display_surface.blit(threesix, lowerRightPlat.topleft)
        display_surface.blit(PG, bottomPort.topleft)
        display_surface.blit(PG, midPort.topleft)
        display_surface.blit(PG, midLeft.topleft)
        display_surface.blit(PG, midRight.topleft)
        display_surface.blit(PG, topMid.topleft)
        display_surface.blit(PG, topLeft.topleft)
        display_surface.blit(PG, topRight.topleft)
        
        
        
        hero = CreateHero(hero_color, hero_x, hero_y, rect_width, rect_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                end_display_surface(display_surface, width, height, final_score)
            if event.type == spawnEnemy:
                ranchoice = random.randint(0,3)
                if ranchoice == 0:
                    enemy = CreateEnemy(100, 800, enemyList)
                if ranchoice == 1:
                    enemy = CreateEnemy(1100, 800, enemyList)
                if ranchoice == 2:
                    enemy = CreateEnemy(100, 80, enemyList)
                if ranchoice == 3:
                    enemy = CreateEnemy(1100, 80, enemyList)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    hero = teleportUp(hero, facing_direction)
                    hero_x, hero_y = hero.topleft

                if event.key == pygame.K_DOWN:
                    hero = teleportDown(hero, facing_direction)
                    hero_x, hero_y = hero.topleft
        if alive == True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                hero_x -= hero_speed
                facing_direction = "left"
            if keys[pygame.K_RIGHT]:
                hero_x += hero_speed
                facing_direction = "right"
            keys = pygame.key.get_pressed()
            level = checkLvl(hero)
            if level == "floor":
                if hero_x < 0:
                    hero_x = 0
                elif hero_x > width - rect_width:
                    hero_x = width - rect_width


            elif level == "bottom":
                if hero_x < midPlat.left:
                    hero_x = midPlat.left
                elif hero_x > midPlat.right - rect_width:
                    hero_x = midPlat.right - rect_width

            elif level == "lower":
                if hero_x < lowerLeftPlat.left:
                    hero_x = lowerLeftPlat.left
                elif lowerLeftPlat.right - rect_width < hero_x < lowerRightPlat.left:
                    if (hero_x - (lowerLeftPlat.right - rect_width)
                        < (lowerRightPlat.left - hero_x)):
                        hero_x = lowerLeftPlat.right - rect_width
                    else:
                        hero_x = lowerRightPlat.left
                elif hero_x > lowerRightPlat.right - rect_width:
                    hero_x = lowerRightPlat.right - rect_width

            elif level == "mid":
                if hero_x < topmidPlat.left:
                    hero_x = topmidPlat.left
                elif hero_x > topmidPlat.right - rect_width:
                    hero_x = topmidPlat.right - rect_width

            elif level == "top":
                if hero_x < topleftPlat.left:
                    hero_x = topleftPlat.left
                elif topleftPlat.right - rect_width < hero_x < toprightPlat.left:
                    if (hero_x - (topleftPlat.right - rect_width)
                        < (toprightPlat.left - hero_x)):
                        hero_x = topleftPlat.right - rect_width
                    else:
                        hero_x = toprightPlat.left
                elif hero_x > toprightPlat.right - rect_width:
                    hero_x = toprightPlat.right - rect_width

            if keys[pygame.K_a] and hitbox_timer == 0 and attack_timer == 0:
                if facing_direction == "right":
                    hb_x = hero_x + rect_width
                else:
                    hb_x = hero_x - HITBOX_WIDTH
                hb_y = hero_y
                hitbox = pygame.Rect(hb_x, hb_y, HITBOX_WIDTH, HITBOX_HEIGHT)
                for enemy in enemyList:
                    final_score = checkHit(hitbox, enemy, enemyList, final_score)
                hitbox_timer = HITBOX_DURATION
                attack_timer = attack_delay

            if attack_timer > 0:
                attack_timer -= 1

            
            
            

            
            


            now = pygame.time.get_ticks()
            if now - LastTime >= moveDelay:
                for enemy in enemyList:
                    MoveEnemyTowardsHero(hero, enemy)
                LastTime = now

            
            for enemy in enemyList:
                    drawEnemy(enemy)

            # made the hero rect callable as a function that draws a rect and names it as "hero"
            

            # pygame.draw.rect(display_surface, hero_color, (hero_x, hero_y, rect_width, rect_height))
            
            for enemy in enemyList:
                alive = checkKill(hero , enemy, alive)
            
            


            if hitbox_timer > 0 and hitbox:
                pygame.draw.rect(display_surface, hitbox_color, hitbox)
                hitbox_timer -= 1
            else:
                hitbox = None
        else:
            end_display_surface(display_surface, width, height, final_score)
        pygame.display.flip()
        Clock.tick(60)


menu()
main()
