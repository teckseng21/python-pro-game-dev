import pygame

pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

img=pygame.image.load("backgroundone.jpg")
image=pygame.transform.scale(img,(WIDTH,HEIGHT))

while(True):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

    font=pygame.font.SysFont("Time New Roman", 72)
    text=font.render("Happy", True, (0,0,0))
    text2=font.render("Birthday", True, (0,0,0))

    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    screen.blit(text, (210, 180))
    screen.blit(text2, (180, 264))
    pygame.display.update()
    pygame.time.delay(2000)

    image2=pygame.image.load("backgroundtwo.jpg")
    font2=pygame.font.SysFont("Arial", 36)
    text3=font2.render("Wish you a bright future ahead!", True, (0,0,0))
    screen.fill((255,255,255))
    screen.blit(image2,(0,0))
    screen.blit(text3, (30, 30))
    pygame.display.update()
    pygame.time.delay(2000)

    image3=pygame.image.load("backgroundthree.jpg")
    screen.fill((255,255,255))
    screen.blit(image3,(0,0))
    pygame.display.update()
    pygame.time.delay(2000)
    