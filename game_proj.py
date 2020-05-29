import pygame, sys
import random
import time
from classes import Player, Boss, Projectile, Tree, BossMinion, Castle, Dragon
from pygame.locals import *


def main():
    
    pygame.init()
    # -----Sounds files imported----
    pygame.mixer.music.set_volume(.25)
    pygame.mixer.music.load('music/trogdor_short.mp3')
    pygame.mixer.music.play(-1)

    fireball_sound = pygame.mixer.Sound('music/Fireball.wav')
    fireball_sound.set_volume(.05)
    gothit = pygame.mixer.Sound('music/gothit.wav')
    gothit.set_volume(.25)
    freezeball_sound = pygame.mixer.Sound('music/freeze.wav')
    freezeball_sound.set_volume(.05)
    freeze_hit = pygame.mixer.Sound('music/ice_break.wav')
    freeze_hit.set_volume(.05)



    win = pygame.display.set_mode((500,600))

    pygame.display.set_caption("Burninator George!!!")
    char = pygame.image.load('hero/hero_front.png')


    # ----Background img loading ------
    bg = pygame.image.load('grassbg.png')
    mountain = pygame.transform.scale(pygame.image.load('bg_bg1.png'), (500,100))

    FRAMERATE = 30
    clock = pygame.time.Clock()
    counter = 0
    not_pressed = True
    # ----start of players class -----
            
        
    # ---game setup----
    randomloc = random.randint(50, 450)
    hero = Player(300, 410, 24, 24)
    boss = Boss(randomloc, randomloc, 30, 30)
    tree_2 = Tree(115, 180, 65, 65, 2)
    tree_1 = Tree(340, 170, 75, 75, 1)
    strongbad = BossMinion(30,35,550)
    castle = Castle()
    dragon = Dragon(450)
    minions = []
    fireballs = []
    boss_fireballs = []
    i=0
    j=0
    win_cond = False
    lose_cond = False
    mana_regen = 0
    direction = 'down'
    boss_direction = 'down'
    fireballCoolDown = 0
    run = True
            


    def redrawGameWindow():
        win.blit(bg, (0,100)) 
        win.blit(mountain, (0,0))
        hero.draw(win)
        if boss.visible == True:
            boss.draw(win)
        tree_2.draw(win)
        tree_1.draw(win)
        strongbad.draw(win)
        castle.draw(win)
        dragon.draw(win)

        for fireball in fireballs:
            fireball.draw(win)
        for boss_fireball in boss_fireballs:
            boss_fireball.draw(win)
        pygame.display.update()
        
        pygame.display.flip()

    def check_for_boss(face_boss, boss_box_perp1, boss_box_perp2):
        if face_boss and boss_box_perp1 and boss_box_perp2 == True:
            return True
        else:
            return False
        
    def check_if_past(boss_past):
        if boss_past == True:
            return True
        else:
            return False

    # start screen
    font = pygame.font.SysFont(None,50)
    font1 = pygame.font.SysFont(None,25)
    font2 = pygame.font.SysFont(None,40)
    #screens
    run = False
    font = pygame.font.SysFont(None,50)
    smallfont = pygame.font.SysFont(None, 35)
    titlefont = pygame.font.SysFont(None, 75)

    def draw_text (text, font, color, surface,x, y):
        textobj = font.render(text,1,color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj,textrect)

    # win_condition
    def victory():
        waiting = True
        
        while waiting:
            win.fill((0,0,0))
            draw_text('Congratulations!', font, (255, 255,255), win, 100, 200)
            draw_text("You beat the Burninator!", smallfont, (255,255,255), win, 100, 250)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            pygame.display.update()
            
            
    # lose_condition
    def game_over():
        click = False
        waiting = True
        
        while waiting:
            win.fill ((0,0,0))
            draw_text('Oops! You died!', titlefont, (255, 255,255), win, 50, 250)
            
            mouse = pygame.mouse.get_pos()
            # print(mouse)
            again_button = pygame.Rect(100, 450, 100, 50)
            quit_button = pygame.Rect (250, 450, 100, 50)
            if again_button.collidepoint(mouse):
                if click:
                    return True
            if quit_button.collidepoint(mouse):
                if click:
                    pygame.quit()
            
            pygame.draw.rect(win, (0,0,255), again_button)
            draw_text('Retry', font, (255,255,255), win, 105, 457)
            
            pygame.draw.rect(win, (255,0,0), quit_button)
            draw_text('Quit', font, (255,255,255), win, 265, 457)
            
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        main()
            
            clock.tick(FRAMERATE)


            

            hero.visible = True
            pygame.display.update()
            clock.tick(FRAMERATE)
            
        
    def main_menu():
        if win_cond == False or lose_cond == False:
            click = False
            intro = True
            
            while intro:
                win.fill ((0,0,0))
                draw_text('The Burninator!!!', font, (255, 255,255), win, 100, 50)
                draw_text('Defeat George the Burninator to win!' ,font2, (255, 255,255), win, 2, 90)

                draw_text('Minions must be killed before ',font2, (255, 255,255), win, 45, 145)
                draw_text('boss can take damage',font2, (255, 255,255), win, 90, 170)
                
                draw_text('arrows keys for movement',font1, (255, 255,255), win, 125, 225)
                draw_text('space bar for iceballs',font1, (255, 255,255), win, 140, 250)
                draw_text('W to dash',font1, (255, 255,255), win, 185, 275)
            
                mouse = pygame.mouse.get_pos()
                # print(mouse)
                start_button = pygame.Rect(100, 450, 100, 50)
                quit_button = pygame.Rect (250, 450, 100, 50)
                if start_button.collidepoint(mouse):
                    if click:
                        return True
                if quit_button.collidepoint(mouse):
                    if click:
                        pygame.quit()
                
                pygame.draw.rect(win, (0,255,0), start_button)
                draw_text('Start', font, (255,255,255), win, 112, 457)
                
                pygame.draw.rect(win, (255,0,0), quit_button)
                draw_text('Quit', font, (255,255,255), win, 265, 457)
                
                click = False
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

                pygame.display.update()
                clock.tick(FRAMERATE)


    main_menu()

    #----game operations loop -----
    # def game():
    #----game operations loop -----
    run = True
    while run:
        counter += 1
        clock.tick(FRAMERATE)
        
        #----y boss hitbox ranges-----
        x_inpath1 = boss.hitbox[1] + boss.hitbox[3] > hero.hitbox[1]
        x_inpath2 = hero.hitbox[1] + hero.hitbox[3] > boss.hitbox[1]
        
        #------x boss hitbox ranges-----
        y_inpath1 = boss.hitbox[0]+boss.hitbox[2] > hero.hitbox[0]
        y_inpath2 = hero.hitbox[2] + hero.hitbox[0] > boss.hitbox[0]
        
        #----direction up collision----
        up = boss.hitbox[1] + boss.hitbox[3] + hero.vel*2 > hero.hitbox[1]
        past_down = hero.hitbox[1] + hero.hitbox[3] < boss.hitbox[1] 
        
        #----direction down collision----
        past_up = boss.hitbox[1] + boss.hitbox[3] < hero.hitbox[1] - hero.vel
        down = hero.hitbox[1] + hero.hitbox[3] + hero.vel*2 > boss.hitbox[1] 
        
        #----direction left collision----
        left = boss.hitbox[0] + boss.hitbox[2] > hero.hitbox[0] -hero.vel
        past_left = hero.hitbox[0] + hero.hitbox[2] -hero.vel < boss.hitbox[0]
        
        #----direction right collision----
        right = hero.hitbox[0] + hero.hitbox[2] + hero.vel > boss.hitbox[0]
        past_right = boss.hitbox[0] + boss.hitbox[2] < hero.hitbox[0] +hero.vel
        
        #-----y tree ranges-------
        x_inpath1_tree_1 = tree_1.hitbox[1] + tree_1.hitbox[3] > hero.hitbox[1]
        x_inpath2_tree_1 = hero.hitbox[1] + hero.hitbox[3] > tree_1.hitbox[1]
        
        #------x tree hitbox ranges-----
        y_inpath1_tree_1 = tree_1.hitbox[0]+tree_1.hitbox[2] > hero.hitbox[0]
        y_inpath2_tree_1 = hero.hitbox[2] + hero.hitbox[0] > tree_1.hitbox[0]
        
        #----direction tree up collision----
        tree_1_up = tree_1.hitbox[1] + tree_1.hitbox[3] + hero.vel*2 > hero.hitbox[1]
        tree_1_past_down = hero.hitbox[1] + hero.hitbox[3] < tree_1.hitbox[1] 
        
        #----direction tree down collision----
        tree_1_past_up = tree_1.hitbox[1] + tree_1.hitbox[3] < hero.hitbox[1] - hero.vel
        tree_1_down = hero.hitbox[1] + hero.hitbox[3] + hero.vel*2 > tree_1.hitbox[1] 
        
        #----direction tree left collision----
        tree_1_left = tree_1.hitbox[0] + tree_1.hitbox[2] > hero.hitbox[0] -hero.vel
        tree_1_past_left = hero.hitbox[0] + hero.hitbox[2] -hero.vel < tree_1.hitbox[0]
        
        #-----y tree ranges-------
        x_inpath1_tree_2 = tree_2.hitbox[1] + tree_2.hitbox[3] > hero.hitbox[1]
        x_inpath2_tree_2 = hero.hitbox[1] + hero.hitbox[3] > tree_2.hitbox[1]
        
        #------x tree hitbox ranges-----
        y_inpath1_tree_2 = tree_2.hitbox[0]+tree_2.hitbox[2] > hero.hitbox[0]
        y_inpath2_tree_2 = hero.hitbox[2] + hero.hitbox[0] > tree_2.hitbox[0]
        
        tree_2_up = tree_2.hitbox[1] + tree_2.hitbox[3] + hero.vel*2 > hero.hitbox[1]
        tree_2_past_down = hero.hitbox[1] + hero.hitbox[3] < tree_2.hitbox[1] 
        
        #----direction tree down collision----
        tree_2_past_up = tree_2.hitbox[1] + tree_2.hitbox[3] < hero.hitbox[1] - hero.vel
        tree_2_down = hero.hitbox[1] + hero.hitbox[3] + hero.vel*2 > tree_2.hitbox[1] 
        
        #----direction tree left collision----
        tree_2_right = hero.hitbox[0] + hero.hitbox[2] + hero.vel > tree_2.hitbox[0]
        tree_2_past_right = tree_2.hitbox[0] + tree_2.hitbox[2] < hero.hitbox[0] +hero.vel


        #-----hero fireball firerate limit -----
        
        if fireballCoolDown > 0:
            fireballCoolDown += 1
        if fireballCoolDown > 5:
            fireballCoolDown = 0
        if hero.mana >= 2:
            hero.no_mana = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        #----hero fireballs -----
        
        for fireball in fireballs:
                if fireball.y + fireball.radius > boss.hitbox[1] and fireball.y - fireball.radius < boss.hitbox[1] + boss.hitbox[3]:
                    if fireball.x + fireball.radius > boss.hitbox[0] and fireball.x - fireball.radius < boss.hitbox[0] + boss.hitbox[2]:
                        fireballs.pop(fireballs.index(fireball))
                        if strongbad.visible == False and dragon.visible == False:
                            boss.hit(fireball.damage)
                            pygame.mixer.Sound.play(freeze_hit)
                            

                if fireball.y + fireball.radius > strongbad.hitbox[1] and fireball.y - fireball.radius < strongbad.hitbox[1] + strongbad.hitbox[3]:
                    if fireball.x + fireball.radius > strongbad.hitbox[0] and fireball.x - fireball.radius < strongbad.hitbox[0] + strongbad.hitbox[2]:
                        strongbad.hit(fireball.damage)
                        pygame.mixer.Sound.play(freeze_hit)
                        fireballs.pop(fireballs.index(fireball))
                if fireball.y + fireball.radius > dragon.hitbox[1] and fireball.y - fireball.radius < dragon.hitbox[1] + dragon.hitbox[3]:
                    if fireball.x + fireball.radius > dragon.hitbox[0] and fireball.x - fireball.radius < dragon.hitbox[0] + dragon.hitbox[2]:
                        dragon.hit(fireball.damage)
                        pygame.mixer.Sound.play(freeze_hit)
                        fireballs.pop(fireballs.index(fireball))

                if fireball.x < 500 and fireball.x > 0 and fireball.y < 600 and fireball.y > 100:
                    fireball.fire()
                else:
                    fireballs.remove(fireball)
                    
        #----boss fireballs------
        
        for boss_fireball in boss_fireballs:
            if boss_fireball.y - boss_fireball.radius > hero.hitbox[1] and boss_fireball.y - boss_fireball.radius < hero.hitbox[1] + hero.hitbox[3]:
                    if boss_fireball.x + boss_fireball.radius > hero.hitbox[0] and boss_fireball.x - boss_fireball.radius < hero.hitbox[0] + hero.hitbox[2]:
                        hero.hit(boss.fireball_dam)
                        if hero.visible == True:
                            pygame.mixer.Sound.play(gothit)
                        boss_fireballs.pop(boss_fireballs.index(boss_fireball))
                        
            if boss_fireball.x < 500 and boss_fireball.x > 0 and boss_fireball.y < 600 and boss_fireball.y > 100:
                boss_fireball.fire()
            else:
                boss_fireballs.remove(boss_fireball)
        
        
        # ---fireball action key----
        

        # if hero.hitbox[1] < boss.hitbox[1] + boss.hitbox[3] and hero.hitbox[1] - 5 + hero.hitbox[3] > boss.hitbox[1]:
        #     if hero.hitbox[0] + hero.hitbox[2] > boss.hitbox[0] and hero.hitbox[0] < boss.hitbox[0] + boss.hitbox[2]:
        #         hero.hit(.5)
        if dragon.visible == True:
            if hero.hitbox[1] < dragon.hitbox[1] + dragon.hitbox[3] and hero.hitbox[1] + hero.hitbox[3] > dragon.hitbox[1]:
                if hero.hitbox[0] + hero.hitbox[2] > dragon.hitbox[0] and hero.hitbox[0] < dragon.hitbox[0] + dragon.hitbox[2]:
                    hero.hit(.5)
                    if hero.visible == True:
                        pygame.mixer.Sound.play(gothit)
        if strongbad.visible == True:
            if hero.hitbox[1] < strongbad.hitbox[1] + strongbad.hitbox[3] and hero.hitbox[1] + hero.hitbox[3] > strongbad.hitbox[1]:
                if hero.hitbox[0] + hero.hitbox[2] > strongbad.hitbox[0] and hero.hitbox[0] < strongbad.hitbox[0] + strongbad.hitbox[2]:
                    hero.hit(.5)
                    if hero.visible == True:
                        pygame.mixer.Sound.play(gothit) 

        keys = pygame.key.get_pressed()
        
        
        #----------- Dash Skill--------------
        if not_pressed:
            if keys[pygame.K_w]:
                if hero.left and hero.x -50 > 0 :
                    hero.x -= 50
                    not_pressed = False
                if hero.right and hero.x + 50 < 500  - hero.width:
                    hero.x += 50
                    not_pressed = False
                if hero.up and hero.y - 50 > 100:
                    hero.y -= 50
                    not_pressed = False
                if hero.down and hero.y + 50 < 600 - hero.height - hero.vel:
                    hero.y += 50
                    not_pressed = False

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
            
            if hero.mana >= 4 and hero.no_mana == False:
                if len(fireballs) < 10 and hero.equip == False:
                    hero.mana -= 4
                    pygame.mixer.Sound.play(freezeball_sound)
                    fireballs.append(Projectile(round(hero.x + hero.width // 2), round(hero.y + hero.height // 2), (52, 232, 235), 5, direction))
                    fireballCoolDown = 1
            else:
                hero.no_mana = True
        
            
        else:
            hero.magicAttack = False
            
        while mana_regen == 20 and hero.mana <= 50:
            hero.mana += 4 
            mana_regen += 1
        if mana_regen > 20:
            mana_regen = 0
        mana_regen += 1
            
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
        
        if keys[pygame.K_LEFT] and hero.x > 0 :
            if boss.visible == True:
                boss_blocked = check_for_boss(left, x_inpath1, x_inpath2)
                boss_pass = check_if_past(past_left)
                # tree1_blocked = check_for_boss(tree_1_left, x_inpath1_tree_1, x_inpath2_tree_1)
                # tree1_pass = check_if_past(tree_1_past_left)
                if boss_blocked == False:
                # if boss_blocked == False and tree1_blocked == False and tree1_pass == False:
                    hero.x -= hero.vel
                    hero.left = True
                    hero.right = False
                    hero.up = False
                    hero.down = False
                    hero.standing = False
                elif boss_pass == True:
                # if boss_pass == True and tree1_blocked == False :
                    hero.x -= hero.vel
                    hero.left = True
                    hero.right = False
                    hero.up = False
                    hero.down = False
                    hero.standing = False
                else:
                    hero.left = True
                    hero.right = False
                    hero.up = False
                    hero.down = False
                    hero.standing = False
            else:
                hero.x -= hero.vel
                hero.left = True
                hero.right = False
                hero.up = False
                hero.down = False
                hero.standing = False
                
        #-----character movement-----


        elif keys[pygame.K_RIGHT] and hero.x < 500  -hero.width:
            if boss.visible == True:
                boss_blocked = check_for_boss(right, x_inpath1, x_inpath2)
                boss_pass = check_if_past(past_right)
                # tree2_blocked = check_for_boss(tree_2_right, x_inpath1_tree_2, x_inpath2_tree_2)
                # tree2_pass = check_if_past(tree_2_past_right)
                if boss_blocked == False:
                # if boss_blocked == False and tree2_blocked == False and tree2_pass == False:
                    hero.x += hero.vel
                    hero.left = False
                    hero.right = True
                    hero.up = False
                    hero.down = False
                    hero.standing = False
                elif boss_pass == True:
                # if boss_pass == True and tree2_blocked == False :
                    hero.x += hero.vel
                    hero.left = False
                    hero.right = True
                    hero.up = False
                    hero.down = False
                    hero.standing = False
                else:
                    hero.left = False
                    hero.right = True
                    hero.up = False
                    hero.down = False
                    hero.standing = False
            else:
                hero.x += hero.vel
                hero.left = False
                hero.right = True
                hero.up = False
                hero.down = False
                hero.standing = False
                
        elif keys[pygame.K_UP] and hero.y > 100:
            if boss.visible == True:
                boss_blocked = check_for_boss(up, y_inpath1, y_inpath2)
                boss_pass = check_if_past(past_down)
                # tree1_blocked = check_for_boss(tree_1_up, y_inpath1_tree_1, y_inpath2_tree_1)
                # tree1_pass = check_if_past(tree_1_past_up)
                # tree2_blocked = check_for_boss(tree_2_up, y_inpath1_tree_2, y_inpath2_tree_2)
                # tree2_pass = check_if_past(tree_2_past_down)
                if boss_blocked == False:
                # elif boss_pass == True and tree1_blocked == False and tree2_blocked == False :
                    hero.y -= hero.vel
                    hero.left = False
                    hero.right = False
                    hero.up = True
                    hero.down = False
                    hero.standing = False
                elif boss_pass == True:
                # elif boss_pass == True and tree1_blocked == False and tree2_blocked == False :
                    hero.y -= hero.vel
                    hero.left = False
                    hero.right = False
                    hero.up = True
                    hero.down = False
                    hero.standing = False
                else:
                    hero.left = False
                    hero.right = False
                    hero.up = True
                    hero.down = False
                    hero.standing = False
            else:
                hero.y -= hero.vel
                hero.left = False
                hero.right = False
                hero.up = True
                hero.down = False
                hero.standing = False


        elif keys[pygame.K_DOWN] and hero.y < 600 - hero.height - hero.vel:
            if boss.visible == True:
                boss_blocked = check_for_boss(down, y_inpath1, y_inpath2)
                boss_pass = check_if_past(past_up)
                # tree1_blocked = check_for_boss(tree_1_down, y_inpath1_tree_1, y_inpath2_tree_1)
                # tree1_pass = check_if_past(tree_1_past_down)
                # tree2_blocked = check_for_boss(tree_2_down, y_inpath1_tree_2, y_inpath2_tree_2)
                # tree2_pass = check_if_past(tree_2_past_up)
                if boss_blocked == False:
                # elif boss_pass == True and tree1_blocked == False and tree2_blocked == False :
                    hero.y += hero.vel
                    hero.left = False
                    hero.right = False
                    hero.up = False
                    hero.down = True
                    hero.standing = False
                # elif boss_pass == True and tree1_blocked == False and tree2_blocked == False :
                elif boss_pass == True:
                    hero.y += hero.vel
                    hero.left = False
                    hero.right = False
                    hero.up = False
                    hero.down = True
                    hero.standing = False
                else:
                    hero.left = False
                    hero.right = False
                    hero.up = False
                    hero.down = True
                    hero.standing = False
            else:
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
            if hero.visible == True:
                #----boss auto walk left if it is the furthest from player------
                    if boss.hitbox[0] - (hero.hitbox[0] + hero.hitbox[2]) >= boss.hitbox[1] - (hero.hitbox[1] + hero.hitbox[3]):
                        if boss.hitbox[0] - (hero.hitbox[0] + hero.hitbox[2]) >= hero.hitbox[1] - (boss.hitbox[1] + boss.hitbox[3]):
                            if boss.hitbox[0]-boss.vel-hero.vel > hero.hitbox[0] + hero.hitbox[2]:
                                boss.x -= boss.vel
                                boss.up = False
                                boss.down = False
                                boss.left = True
                                boss.right = False
                                boss.standing = False
                                
                    if hero.hitbox[0] - (boss.hitbox[0] + boss.hitbox[2]) >= hero.hitbox[1] - (boss.hitbox[1] + boss.hitbox[3]):
                        if hero.hitbox[0] - (boss.hitbox[0] + boss.hitbox[2]) >= boss.hitbox[1] - (hero.hitbox[1] + hero.hitbox[3]):
                            if hero.hitbox[0] > boss.hitbox[0] + boss.hitbox[2] + boss.vel + hero.vel:
                                boss.x += boss.vel
                                boss.up = False
                                boss.down = False
                                boss.left = False
                                boss.right = True
                                boss.standing = False
                                
                    if boss.hitbox[1] - hero.hitbox[1] + hero.hitbox[3] >= hero.hitbox[0] - boss.hitbox[0] +boss.hitbox[2]:
                        if boss.hitbox[1] - hero.hitbox[1] + hero.hitbox[3] >= boss.hitbox[0] - hero.hitbox[0] + hero.hitbox[2]:
                            if boss.hitbox[1] - boss.vel - hero.vel> hero.hitbox[1] + hero.hitbox[3]:
                                boss.y -= boss.vel
                                boss.up = True
                                boss.down = False
                                boss.left = False
                                boss.right = False
                                boss.standing = False
                                
                    if hero.hitbox[1] - boss.hitbox[1] + boss.hitbox[3] >= boss.hitbox[0] - hero.hitbox[0] +hero.hitbox[2]:
                        if hero.hitbox[1] - boss.hitbox[1] + boss.hitbox[3] >= hero.hitbox[0] - boss.hitbox[0] + boss.hitbox[2]:
                            if hero.hitbox[1] > boss.hitbox[1] + boss.hitbox[3] + boss.vel + hero.vel:
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
        if boss.visible == True and hero.visible == True:
            while j == 60:
        
                if boss.left:
                    boss_direction = 'left'
                if boss.right:
                    boss_direction = 'right'
                if boss.up:
                    boss_direction = 'up'
                if boss.down:
                    boss_direction = 'down'
                if len(boss_fireballs) < 100:
                    pygame.mixer.Sound.play(fireball_sound)
                    boss_fireballs.append(Projectile(round(boss.x + boss.width //2), round(boss.y + boss.height //2+10), (255,0,0), 12, boss_direction))
                j += 1
            
        if j > 60:
            j = 0
        j += 1 
    # -----end of boss movement loop-----
        if counter == FRAMERATE *.5:
            counter = 0
            not_pressed = True
        #---rerender screen after game operations---
        
        if boss.visible == False:
            win_cond == True
            # while win_cond == True:
            victory()
        
        if hero.visible == False:
            lose_cond == True
            # while lose_cond == True:
            game_over()
        
        redrawGameWindow()            
    pygame.quit()
main()