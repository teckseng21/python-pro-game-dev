import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill((255,255,255))

class rectangle:
    def __init__(self, colour, x, y, width, height):
        self.colour=colour
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def draw(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

class circle:
    def __init__(self, colour, radius, pos, width=0):
        self.colour=colour
        self.radius=radius
        self.pos=pos
        self.width=width
        self.screen=screen

    def draw(self):
        pygame.draw.circle(self.screen,self.colour, self.pos, self.radius, self.width)

class line:
    def __init__(self,colour, start_pos, end_pos, width=1):
        self.colour=colour
        self.start_pos=start_pos
        self.end_pos=end_pos
        self.width=width

    def draw(self):
        pygame.draw.line(self.screen, self.colour, self.start_pos, self.end_pos, self.width)

rect=rectangle((0,255,0), 250,250, 100, 50)
cir=circle((255,255,0), 50, (150,250))
lin=line((255,165,0), (100,100), (400,400), 2)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if (event.type==pygame.KEYDOWN):
            if event.key==pygame.K_r:
                rect.draw()
                pygame.display.update()
            elif event.key==pygame.K_c:
                cir.draw()
                pygame.display.update()
            elif event.key==pygame.K_l:
                lin.draw()
                pygame.display.update()