import tkinter as tk
from tkinter import messagebox
import os

# Constants
SAVE_FILE = "brownie_points.txt"

# Functionality
def load_points():
    """Load points from the save file."""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return 0
    return 0

def save_points(points):
    """Save points to the save file."""
    with open(SAVE_FILE, "w") as file:
        file.write(str(points))

def increment_points():
    """Increment the brownie points and update the display."""
    global points
    points += 1
    update_points_display()

def reset_points():
    """Reset the brownie points to 0 and update the display."""
    global points
    points = 0
    update_points_display()

def update_points_display():
    """Update the points label and save the points."""
    points_label.config(text=f"Brownie Points: {points}")
    save_points(points)

# Load initial points
points = load_points()

# UI Setup
root = tk.Tk()
root.title("Brownie Points Counter")
root.geometry("300x200")
root.resizable(False, False)

# Styling
root.configure(bg="#f9f9f9")

# Points Display
points_label = tk.Label(root, text=f"Brownie Points: {points}", font=("Helvetica", 18, "bold"), bg="#f9f9f9", fg="#333")
points_label.pack(pady=20)

# Increment Button
increment_button = tk.Button(
    root,
    text="Add Point",
    command=increment_points,
    font=("Helvetica", 14),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    activeforeground="white",
    relief="flat",
    borderwidth=0,
    padx=20,
    pady=10
)
increment_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(
    root,
    text="Reset Points",
    command=reset_points,
    font=("Helvetica", 14),
    bg="#888888",
    fg="white",
    activebackground="#777777",
    activeforeground="white",
    relief="flat",
    borderwidth=0,
    padx=20,
    pady=10
)
reset_button.pack(pady=10)

# Add button hover styling
def apply_styles(widget, normal_color, hover_color):
    widget.bind("<Enter>", lambda e: widget.config(bg=hover_color))
    widget.bind("<Leave>", lambda e: widget.config(bg=normal_color))

apply_styles(increment_button, "#4CAF50", "#45a049")
apply_styles(reset_button, "#888888", "#777777")

# Run the App
root.mainloop()
