import tkinter as tk

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

BAR_WIDTH = 200
BAR_HEIGHT = 20
BAR_COLOR = '#89ABE3'

class Bar:
    def __init__(self, master):
        self.master = master

        self.x = (WINDOW_WIDTH/2) - (BAR_WIDTH/2)
        self.y = WINDOW_HEIGHT * (5/6)

        self.the_bar = tk.Frame(self.master, width=BAR_WIDTH, height=BAR_HEIGHT, bg=BAR_COLOR)
        self.the_bar.place(x=self.x, y=self.y)


    # Moving bar, if touches wall
    def move_bar(self, event):
        key = event.keysym

        if key == "Left":
            if self.x > 0:
                self.x -= 20
        
        if key == "Right":
            if self.x + BAR_WIDTH < 1200:
                self.x += 20
        
        self.the_bar.place(x=self.x, y=self.y)