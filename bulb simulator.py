import pygame

pygame.init()

WIDTH=500
HEIGHT=500

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Bulb Simulator")

WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
GRAY=(120,120,120)
GREEN=(0,200,0)
RED=(220,0,0)

font=pygame.font.SysFont(None,35)

bulb_on=False

running=True

while running:
    screen.fill(WHITE)

    if bulb_on:
        bulb_color=YELLOW
    else:
        bulb_color=GRAY

    pygame.draw.circle(screen, bulb_color, (250,150), 50)

    pygame.draw.rect(screen, BLACK, (235,195,30,40))

    button=pygame.Rect(175,320,150,60)

    if bulb_on:
        pygame.draw.rect(screen, RED, button)
        text=font.render("TURN OFF", True, WHITE)

    else:
        pygame.draw.rect(screen, GREEN, button)
        text=font.render("TURN ON", True, WHITE)

    screen.blit(text, (195,337))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                bulb_on=not bulb_on

    pygame.display.update()

pygame.quit()