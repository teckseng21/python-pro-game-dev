import pygame

pygame.init()

screen=pygame.display.set_mode((900,600))
pygame.display.set_caption("Match the following")

white=(255,255,255)
black=(0,0,0)
green=(0,150,0)
red=(200,0,0)

screen.fill(white)

mcdonalds=pygame.image.load("mcdonalds.png")
shell=pygame.image.load("shell.png")
sia=pygame.image.load("SIA.png")
starbucks=pygame.image.load("starbucks.png")

font=pygame.font.SysFont("Times New Roman",28)

images=[
    (mcdonalds, (100,80), "McDonald's"),
    (shell, (100,180), "Shell"),
    (sia, (100,280), "SIA"),
    (starbucks, (100,380), "Starbucks"),
]

right_names=[
    ("Shell", (600,100)),
    ("Starbucks", (600,200)),
    ("McDonald's", (600,300)),
    ("SIA", (600,400))
]

for img,pos,name in images:
    screen.blit(img,pos)

for text,pos in right_names:
    t=font.render(text, True, black)
    screen.blit(t,pos)

pygame.display.update()

selected_left=None
selected_pos=None
match_count=0
wrong_match=False
total_attempts=0

running=True

while running:
    events=pygame.event.poll()

    if events.type==pygame.QUIT:
        running=False

    if events.type==pygame.MOUSEBUTTONDOWN:
        x,y=pygame.mouse.get_pos()

        for img,pos,name in images:
            rect=img.get_rect(topleft=pos)
            if rect.collidepoint(x,y):
                selected_left=name
                selected_pos=(pos[0]+120,pos[1]+40)

        for text,pos in right_names:
            text_surface=font.render(text, True, black)
            text_rect=text_surface.get_rect(topleft=pos)
            if text_rect.collidepoint(x,y) and selected_left:
                pygame.draw.line(
                    screen,
                    black,
                    selected_pos,
                    (pos[0],pos[1]+15),
                    3
                )

                pygame.display.update()
                total_attempts+=1

                if selected_left==text:
                    match_count+=1

                else:
                    wrong_match=True

                selected_left=None

        if total_attempts==4:
            screen.fill("lightblue")
            if wrong_match:
                result=font.render("LOSER", True, red)

            else:
                result=font.render("WINNER", True, green)

            screen.blit(result,(350,250))
            pygame.display.update()
            result_screen=True
            while result_screen:
                result_events=pygame.event.wait()
                if result_events.type==pygame.QUIT:
                    result_screen=False
                    running=False

pygame.quit()