import pygame
import threading
def selectColorLoop(run):
   global num0,num1,num2,num3,num4,num5,num6,num7,num8,num9,comma,customColor
   while run:
      selectColor(num0,num1,num2,num3,num4,num5,num6,num7,num8,num9,comma)
def selectColor(num0,num1,num2,num3,num4,num5,num6,num7,num8,num9,comma):
    acceptedInputs=["0","1","2","3","4","5","6","7","8","9",","]
pygame.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
BLUE=(0,0,255)
RED=(255,0,0)
ORANGE=(255,255,0)
PURPLE=(255,0,255)
YELLOW=(0,255,255)
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
    if keys[pygame.K_LCTRL] and keys[pygame.K_c]:
        customColor=not customColor
pygame.quit()
