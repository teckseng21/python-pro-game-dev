import pygame
import random

pygame.init()

WIDTH=1000
HEIGHT=650

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Neon wireframe city")

clock=pygame.time.Clock()

BUILDING=(18,18,30)
CYAN=(0,255,255)
PINK=(255,0,200)
BLUE=(0,170,255)
WHITE=(255,255,255)

stars=[]

for i in range(180):
    stars.append([
        random.randint(0,WIDTH),
        random.randint(0,HEIGHT//2),
        random.randint(1,3),
        random.uniform(0.2,0.8)
    ])

background=[]
foreground=[]

x=0
while x<WIDTH:
    w=random.randint(60,110)
    h=random.randint(140,250)
    background.append((x,w,h))
    x+=w+random.randint(5,20)

x=0
while x<WIDTH:
    w=random.randint(70,120)
    h=random.randint(230,430)
    foreground.append((x,w,h))
    x+=w+random.randint(5,15)

window_state=[]
for bx, bw, bh in foreground:
    top=HEIGHT-bh
    building=[]
    wx=bx+8
    while wx<bx+bw-10:
        wy=top+10

        while wy<HEIGHT-20:
            building.append([wx,wy, random.choice([True,False])])
            wy+=20

        wx+=16
    window_state.append(building)

window_timer=0
running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    for y in range(HEIGHT):
        pygame.draw.line(screen,(5+y//20,0,25+y//8), (0,y), (WIDTH,y))
    for s in stars:
        pygame.draw.circle(screen, WHITE, (int(s[0]), int(s[1])), int(s[2]))

        s[0]+=s[3]
        if s[0]>WIDTH:
            s[0]=0
            s[1]=random.randint(0,HEIGHT//2)


    pygame.draw.circle(screen, (100,20,100), (800, 110), 70)
    pygame.draw.circle(screen, (170,40,170), (800, 110), 60)
    pygame.draw.circle(screen, (255,120,220), (800, 110), 50)

    pygame.draw.polygon(screen, (30,20,60), [(0,410),(180,270),(420,410)])
    pygame.draw.polygon(screen, (40,20,70), [(250,410),(520,170),(780,410)])
    pygame.draw.polygon(screen, (30,15,60), [(650,410),(900,240),(1000,410)])

    horizon=410
    pygame.draw.line(screen, PINK, (0, horizon), (WIDTH, horizon), 3)

    for i in range(0, WIDTH+60,30):
        pygame.draw.line(screen, BLUE, (WIDTH//2, horizon),(i,HEIGHT),1)

    for bx, bw, bh in background:
        pygame. draw. rect(screen, (12,12,22),(bx, HEIGHT-bh,bw,bh))

    window_timer+=1

    if window_timer>30:
        window_timer=0

        for building in window_state:
            for window in building:
                if random.random()<0.08:
                    window[2]=not window[2]

    for idx, (bx,bw,bh) in enumerate(foreground):
        top=HEIGHT-bh
        pygame.draw.rect(screen, BUILDING, (bx, top, bw, bh))
        pygame.draw.rect(screen, CYAN,(bx,top,bw,bh),2)

        for wx,wy, on in window_state[idx]:
            if on:
                pygame.draw.rect(screen, PINK, (wx,wy,8,12))

    font=pygame.font.SysFont("Arial", 42, True)
    tittle= font.render(" NEON WIREFRAME CITY", True, PINK)
    screen.blit(tittle, (20,20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()