# Import required modules
import pgzrun
from bar import Bar
from ball import Ball
from bricks import Bricks

# Set the window dimensions using WIDTH and HEIGHT variables
WIDTH = 1200
HEIGHT = 600

# Initialize game objects
bar = Bar()
ball = Ball()
bricks = Bricks()

# Define variables for game state
game_over = False
player_won = False

# Function to display user interface elements
def draw_ui():
    # Display score, lives, etc.
    screen.draw.text("Score: 0", (10, 10), color="white")

# Function to check win conditions
def check_win_condition():
    # Check if all bricks are destroyed
    return len(bricks.bricks) == 0

def update():
    global game_over, player_won

    if not game_over:
        bar.update()
        ball.update(bar, bar.x, bar.y)
        bricks.update(ball)

        if check_win_condition():
            player_won = True
            game_over = True
    else:
        # Logic for handling game over state
        pass

def draw():
    screen.clear()
    bar.draw(screen)
    ball.draw(screen)
    bricks.draw(screen)

    draw_ui()

    if game_over:
        if player_won:
            screen.draw.text("You Win!", (WIDTH // 2 - 50, HEIGHT // 2), color="green", fontsize=50)
        else:
            screen.draw.text("Game Over", (WIDTH // 2 - 70, HEIGHT // 2), color="red", fontsize=50)

# Start the game
pgzrun.go()
