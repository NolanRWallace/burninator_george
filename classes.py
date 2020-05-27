import pygame 

walkRight = pygame.image.load('hero_right.png')
walkLeft = pygame.image.load('hero_left.png')
walkUp = pygame.image.load('hero_back.png')
walkDown = pygame.image.load('hero_front.png')
fireball = pygame.image.load('fireball.gif')
# pygame.transform.scale(fireball, (10,10))
# georgewalkup = pygame.image.load('burnwalkup1.png', 'burnstdup.png', 'burnwalkup2.png')

georgestanding = {
    'stdup' : pygame.image.load('burnstdup.png'),
    'stdright' : pygame.image.load('burnstdright.png'),
    'stddown' : pygame.image.load('burnstddown.png'),
    'stdleft' : pygame.image.load('burnstdleft.png'),
}
georgewalking = {
    'walkup' : [pygame.image.load('burnwalkup1.png'), pygame.image.load('burnstdup.png'), pygame.image.load('burnwalkup2.png')],
    'walkright' : [pygame.image.load('burnwalkright1.png'), pygame.image.load('burnstdright.png'), pygame.image.load('burnwalkright2.png')],
    'walkdown' : [pygame.image.load('burnwalkdown1.png'), pygame.image.load('burnstddown.png'), pygame.image.load('burnwalkdown2.png',)],
    'walkleft' : [pygame.image.load('burnwalkleft1.png'), pygame.image.load('burnstdleft.png'), pygame.image.load('burnwalkleft2.png')],
}



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
        self.hitbox = (self.x, self.y, 20, 25)
    
    def draw(self, win):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft, (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight, (self.x,self.y))
                self.walkCount += 1
            elif self.up:
                win.blit(walkUp, (self.x,self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(walkDown, (self.x,self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(walkLeft, (self.x,self.y))
            elif self.right:
                win.blit(walkRight, (self.x,self.y))
            elif self.up:
                win.blit(walkUp, (self.x,self.y))
            else: 
                self.down
                win.blit(walkDown, (self.x,self.y))
                
        self.hitbox = (self.x-2, self.y-2, 24, 28)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        
        def hit():
            pass

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
        
