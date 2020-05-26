import pygame
import random
from classes import Player, Boss, Projectile
pygame.init()

# -----Sounds files imported----

# pygame.mixer.music.load('trogdor_short.mp3')
# pygame.mixer.music.play(-1)
# fireball_sound = pygame.mixer.Sound('Fireball.wav')
# sword_swing = pygame.mixer.Sound('sword_swing.wav')
# sword_hit = pygame.mixer.Sound('sword_hit.wav')
# pygame.mixer.Sound.play(sword_swing)

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Burninator George!!!")
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
    pygame.display.update()
    
# ---game setup----
randomloc = random.randint(50, 450)
hero = Player(300, 410, 24, 24)
boss = Boss(randomloc, randomloc, 30, 30)
fireballs = []
run = True
i=0
direction = 'down'
#----game operations loop -----
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for fireball in fireballs:
            if fireball.x < 500 and fireball.x > 0 and fireball.y < 500 and fireball.y > 0:
                fireball.fire()
            else:
                fireballs.remove(fireball)
            
        


    keys = pygame.key.get_pressed()
    
    # ---fireball action key----
    
    if keys[pygame.K_SPACE]:
        if hero.left:
            direction = 'left'
        if hero.right:
            direction = 'right'
        if hero.up:
            direction = 'up'
        if hero.down: 
            direction = 'down'
        
        if len(fireballs) < 100:
            fireballs.append(Projectile(round(hero.x + hero.width //2), round(hero.y + hero.height //2), (255,0,0), 5, direction))
    
    #-----character movement-----
    
    if keys[pygame.K_LEFT] and hero.x > hero.vel:
            hero.x -= hero.vel
            hero.left = True
            hero.right = False
            hero.up = False
            hero.down = False
            hero.standing = False
        
    elif keys[pygame.K_RIGHT] and hero.x < 500 - hero.width - hero.vel:
        hero.x += hero.vel
        hero.left = False
        hero.right = True
        hero.up = False
        hero.down = False
        hero.standing = False

        
    elif keys[pygame.K_UP] and hero.y > hero.vel:
        hero.y -= hero.vel
        hero.left = False
        hero.right = False
        hero.up = True
        hero.down = False
        hero.standing = False
    

    elif keys[pygame.K_DOWN] and hero.y < 500 - hero.height - hero.vel:
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
        
    while i == 7:
        if boss.x+11 > hero.x:
            boss.x -= boss.vel
                    
        if boss.x+11 < hero.x:
            boss.x += boss.vel
                        
        if boss.y+11 > hero.y:
            boss.y -= boss.vel
                    
        if boss.y+11 < hero.y:
            boss.y += boss.vel
        i += 1
    if i > 7:
            i = 0
    i += 1
# -----end of boss movement loop-----

    #---rerender screen after game operations---
    redrawGameWindow()

            
pygame.quit()
