#import the pygame library 
import pygame 
import sys
import random
import time
import os
import threading
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

#start the pygame module 

pygame.init() 

#variables for screen size: 
screen_width=1380
screen_height=580


#color code constants 
def selectColorLoop(run): 
   """loop for selectColor()"""
   global num0,num1,num2,num3,num4,num5,num6,num7,num8,num9,comma,customColor,backspace
   while run:
      selectColor(num0,num1,num2,num3,num4,num5,num6,num7,num8,num9,comma)
def selectColor(num0,num1,num2,num3,num4,num5,num6,num7,num8,num9,comma,backs):
    """for selecting a color with a custom color so you can type in a color rgb value for the custom color"""
    global typedColor
    currTime=time.time()
    typedColor=""
    if currTime - lastPrint > 100:
        if customColor:
            if num0:
                typedColor+="0"
                lastPrint=currTime
            if num1:
                typedColor+="1"
                lastPrint=currTime
            if num2:
                typedColor+="2"
                lastPrint=currTime
            if num3:
                typedColor+="3"
                lastPrint=currTime
            if num4:
                typedColor+="4"
                lastPrint=currTime
            if num5:
                typedColor+="5"
                lastPrint=currTime
            if num6:
                typedColor+="6"
                lastPrint=currTime
            if num7:
                typedColor+="7"
                lastPrint=currTime
            if num8:
                typedColor+="8"
                lastPrint=currTime
            if num9:
                typedColor+="9"
                lastPrint=currTime
            if comma:
                typedColor+=","
                lastPrint=currTime
            if backspace:
                typedColor-=typedColor[-1]
                lastPrint=currTime
def menuScreen():
    """where to draw the menu"""
    global run
    while run:
        window.fill((120, 120, 120))
        screen.blit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return run
        pygame.display.update()
        clock.tick(60)
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
BLUE=(0,0,255)
RED=(255,0,0)
ORANGE=(255,255,0)
PURPLE=(255,0,255)
YELLOW=(0,255,255)
colorList=[BLACK, WHITE, GREEN, BLUE, RED, ORANGE, PURPLE, YELLOW]
font = pygame.font.SysFont("comicsansms", 72)
customColorText=font.render(f"({typedColor})", True, BLACK)
screen = pygame.display.set_mode((1000,1000))
customColorRect=pygame.rect(100,100,100,100)
keys=pygame.pygame.get_pressed()
numBlock=pygame.rect()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Calculator")
clock = pygame.time.Clock()
menuScreen()
run = True
customColor=False
selctColorThread=threading.Thread(target=selectColorLoop, args=(run), daemon=True)
selctColorThread.start()
while run:
    window.fill((120, 120, 120))
    screen.blit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(60)
    num0=keys[pygame.K_0]
    num1=keys[pygame.K_1]
    num2=keys[pygame.K_2]
    num3=keys[pygame.K_3]
    num4=keys[pygame.K_4]
    num5=keys[pygame.K_5]
    num6=keys[pygame.K_6]
    num7=keys[pygame.K_7]
    num8=keys[pygame.K_8]
    num9=keys[pygame.K_9]
    comma=keys[pygame.K_COMMA]
    backspace=keys[pygame.K_BACKSPACE]
    if keys[pygame.K_LCTRL] and keys[pygame.K_c]:
        customColor=not customColor
pygame.quit()


#other variable initializers (fonts, text, images, etc)



