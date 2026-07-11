import pgzrun

WIDTH=800
HEIGHT=600
TITLE="Multiple Ball"

gravity=2000

class Ball:
    def __init__(self, initial_x, initial_y):
        self.x=initial_x
        self.y=initial_y
        self.radius=40
        self.vx=200
        self.vy=0
    
    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,"blue")

ball=Ball(50,100)

def draw():
    screen.clear()
    ball.draw()

pgzrun.go()