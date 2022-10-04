#this is a vidya game built by:
#   - @evanrbuchanan @initialvisuals
#   - @yournamehere

import os, time, sys, random
import pygame as pygame
import pymunk

sys.path.insert(1, 'pymunk')
pygame.init()
gameClock = pygame.time.Clock()

from pygame.locals import * 

os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal

#variables
FPS = 60
WIDTH, HEIGHT, = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vidya")

########## PLAYER ##########


########## Player2 ##########



#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GREY = (100, 100, 100)
PURP = (255, 0, 255)

#load images
icon = pygame.image.load(os.path.join('source\images', 'space.jpg'))
pygame.display.set_icon(icon)
player1Ship = pygame.image.load(os.path.join('source\images', 'ship.png'))
player2Ship = pygame.image.load(os.path.join('source\images', 'enemy.png'))
bg = pygame.image.load(os.path.join('source\images', 'space.jpg'))

#classes
class menuBTN:
    #button style 100px x 50px, orange
    btnW = 100
    btnH = 50
    btnColor = (255, 165, 0)
    btnText = ""
    btnTextSize = 20
    
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.btnW, self.btnH)

class Player1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.Player1W, self.Player1H)
        self.speed = 6
        self.health = 1000
        self.shotVel = 10
        self.width = 50
        self.height = 50
        self.hitbox = (self.x, self.y, self.width, self.height)
        
    
class Player2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.Player2W, self.Player2H)
        self.speed = 6
        self.health = 1000
        self.shotVel = 10
        self.width = 50
        self.height = 50
        self.hitbox = (self.x, self.y, self.width, self.height)

#functions

def get_inputs_Player1(keys,Player1):
    if keys[pygame.K_a] and Player1.x > 0:
        Player1.x -= Player1.speed
    if keys[pygame.K_d] and Player1.x < WIDTH - Player1.Player1W:
        Player1.x += Player1.speed
    if keys[pygame.K_w] and Player1.y > 0:
        Player1.y -= Player1.speed
    if keys[pygame.K_s] and Player1.y < HEIGHT - Player1.Player1H:
        Player1.y += Player1.speed
    if keys[pygame.K_SPACE] and Player1.cooldown == 0:
        print("pwoosh ")
        
def get_inputs_Player2(keys,Player2):
    if keys[pygame.K_LEFT] and Player2.x > 0:
        Player2.x -= Player2.speed
    if keys[pygame.K_RIGHT] and Player2.x < WIDTH - Player2.Player2W:
        Player2.x += Player2.speed
    if keys[pygame.K_UP] and Player2.y > 0:
        Player2.y -= Player2.speed
    if keys[pygame.K_DOWN] and Player2.y < HEIGHT - Player2.Player2H:
        Player2.y += Player2.speed
    if keys[pygame.K_0] and Player2.cooldown == 0:
        print("pew pew")
    
    if keys[pygame.K_ESCAPE]:
        main_menu()
    if keys[pygame.K_SLASH]:
        #full screen toggle
        if pygame.display.get_window_size() == (WIDTH, HEIGHT):
            pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            pygame.display.set_mode((WIDTH, HEIGHT))
        
    

def main_menu():
    #create 3 buttons vertically aligned in the center, with a 10 pixel gap between them. Buttons are Resume, Options, Quit to Desktop
    resumeBTN = menuBTN(WIDTH/2, HEIGHT/2, "Resume")
    optionsBTN = menuBTN(WIDTH/2, HEIGHT/2 + 60, "Options")
    quitBTN = menuBTN(WIDTH/2, HEIGHT/2 + 120, "Quit to Desktop")
    #gotta do these: 
    #create a function for each button that will be called when the button is pressed
    #create a function that will draw the buttons to the screen
    #create a function that will check if the mouse is hovering over a buttons
    #create a function that will check if the mouse is clicking on a button
    #create a function that will check if the mouse is hovering over a button and if it is, change the color of the button to a lighter color



def draw_window(Player1,Player2):
    WIN.fill(BLACK) #fill the screen with black helps with flashes etc
    WIN.blit(bg, (0, 0)) #background
    WIN.blit(player1Ship, (Player1.x, Player1.y))
    WIN.blit(player2Ship, (Player2.x, Player2.y))

    #display fps in top left corner
    pygame.display.set_caption("FPS: " + str(int(gameClock.get_fps())))
    
    
    #update per frame here please leave here
    pygame.display.update()
    


def main():

    run = True
    while run:
        gameClock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main_menu()
        keys = pygame.key.get_pressed()
        get_inputs_Player1(keys,Player1)
        get_inputs_Player2(keys,Player2)
        
        draw_window(Player1,Player2)
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()