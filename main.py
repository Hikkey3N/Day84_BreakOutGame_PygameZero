from bar import Bar
from ball import Ball
from bricks import Bricks
import pgzrun
import keyboard

# Set the window dimensions using WIDTH and HEIGHT variables
WIDTH = 1200
HEIGHT = 600

bar = Bar()
ball = Ball()
bricks = Bricks()

def update():
    bar.update()
    ball.update(bar, bar.x, bar.y)
    bricks.update(ball)
    

def draw():
    screen.clear()
    bar.draw(screen)
    ball.draw(screen)
    bricks.draw(screen)


pgzrun.go()
