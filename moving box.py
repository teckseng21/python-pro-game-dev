import pygame
from pygame.locals import *

pygame.init()
screen= pygame.display.set_mode((600,400))

x=300
y=200
speed=0.5

running=True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==QUIT:
            running=False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y-=speed

    if keys[pygame.K_s]:
        y+=speed

    if keys[pygame.K_a]:
        x-=speed                

    if keys[pygame.K_d]:
        x+=speed

    pygame.draw.rect(screen,(255,0,0),(x,y,40,40))
    pygame.display.update()

pygame.quit()