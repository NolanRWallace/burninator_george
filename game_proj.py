import pygame
import random
from classes import Player, Boss, Projectile
pygame.init()

# -----Sounds files imported----

# pygame.mixer.music.load('music/trogdor_short.mp3')
# pygame.mixer.music.play(-1)
fireball_sound = pygame.mixer.Sound('music/Fireball.wav')
fireball_sound.set_volume(.05)
sword_swing = pygame.mixer.Sound('music/sword_swing.wav')
sword_hit = pygame.mixer.Sound('music/sword_hit.wav')


win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Burninator George!!!")
char = pygame.image.load('hero/hero_front.png')


# ----Backgroudn img loading ------
bg = pygame.image.load('grassbg.png')


clock = pygame.time.Clock()
# ----start of players class -----
        
def redrawGameWindow():
    win.blit(bg, (0,0)) 
    hero.draw(win)
    boss.draw(win)
    for fireball in fireballs:
        fireball.draw(win)
    for boss_fireball in boss_fireballs:
        boss_fireball.draw(win)
    pygame.display.update()
    
# ---game setup----
randomloc = random.randint(50, 450)
hero = Player(300, 410, 24, 24)
boss = Boss(randomloc, randomloc, 30, 30)
fireballs = []
boss_fireballs = []
run = True
i=0
j=0
direction = 'down'
boss_direction = 'down'
fireballCoolDown = 0

# inpath1 = boss.hitbox[1]+boss.hitbox[3] > hero.hitbox[1] 
# inpath2 = hero.hitbox[1] + hero.hitbox[3] >= boss.hitbox[1]
#     # inpath = True
# # else:
# #     inpath = False
# left = boss.hitbox[0]+boss.hitbox[2] >= hero.hitbox[0]
def check_for_boss(face_boss, boss_box_perp1, boss_box_perp2):
    if face_boss and boss_box_perp1 and boss_box_perp2 == True:
        return True
    else:
        return False
    
def check_if_past(boss_past):
    if boss_past == True:
        return True

#----game operations loop -----

while run:
    clock.tick(30)
    
    #----y boss hitbox ranges-----
    x_inpath1 = boss.hitbox[1] + boss.hitbox[3] > hero.hitbox[1]
    x_inpath2 = hero.hitbox[1] + hero.hitbox[3] > boss.hitbox[1]
    
    #------x boss hitbox ranges-----
    y_inpath1 = boss.hitbox[0]+boss.hitbox[2] > hero.hitbox[0]
    y_inpath2 = hero.hitbox[2] + hero.hitbox[0] > boss.hitbox[0]
    
    #----direction up collision----
    up = boss.hitbox[1] + boss.hitbox[3] + hero.vel > hero.hitbox[1]
    past_down = hero.hitbox[1] + hero.hitbox[3] < boss.hitbox[1]
    
    #----direction down collision----
    past_up = boss.hitbox[1] + boss.hitbox[3] < hero.hitbox[1]
    down = hero.hitbox[1] + hero.hitbox[3] + hero.vel> boss.hitbox[1] 
    
    #----direction left collision----
    left = boss.hitbox[0] + boss.hitbox[2] > hero.hitbox[0] -hero.vel
    past_left = hero.hitbox[0] + hero.hitbox[2] -hero.vel < boss.hitbox[0]
    
    #----direction right collision----
    right = hero.hitbox[0] + hero.hitbox[2] + hero.vel > boss.hitbox[0]
    past_right = boss.hitbox[0] + boss.hitbox[2] < hero.hitbox[0]


    #-----hero fireball firerate limit -----
    
    if fireballCoolDown > 0:
        fireballCoolDown += 1
    if fireballCoolDown > 5:
        fireballCoolDown = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #----hero fireballs -----
    
    for fireball in fireballs:
            if fireball.x < 500 and fireball.x > 0 and fireball.y < 500 and fireball.y > 0:
                fireball.fire()
            else:
                fireballs.remove(fireball)
                
    #----boss fireballs------
    
    for boss_fireball in boss_fireballs:
        if boss_fireball.x < 500 and boss_fireball.x > 0 and boss_fireball.y < 500 and boss_fireball.y > 0:
            boss_fireball.fire()
        else:
            boss_fireballs.remove(boss_fireball)

    keys = pygame.key.get_pressed()
    
    # ---fireball action key----
    
    if keys[pygame.K_SPACE] and fireballCoolDown == 0:
        hero.magicAttack = True
        if hero.left:
            direction = 'left'
        if hero.right:
            direction = 'right'
        if hero.up:
            direction = 'up'
        if hero.down:
            direction = 'down'
        
        if hero.mana > 0:
            hero.mana -= 1
            if len(fireballs) < 5 and hero.equip == False:
                pygame.mixer.Sound.play(fireball_sound)
                fireballs.append(Projectile(round(hero.x + hero.width // 2), round(hero.y + hero.height // 2), (255, 0, 0), 5, direction))
                fireballCoolDown = 1
    else:
        hero.magicAttack = False
        
    #-----weapon switching------
        
    if keys[pygame.K_q]:
        hero.equip = True
    if keys[pygame.K_e]:
        hero.equip = False
    
    if hero.equip == True:
        if keys[pygame.K_SPACE]:
            hero.swordAttack = True
        else:
            hero.swordAttack = False
    
        
    #-----character movement-----
    
    if keys[pygame.K_LEFT] and hero.x > hero.vel - hero.height:
        blocked = check_for_boss(left, x_inpath1, x_inpath2)
        past = check_if_past(past_left)
        if blocked == False:
            hero.x -= hero.vel
            hero.left = True
            hero.right = False
            hero.up = False
            hero.down = False
            hero.standing = False
        elif past == True:
            hero.x -= hero.vel
            hero.left = True
            hero.right = False
            hero.up = False
            hero.down = False
            hero.standing = False

    elif keys[pygame.K_RIGHT] and hero.x < 500  -hero.width :
        blocked = check_for_boss(right, x_inpath1, x_inpath2)
        past = check_if_past(past_right)
        if blocked == False:
            hero.x += hero.vel
            hero.left = False
            hero.right = True
            hero.up = False
            hero.down = False
            hero.standing = False
        elif past == True:
            hero.x += hero.vel
            hero.left = False
            hero.right = True
            hero.up = False
            hero.down = False
            hero.standing = False
        
    elif keys[pygame.K_UP] and hero.y > hero.vel:
        blocked = check_for_boss(up, y_inpath1, y_inpath2)
        past = check_if_past(past_down)
        if blocked == False:
            hero.y -= hero.vel
            hero.left = False
            hero.right = False
            hero.up = True
            hero.down = False
            hero.standing = False
        elif past == True:
            hero.y -= hero.vel
            hero.left = False
            hero.right = False
            hero.up = True
            hero.down = False
            hero.standing = False
    

    elif keys[pygame.K_DOWN] and hero.y < 500 - hero.height - hero.vel:
        blocked = check_for_boss(down, y_inpath1, y_inpath2)
        past = check_if_past(past_up)
        print(blocked)
        print(past)
        if blocked == False:
            hero.y += hero.vel
            hero.left = False
            hero.right = False
            hero.up = False
            hero.down = True
            hero.standing = False
        elif past == True:
            hero.y += hero.vel
            hero.left = False
            hero.right = False
            hero.up = False
            hero.down = True
            hero.standing = False


    else:
        hero.standing = True
        hero.walkCount = 0
        
# ----end of character movements-----

# ----boss automated movement loop -----
        
    while i == 5:
        #----boss auto walk left if it is the furthest from player------
        if boss.hitbox[0] - (hero.hitbox[0] + hero.hitbox[2]) >= boss.hitbox[1] - (hero.hitbox[1] + hero.hitbox[3]):
            if boss.hitbox[0] - (hero.hitbox[0] + hero.hitbox[2]) >= hero.hitbox[1] - (boss.hitbox[1] + boss.hitbox[3]):
                if boss.hitbox[0]-boss.vel > hero.hitbox[0] + hero.hitbox[2]:
                    boss.x -= boss.vel
                    boss.up = False
                    boss.down = False
                    boss.left = True
                    boss.right = False
                    boss.standing = False
                    
        if hero.hitbox[0] - (boss.hitbox[0] + boss.hitbox[2]) >= hero.hitbox[1] - (boss.hitbox[1] + boss.hitbox[3]):
            if hero.hitbox[0] - (boss.hitbox[0] + boss.hitbox[2]) >= boss.hitbox[1] - (hero.hitbox[1] + hero.hitbox[3]):
                if hero.hitbox[0] > boss.hitbox[0] + boss.hitbox[2] + boss.vel:
                    boss.x += boss.vel
                    boss.up = False
                    boss.down = False
                    boss.left = False
                    boss.right = True
                    boss.standing = False
                    
        if boss.hitbox[1] - hero.hitbox[1] + hero.hitbox[3] >= hero.hitbox[0] - boss.hitbox[0] +boss.hitbox[2]:
            if boss.hitbox[1] - hero.hitbox[1] + hero.hitbox[3] >= boss.hitbox[0] - hero.hitbox[0] + hero.hitbox[2]:
                if boss.hitbox[1] - boss.vel > hero.hitbox[1] + hero.hitbox[3]:
                    boss.y -= boss.vel
                    boss.up = True
                    boss.down = False
                    boss.left = False
                    boss.right = False
                    boss.standing = False
                    
        if hero.hitbox[1] - boss.hitbox[1] + boss.hitbox[3] >= boss.hitbox[0] - hero.hitbox[0] +hero.hitbox[2]:
            if hero.hitbox[1] - boss.hitbox[1] + boss.hitbox[3] >= hero.hitbox[0] - boss.hitbox[0] + boss.hitbox[2]:
                if hero.hitbox[1] > boss.hitbox[1] + boss.hitbox[3] + boss.vel:
                    boss.y += boss.vel
                    boss.up = False
                    boss.down = True
                    boss.left = False
                    boss.right = False
                    boss.standing = False
        # else:
        #     boss.standing = True
        #     boss.walkCount = 0

        i += 1
    if i > 5:
        i = 0
    i += 1
        
    while j == 23:
        if boss.left:
            boss_direction = 'left'
        if boss.right:
            boss_direction = 'right'
        if boss.up:
            boss_direction = 'up'
        if boss.down:
            boss_direction = 'down'
        if len(boss_fireballs) < 100:
            # pygame.mixer.Sound.play(fireball_sound)
            boss_fireballs.append(Projectile(round(boss.x + boss.width //2), round(boss.y + boss.height //2), (255,0,0), 10, boss_direction))
        j += 1
        
    if j > 22:
        j = 0
    j += 1
# -----end of boss movement loop-----

    #---rerender screen after game operations---
    redrawGameWindow()

pygame.quit()
