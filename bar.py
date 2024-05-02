from pygame.rect import Rect
import pgzrun
import math
import keyboard

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

BAR_WIDTH = 150
BAR_HEIGHT = 20
BAR_COLOR = '#89ABE3'
BAR_SPEED = 10


class Bar:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2 - BAR_WIDTH/2
        self.y = (WINDOW_HEIGHT - WINDOW_HEIGHT*(1/10)) - BAR_HEIGHT/2

    def draw(self, screen):
        screen.draw.filled_rect(Rect(self.x, self.y, BAR_WIDTH, BAR_HEIGHT), BAR_COLOR)

    def move(self, direction):
        if direction == 'left':
            if self.x > 0:
                self.x -= BAR_SPEED
        elif direction == 'right':
            if self.x + BAR_WIDTH < 1200:
                self.x += BAR_SPEED
    
    def update(self):
        if keyboard.is_pressed('left'):
            self.move('left')
        elif keyboard.is_pressed('right'):
            self.move('right')
    