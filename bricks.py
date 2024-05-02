import pgzrun
from pygame.rect import Rect
import random

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

BRICK_WIDTH = 100
BRICK_HEIGHT = 50
BRICK_ROWS = 6
BRICKS_PER_ROW = WINDOW_WIDTH // BRICK_WIDTH

BRICK_COLOR = (155, 155, 155)
BORDER_COLOR = (0, 0, 0)

RADIUS = 10

class Bricks:
    def __init__(self):
        self.bricks = []
        for row in range(BRICK_ROWS):
            for col in range(BRICKS_PER_ROW):
                brick_x = col * BRICK_WIDTH
                brick_y = (row + 1) * BRICK_HEIGHT  # Starting 50 units below the top ceiling
                brick_rect = Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
                self.bricks.append(brick_rect)

    def draw(self, screen):
        for brick_rect in self.bricks:
            screen.draw.rect(brick_rect, BORDER_COLOR)  # Draw brick border
            screen.draw.filled_rect(brick_rect.inflate(-4, -4), BRICK_COLOR)  # Draw brick with margin
    
    def remove_brick(self, brick_rect):
        if brick_rect in self.bricks:
            self.bricks.remove(brick_rect)
    
    def detect_collision(self, ball):
        # Calculate additional collision points on the ball
        left_collision_point = (ball.x - RADIUS, ball.y)
        right_collision_point = (ball.x + RADIUS, ball.y)
        top_collision_point = (ball.x, ball.y - RADIUS)
        bot_collision_point = (ball.x, ball.y + RADIUS)

        # Check collision with each brick
        for brick_rect in self.bricks:
            if brick_rect.collidepoint(left_collision_point):
                ball.left_collision()
                self.bricks.remove(brick_rect)
            elif brick_rect.collidepoint(right_collision_point):
                ball.right_collision()
                self.bricks.remove(brick_rect)
            elif brick_rect.collidepoint(top_collision_point):
                ball.top_collision()
                self.bricks.remove(brick_rect)
            elif brick_rect.collidepoint(bot_collision_point):
                ball.bot_collision()
                self.bricks.remove(brick_rect)

    def update(self, ball):
        self.detect_collision(ball)
    