import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill((255,255,255))


class circle:
    def __init__(self, colour, radius, pos, width=0):
        self.colour=colour
        self.radius=radius
        self.pos=pos
        self.width=width
        self.screen=screen
    
    def draw(self):
        pygame.draw.circle(self.screen,self.colour, self.pos, self.radius, self.width)
    def grow(self, x):
        self.radius+=x
        pygame.draw.circle(self.screen,self.colour,self.pos,self.radius,self.width)

blue_circle=circle((0,0,255), 50, (250,250))
green_circle=circle((0,255,0), 70, (250,250))
red_circle=circle((255,0,0),90, (250,250))



while True:
    for event in pygame.event.get():
        if (event.type==pygame.MOUSEBUTTONDOWN):
            red_circle.draw()
            green_circle.draw()
            blue_circle.draw()
            pygame.display.update()
        if (event.type==pygame.MOUSEBUTTONUP):
            red_circle.grow(10)
            green_circle.grow(10)
            blue_circle.grow(10)
            pygame.display.update()