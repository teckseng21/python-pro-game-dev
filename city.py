import pygame
import random

pygame.init()

WIDTH=1000
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("City Skiline")

stars=[]
for i in range(150):
    x=random.randint(0, WIDTH)
    y=random.randint(0, HEIGHT // 2)
    size=random.randint(1,3)
    stars.append((x,y,size))

buildings=[]

x=0
while x<WIDTH:
    width=random.randint(50,100)
    height=random.randint(150,450)

    windows=[]

    for wx in range(x+10, x+width-10,18):
        for wy in range(HEIGHT-height+15, HEIGHT-20, 22):
            if random.random()>0.35:
                windows.append((wx,wy))
    buildings.append((x, width, height, windows))
    x+=width

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill((10,10,35))

    pygame.draw.circle(screen, (240,240,240), (850,100), 50)

    for star in stars:
        pygame.draw.circle(screen, (255,255,255), (star[0], star[1]), star[2])

    for building in buildings:
        x, width, height, windows=building
        pygame.draw.rect(screen, (25,25,25), (x, HEIGHT-height, width, height))

        for wx, wy in windows:
            pygame.draw.rect(screen, (255,220,80), (wx, wy, 8, 12))

    pygame.draw.rect(screen, (40,40,40), (0, HEIGHT-50, WIDTH, 50))

    for i in range(0, WIDTH, 60):
        pygame.draw.rect(screen, (255,255,255), (i, HEIGHT-25, 30, 5))

    pygame.display.flip()

pygame.quit()