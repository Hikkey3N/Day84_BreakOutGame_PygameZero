from bar import Bar
from ball import Ball
import pgzrun
import keyboard

# Set the window dimensions using WIDTH and HEIGHT variables
WIDTH = 1200
HEIGHT = 600

bar = Bar()
ball = Ball()

def update():
    bar.update()
    ball.update(bar.x, bar.y)
    

def draw():
    screen.clear()
    bar.draw(screen)
    ball.draw(screen)


pgzrun.go()
