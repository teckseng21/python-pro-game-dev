import pygame
import random

pygame.init()

screen_width=864
screen_height=700
fps=60

screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Catch the fruits'   )

score=0
game_over=False
game_complete=False
current_level=1

FRUITS=["apple","banana","cherry","orange"]
fruits=[]
BASKET=["basket"]
basket=[]

background=pygame.image.load('images/bg.png')

running = True
while running:
    for event in pygame.event.get():
        screen.blit(background, (0, 0))
    pygame.display.flip() 

def draw():
    global FRUITS,current_level,game_over,game_complete
    fruits=pygame.image.load('images/apple.png')
    fruits=pygame.image.load('images/banana.png')
    fruits=pygame.image.load('images/cherry.png')
    fruits=pygame.image.load('images/orange.png')
    basket=pygame.image.load('images/basket.png')
    for fruits in FRUITS:
        fruits.draw()
    for basket in BASKET:
        basket.draw()
    pygame.display.flip()
    
pygame.display.flip()

pygame.quit()