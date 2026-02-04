import pygame
import threading
import time

def selectColorLoop(run): 
   global num0,num1,num2,num3,num4,num5,num6,num7,num8,num9,comma,customColor,backspace
   while run:
      selectColor(num0,num1,num2,num3,num4,num5,num6,num7,num8,num9,comma)
def selectColor(num0,num1,num2,num3,num4,num5,num6,num7,num8,num9,comma,backs):
    global typedColor, waitTime
    waitTime=0.25
    typedColor=""
    if customColor:
        if num0:
            typedColor+="0"
            time.sleep(0.25)
        if num1:
            typedColor+="1"
            time.sleep(0.25)
        if num2:
            typedColor+="2"
            time.sleep(0.25)
        if num3:
            typedColor+="3"
            time.sleep(0.25)
        if num4:
            typedColor+="4"
            time.sleep(0.25)
        if num5:
            typedColor+="5"
            time.sleep(0.25)
        if num6:
            typedColor+="6"
            time.sleep(0.25)
        if num7:
            typedColor+="7"
            time.sleep(0.25)
        if num8:
            typedColor+="8"
            time.sleep(0.25)
        if num9:
            typedColor+="9"
            time.sleep(0.25)
        if comma:
            typedColor+=","
            time.sleep(0.25)
        if backspace:
            typedColor-=typedColor[-1]

pygame.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
BLUE=(0,0,255)
RED=(255,0,0)
ORANGE=(255,255,0)
PURPLE=(255,0,255)
YELLOW=(0,255,255)
customColorText=pygame.font.render(f"({typedColor})", True, BLACK, background=None)
screen = pygame.display.set_mode((1000,1000))
customColorRect=pygame.rect(100,100,100,100)
keys=pygame.pygame.get_pressed()
numBlock=pygame.rect()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Calculator")
clock = pygame.time.Clock()
run = True
customColor=False
selctColorThread=threading.Thread(target=selectColorLoop, args=(run), daemon=True)
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
