import pygame
import random
pygame.init()


win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Test Run")

walkRight = pygame.image.load('hero_right.png')
walkLeft = pygame.image.load('hero_left.png')
walkUp = pygame.image.load('hero_back.png')
walkDown = pygame.image.load('hero_front.png')
bg = pygame.image.load('grassbg.png')
char = pygame.image.load('hero_front.png')
fireball = pygame.image.load('fireball.gif')
george = pygame.image.load('Burninator.png')

clock = pygame.time.Clock()

class player(object):
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
                
# ---start of burninator george class -----


class Boss(object):
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
                
                
# ------end of burninator george class ------
            
        
class fireball(object):
    def __init__ (self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.vel = 10 * direction
    
    def draw(self, win):
        win.blit(fireball, self.x, self.y)

def redrawGameWindow():
    win.blit(bg, (0,0)) 
    hero.draw(win)
    boss.draw(win)
    pygame.display.update()
randomloc = random.randint(50, 450)
hero = player(300, 410, 24, 24)
boss = Boss(randomloc, randomloc, 30, 30)
fireballs = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for fireball in fireballs:
        if fireball.x < 500 and fireball.x > -1:
            fireball.x += fireball.vel


    keys = pygame.key.get_pressed()
    
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

    redrawGameWindow()

            
pygame.quit()
