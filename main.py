import tkinter as tk
from bar import Bar
import time

############################## GLOBAL VARIABLES ##############################
BG_COLOR = "#EA738D"

# Create the main window
root = tk.Tk()
bar = Bar(root)
root.configure(bg=BG_COLOR)

# Set the window size
window_width = 1200
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Bind key events to the move_bar function
root.bind("<KeyPress>", bar.move_bar)

# Start the Tkinter event loop
root.mainloop()