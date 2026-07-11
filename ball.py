import pgzrun

WIDTH = 800
HEIGHT=600
TITLE="Flappy Ball"

gravity=2000

class Ball:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
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

def update(dt):
    uy=ball.vy
    ball.vy+=gravity*dt
    ball.y+=(uy+ball.vy)*0.5*dt
    if ball.y>HEIGHT-ball.radius:
        ball.y=HEIGHT-ball.radius
        ball.vy=-ball.vy*0.9
    ball.x+=ball.vx*dt
    if ball.x>WIDTH+ball.radius:
        ball.vx=-ball.vx
    if ball.x<ball.radius:
        ball.vx=ball.vx*dt

def on_key_down(key):
    if key==keys.SPACE:
        ball.vy=-500
    if key==keys.RIGHT:
        ball.vx=500
    if key==keys.LEFT:
        ball.vx=-500

pgzrun.go()