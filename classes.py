import pygame 

walkRight = [pygame.image.load('hero/hero_right.png'), pygame.image.load('hero/hero_right_walk1.png'), pygame.image.load('hero/hero_right_walk2.png')]
walkLeft = [pygame.image.load('hero/hero_left.png'), pygame.image.load('hero/hero_left_walk1.png'), pygame.image.load('hero/hero_left_walk2.png')]
walkUp = [pygame.image.load('hero/hero_back.png'), pygame.image.load('hero/hero_back_walk1.png'), pygame.image.load('hero/hero_back_walk2.png')]
walkDown = [pygame.image.load('hero/hero_front.png'), pygame.image.load('hero/hero_front_walk1.png'), pygame.image.load('hero/hero_front_walk2.png')]
swordRight = [pygame.image.load('hero/sword_idle_right.png'), pygame.image.load('hero/sword_right_walk1.png'), pygame.image.load('hero/sword_right_walk2.png')]
swordLeft = [pygame.image.load('hero/sword_idle_left.png'), pygame.image.load('hero/sword_left_walk1.png'), pygame.image.load('hero/sword_left_walk2.png')]
swordUp = [pygame.image.load('hero/sword_idle_back.png'), pygame.image.load('hero/sword_back_walk1.png'), pygame.image.load('hero/sword_back_walk2.png')]
swordDown = [pygame.image.load('hero/sword_idle_front.png'), pygame.image.load('hero/sword_front_walk1.png'), pygame.image.load('hero/sword_front_walk2.png')]
swordAttackRight = [pygame.transform.scale(pygame.image.load('hero/sword_right_attack1.png'), (32,32)), pygame.transform.scale(pygame.image.load('hero/sword_right_attack2.png'), (32,32))]
swordAttackLeft = [pygame.transform.scale(pygame.image.load('hero/sword_left_attack1.png'), (32,32)), pygame.transform.scale(pygame.image.load('hero/sword_left_attack2.png'), (32,32))]
swordAttackUp = [pygame.transform.scale(pygame.image.load('hero/sword_back_attack1.png'), (32,32)), pygame.transform.scale(pygame.image.load('hero/sword_back_attack2.png'), (32,32))]
swordAttackDown = [pygame.transform.scale(pygame.image.load('hero/sword_front_attack1.png'), (32,32)), pygame.transform.scale(pygame.image.load('hero/sword_front_attack2.png'), (32,32))]
magicAttackRight = pygame.image.load('hero/magic_right_attack.png')
magicAttackLeft = pygame.image.load('hero/magic_left_attack.png')
magicAttackUp = pygame.image.load('hero/magic_back_attack.png')
magicAttackDown = pygame.image.load('hero/magic_front_attack.png')

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
        self.hitbox = (self.x-2, self.y, 24, 25)
    
    def draw(self, win):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        
        if self.equip == True and self.swordAttack == False:
            if self.left:
                win.blit(swordLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.right:
                win.blit(swordRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.up:
                win.blit(swordUp[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.down:
                win.blit(swordDown[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        
        if not(self.standing) and self.equip == False and self.swordAttack == False and self.magicAttack == False:
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            if self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            if self.up:
                win.blit(walkUp[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            if self.down:
                win.blit(walkDown[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
        if self.standing and self.equip == False and self.swordAttack == False and self.magicAttack == False:
            if self.left:
                win.blit(walkLeft[0], (self.x,self.y))
            elif self.right:
                win.blit(walkRight[0], (self.x,self.y))
            elif self.up:
                win.blit(walkUp[0], (self.x,self.y))
            else: 
                self.down
                win.blit(char, (self.x,self.y))
        
        if self.swordSlashCount + 1 >= 6:
            self.swordSlashCount = 0

        if self.swordAttack == True:
            if self.left:
                win.blit(swordAttackLeft[self.swordSlashCount//3], (self.x, self.y))
                self.swordSlashCount += 1
            elif self.right:
                win.blit(swordAttackRight[self.swordSlashCount//3], (self.x, self.y))
                self.swordSlashCount += 1
            elif self.up:
                win.blit(swordAttackUp[self.swordSlashCount//3], (self.x, self.y))
                self.swordSlashCount += 1
            elif self.down:
                win.blit(swordAttackDown[self.swordSlashCount//3], (self.x, self.y))
                self.swordSlashCount += 1
            
        if self. magicAttack == True and self.swordAttack == False:
            if self.left:
                win.blit(magicAttackLeft, (self.x, self.y))
            if self.right:
                win.blit(magicAttackRight, (self.x, self.y))
            if self.up:
                win.blit(magicAttackUp, (self.x, self.y))
            if self.down:
                win.blit(magicAttackDown, (self.x, self.y))
                
        def hit(self):
            pass    
        
        self.hitbox = (self.x-2, self.y, 24, 25)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        

# ----end of player class-----

# ---start of burninator george class -----


class Boss(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x+1, self.y, 37, 49)
    
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
        self.hitbox = (self.x+1, self.y, 37, 49)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                
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
        
