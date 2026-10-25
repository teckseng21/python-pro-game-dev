import pygame
import random

pygame.init()

WIDTH=600
HEIGHT=750
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Parkour")
clock=pygame.time.Clock()

BLACK=(7,5,22)
DARK_BLUE=(12,12,40)
CYAN=(0,245,255)
PINK=(255,40,210)
PURPLE=(125,45,255)
WHITE=(240,245,255)
DARK_PURPLE=(35,25,90)

font=pygame.font.SysFont("consolas",24,bold=True)
small_font=pygame.font.SysFont("consolas",17)
big_font=pygame.font.SysFont("consolas",46,bold=True)

PLAYER_WIDTH=22
PLAYER_HEIGHT=28
PLAYER_SPEED=5
GRAVITY=0.42
JUMP_POWER=-12.5

PLATFORM_WIDTH=112
PLATFORM_HEIGHT=14
MIN_GAP=90
MAX_GAP=110

stars=[]
for i in range(90):
    stars.append(
        [random.randint(0, WIDTH),random.randint(0,HEIGHT),random.randint(1,3)]
    )

buildings=[]
building_x=0
while building_x<WIDTH:
    bw=random.randint(38,72)
    bh=random.randint(110,300)
    buildings.append([building_x,HEIGHT-bh,bw,bh])
    building_x+=bw+3

def draw_background(camera_y):
    screen.fill(DARK_BLUE)

    for sx,sy,size in stars:
        star_y=(sy+ int(camera_y *0.12)) %HEIGHT
        pygame.draw.circle(screen,CYAN,(sx,star_y),size)

    for bx,by,bw,bh in buildings:
        screen_y=(by + int(camera_y * 0.22)) %HEIGHT
        pygame.draw.rect(screen, (15,15,48),(bx,screen_y,bw,bh))
        pygame.draw.line(screen, PURPLE, (bx,screen_y), (bx+bw,screen_y), 2)

        for wy in range(screen_y + 14, screen_y + bh -6, 28):
            for wx in range(bx + 7, bx+bw-5,16):
                if (wx+wy)%3!=0:
                    color=CYAN if (wx+wy) % 2 else PINK
                    pygame.draw.rect(screen,color,(wx,wy,4,7))

    for gy in range(0, HEIGHT,60):
        pygame.draw.line(screen,(20,25,75),(0,gy),(WIDTH,gy),1)