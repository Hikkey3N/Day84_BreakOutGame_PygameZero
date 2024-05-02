from pygame.rect import Rect
import pgzrun
import math
import keyboard

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

BAR_WIDTH = 150
BAR_HEIGHT = 20

SPEED = 5

RADIUS = 10
# Define the angles in degrees
# 45  ↘️
# 135 ↙️
# 225 ↖️
# 315 ↗️
ANGLES = [45, 135, 225, 315]

class Ball:
    def __init__(self, x, y):
        self.x = x + BAR_WIDTH//2
        self.y = y - BAR_HEIGHT//2
        self.speed = SPEED
        self.on_hold = True
        self.current_angle = 0  

    def move(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        speed_x = self.speed * math.cos(angle_radians)
        speed_y = self.speed * math.sin(angle_radians)

        self.x += speed_x
        self.y += speed_y

    def draw(self, screen):
        screen.draw.filled_circle((self.x, self.y), RADIUS, 'white')
    
    def sticking(self, bar_x, bar_y):
        self.x = bar_x + BAR_WIDTH//2
        self.y = bar_y - BAR_HEIGHT//2
    

    def update(self, bar_x, bar_y):
        if keyboard.is_pressed('return'):
            self.on_hold = False

        if self.on_hold:
            self.sticking(bar_x, bar_y)
        else:
            self.move(0)