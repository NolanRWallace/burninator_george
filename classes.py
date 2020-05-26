import pygame 

walkRight = pygame.image.load('hero_right.png')
walkLeft = pygame.image.load('hero_left.png')
walkUp = pygame.image.load('hero_back.png')
walkDown = pygame.image.load('hero_front.png')
george = pygame.image.load('Burninator.png')

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
        if self.walkCount + 1 >= 27:
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
                
        self.hitbox = (self.x, self.y, 20, 25)
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
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(george, (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(george, (self.x,self.y))
                self.walkCount += 1
            elif self.up:
                win.blit(george, (self.x,self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(george, (self.x,self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(george, (self.x,self.y))
            elif self.right:
                win.blit(george, (self.x,self.y))
            elif self.up:
                win.blit(george, (self.x,self.y))
            else: 
                self.down
                win.blit(george, (self.x,self.y))
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