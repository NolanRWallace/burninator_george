import pygame
import random


heroImg = {
    'walkRight' : [pygame.image.load('hero/hero_right.png'), pygame.image.load('hero/hero_right_walk1.png'), pygame.image.load('hero/hero_right_walk2.png')],
    'walkLeft' : [pygame.image.load('hero/hero_left.png'), pygame.image.load('hero/hero_left_walk1.png'), pygame.image.load('hero/hero_left_walk2.png')],
    'walkUp' : [pygame.image.load('hero/hero_back.png'), pygame.image.load('hero/hero_back_walk1.png'), pygame.image.load('hero/hero_back_walk2.png')],
    'walkDown' : [pygame.image.load('hero/hero_front.png'), pygame.image.load('hero/hero_front_walk1.png'), pygame.image.load('hero/hero_front_walk2.png')],
    'swordRight' : [pygame.image.load('hero/sword_idle_right.png'), pygame.image.load('hero/sword_right_walk1.png'), pygame.image.load('hero/sword_right_walk2.png')],
    'swordLeft' : [pygame.image.load('hero/sword_idle_left.png'), pygame.image.load('hero/sword_left_walk1.png'), pygame.image.load('hero/sword_left_walk2.png')],
    'swordUp' : [pygame.image.load('hero/sword_idle_back.png'), pygame.image.load('hero/sword_back_walk1.png'), pygame.image.load('hero/sword_back_walk2.png')],
    'swordDown' : [pygame.image.load('hero/sword_idle_front.png'), pygame.image.load('hero/sword_front_walk1.png'), pygame.image.load('hero/sword_front_walk2.png')],
    'swordAttackRight' : [pygame.transform.scale(pygame.image.load('hero/sword_right_attack1.png'), (32,32)), pygame.transform.scale(pygame.image.load('hero/sword_right_attack2.png'), (32,32))],
    'swordAttackLeft' : [pygame.transform.scale(pygame.image.load('hero/sword_left_attack1.png'), (32,32)), pygame.transform.scale(pygame.image.load('hero/sword_left_attack2.png'), (32,32))],
    'swordAttackUp' : [pygame.transform.scale(pygame.image.load('hero/sword_back_attack1.png'), (32,32)), pygame.transform.scale(pygame.image.load('hero/sword_back_attack2.png'), (32,32))],
    'swordAttackDown' : [pygame.transform.scale(pygame.image.load('hero/sword_front_attack1.png'), (32,32)), pygame.transform.scale(pygame.image.load('hero/sword_front_attack2.png'), (32,32))],
    'magicAttackRight' : pygame.image.load('hero/magic_right_attack.png'),
    'magicAttackLeft' : pygame.image.load('hero/magic_left_attack.png'),
    'magicAttackUp' : pygame.image.load('hero/magic_back_attack.png'),
    'magicAttackDown' : pygame.image.load('hero/magic_front_attack.png'),
}

dragonImg = {
    'dragonLeft' : [pygame.transform.scale(pygame.image.load('dragon/dragon_left1.png'), (40,40)), pygame.transform.scale(pygame.image.load('dragon/dragon_left2.png'), (40,40)), pygame.transform.scale(pygame.image.load('dragon/dragon_left3.png'), (40,40))],
    'dragonRight' : [pygame.transform.scale(pygame.image.load('dragon/dragon_right1.png'), (40,40)), pygame.transform.scale(pygame.image.load('dragon/dragon_right2.png'), (40,40)), pygame.transform.scale(pygame.image.load('dragon/dragon_right3.png'), (40,40))]
}

georgestanding = {
    'stdup' : pygame.image.load('george/burnstdup.png'),
    'stdright' : pygame.image.load('george/burnstdright.png'),
    'stddown' : pygame.image.load('george/burnstddown.png'),
    'stdleft' : pygame.image.load('george/burnstdleft.png'),
}
georgewalking = {
    'walkup' : [pygame.image.load('george/burnwalkup1.png'), pygame.image.load('george/burnstdup.png'), pygame.image.load('george/burnwalkup2.png')],
    'walkright' : [pygame.image.load('george/burnwalkright1.png'), pygame.image.load('george/burnstdright.png'), pygame.image.load('george/burnwalkright2.png')],
    'walkdown' : [pygame.image.load('george/burnwalkdown1.png'), pygame.image.load('george/burnstddown.png'), pygame.image.load('george/burnwalkdown2.png',)],
    'walkleft' : [pygame.image.load('george/burnwalkleft1.png'), pygame.image.load('george/burnstdleft.png'), pygame.image.load('george/burnwalkleft2.png')],
}

char = pygame.image.load('hero/hero_front.png')


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.standing = True
        self.equip = False
        self.swordAttack = False
        self.swordSlashCount = 0
        self.magicAttack = False
        self.hitbox = (self.x, self.y, 20, 25)
    
    def draw(self, win):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        
        if self.equip == True and self.swordAttack == False:
            if self.left:
                win.blit(heroImg['swordLeft'][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.right:
                win.blit(heroImg['swordRight'][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.up:
                win.blit(heroImg['swordUp'][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.down:
                win.blit(heroImg['swordDown'][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        
        if not(self.standing) and self.equip == False and self.swordAttack == False and self.magicAttack == False:
            if self.left:
                win.blit(heroImg['walkLeft'][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            if self.right:
                win.blit(heroImg['walkRight'][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            if self.up:
                win.blit(heroImg['walkUp'][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            if self.down:
                win.blit(heroImg['walkDown'][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
        if self.standing and self.equip == False and self.swordAttack == False and self.magicAttack == False:
            if self.left:
                win.blit(heroImg['walkLeft'][0], (self.x,self.y))
            elif self.right:
                win.blit(heroImg['walkRight'][0], (self.x,self.y))
            elif self.up:
                win.blit(heroImg['walkUp'][0], (self.x,self.y))
            else: 
                self.down
                win.blit(char, (self.x,self.y))
        
        if self.swordSlashCount + 1 >= 6:
            self.swordSlashCount = 0

        if self.swordAttack == True:
            if self.left:
                win.blit(heroImg['swordAttackLeft'][self.swordSlashCount//3], (self.x, self.y))
                self.swordSlashCount += 1
            elif self.right:
                win.blit(heroImg['swordAttackRight'][self.swordSlashCount//3], (self.x, self.y))
                self.swordSlashCount += 1
            elif self.up:
                win.blit(heroImg['swordAttackUp'][self.swordSlashCount//3], (self.x, self.y))
                self.swordSlashCount += 1
            elif self.down:
                win.blit(heroImg['swordAttackDown'][self.swordSlashCount//3], (self.x, self.y))
                self.swordSlashCount += 1
            
        if self. magicAttack == True and self.swordAttack == False:
            if self.left:
                win.blit(heroImg['magicAttackLeft'], (self.x, self.y))
            if self.right:
                win.blit(heroImg['magicAttackRight'], (self.x, self.y))
            if self.up:
                win.blit(heroImg['magicAttackUp'], (self.x, self.y))
            if self.down:
                win.blit(heroImg['magicAttackDown'], (self.x, self.y))
                
        self.hitbox = (self.x, self.y, 20, 25)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        

# ----end of player class-----

# ---start of burninator george class -----


class Boss(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 12
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x+1, self.y, 37, 47)
    
    def draw(self, win):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(georgewalking['walkleft'][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(georgewalking['walkright'][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.up:
                win.blit(georgewalking['walkup'][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(georgewalking['walkdown'][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(georgestanding['stdleft'], (self.x,self.y))
            elif self.right:
                win.blit(georgestanding['stdright'], (self.x,self.y))
            elif self.up:
                win.blit(georgestanding['stdup'], (self.x,self.y))
            else: 
                self.down
                win.blit(georgestanding['stddown'], (self.x,self.y))
        self.hitbox = (self.x+1, self.y, 37, 47)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
                
# ------end of burninator george class ------
            

class Projectile(object):
    def __init__ (self, x, y, color, radius, direction):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.direction = direction
        self.vel = 8 
    
    def fire(self):
        if self.direction == 'left':
            self.x -= self.vel
        elif self.direction == 'right':
            self.x += self.vel
        elif self.direction == 'down':
            self.y += self.vel
        elif self.direction == 'up':
            self.y -= self.vel
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        # win.blit(fireball,(self.x, self.y))
        

class Tree(object):
    def __init__(self, x, y, width, height, type):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = pygame.transform.scale(pygame.image.load(f'tree/tree{type}.png'), (width,height))
        self.hitbox = self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        self.hitbox = self.hitbox = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)


class BossMinion(object):
    def __init__(self, width, height, end):
        self.x = random.randint(50, 450)
        self.y = random.randint(250, 550)
        self.width = width
        self.height = height
        self.vel = 5
        self.end = end
        self.path = [self.y, self.end]
        self.image = pygame.transform.scale(pygame.image.load('george/stongbad.png'), (width,height))
        self.hitbox = (self.x, self.y, 30, 35)
        


    def draw(self, win):
        self.move()
        win.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y, 30, 35)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
    
    def move(self):
        if self.vel > 0:
            if self.y + self.vel < self.path[1]:
                self.y += self.vel
            else:
                self.vel = self.vel * -1
        else:
            if self.y - self.vel > self.path[0]:
                self.y += self.vel
            else:
                self.vel = self.vel * -1
    
class Castle(object):
    def __init__(self):
        self.x = 185
        self.y = 80
        self.image = pygame.transform.scale(pygame.image.load('castle.gif'), (150,150))
        self.hitbox = (self.x, self.y, 100, 100)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y, 150, 150)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class Dragon(object):
    def __init__(self, end):
        self.x = random.randint(50, 450)
        self.y = random.randint(250, 550)
        self.end = end
        self.walkCount = 0
        self.vel = 5
        self.path = [self.x, self.end]
        self.hitbox = (self.x, self.y, 40, 40)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(dragonImg['dragonRight'][self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(dragonImg['dragonLeft'][self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x, self.y, 40, 40)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.WalkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel *-1
                self.walkCount = 0
        
