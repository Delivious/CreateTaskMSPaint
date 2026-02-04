#import the pygame library 
import pygame 
import sys
import random
import time
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

#start the pygame module 
pygame.init() 

#variables for screen size: 
screen_width=690 
screen_height=290


amout = int(input("how many players"))
for a in range(amout):
  newp = input("player "+str(a+1)+" what is your name")
  players.append(newp)
#color code constants 
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
BLUE=(0,0,255)
RED=(255,0,0)
ORANGE=(255,255,0)
PURPLE=(255,0,255)
YELLOW=(0,255,255)

#other variable initializers (fonts, text, images, etc)



def instructions():
  text_load = font.render("loaded", True, (0, 0, 128 ))
#create a screen with dimensions 
screen = pygame.display.set_mode((screen_width, screen_height)) 

#set the screen caption 
pygame.display.set_caption("My First Pygame") 
#fills the screen initially with black
screen.fill(WHITE)

 

#the clock will be used to regulate the frame rate 
clock = pygame.time.Clock() 

#variable to control the game loop 
keep_playing=True 

#Game Loop - needed to keep updating and redrawing the screen 
while keep_playing==True: 
  #iterates over the current list of events(checks for events)  
  for event in pygame.event.get(): 
    #will stop the game loop if escape is pressed (doesn't work in Codio)
    if event.type == pygame.QUIT: 
      keep_playing = False
  #vars in loop
  text = font.render("score: "+str(score), True, (0, 128, 0))

  #add your key press code here


  
  #add your player check here


  #This function call updates the screen
  pygame.display.update()
  screen.fill((0, 0, 0))

  #sets the frame rate
  clock.tick(60)

#quits the pygame module 
pygame.quit() 
quit() 
