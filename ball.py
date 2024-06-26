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
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = SPEED
        self.on_hold = True
        self.current_angle = 315 

    def move(self):
        angle_radians = math.radians(self.current_angle)
        speed_x = self.speed * math.cos(angle_radians)
        speed_y = self.speed * math.sin(angle_radians)

        self.x += speed_x
        self.y += speed_y

    def draw(self, screen):
        screen.draw.filled_circle((self.x, self.y), RADIUS, 'white')
    
    def sticking(self, bar_x, bar_y):
        self.x = bar_x + BAR_WIDTH//2
        self.y = bar_y - BAR_HEIGHT//2
    
    def update(self, bar, bar_x, bar_y):
        if keyboard.is_pressed('return'):
            self.on_hold = False

        if self.on_hold:
            self.sticking(bar_x, bar_y)
        else:
            self.check_wall_collision()
            self.check_bar_collision(bar)
            self.move()
    

    # Changing direction based on the corner of the ball hits.
    def right_collision(self):
        if self.current_angle == 315:
            self.current_angle = 225
        elif self.current_angle == 45:
            self.current_angle = 135
    
    def left_collision(self):
        if self.current_angle == 135:
            self.current_angle = 45
        elif self.current_angle == 225:
            self.current_angle = 315
    
    def top_collision(self):
        if self.current_angle == 315:
            self.current_angle = 45
        elif self.current_angle == 225:
            self.current_angle = 135
    
    def bot_collision(self):
        if self.current_angle == 45:
            self.current_angle = 315
        elif self.current_angle == 135:
            self.current_angle = 225
    
    #Check collisions:
    def check_wall_collision(self):
        if self.x - 10 <= 0:
            self.left_collision()
        elif self.x + 10 >= 1200:
            self.right_collision()
        
        if self.y - 10 <= 0:
            self.top_collision()
    

    def check_bar_collision(self, bar):
        if bar.rect.colliderect(Rect(self.x - RADIUS, self.y - RADIUS, RADIUS * 2, RADIUS * 2)):
            self.bot_collision()

    #Bricks Collisions are in the bricks.py, because it's more optimal in that class, bad structure by me