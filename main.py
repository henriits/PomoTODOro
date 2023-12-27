import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Pomodoro TODO List")
window.geometry("600x400")

canvas = Canvas(window, bg="#1b1b1b")
canvas.pack(fill=BOTH, expand=TRUE)

# Create a round button with no image
round_button = tk.Button(window, relief=tk.FLAT, borderwidth=10, background="#000080", text="Add TODO")
round_button.pack()

# Create a label for the input field
label_text = tk.Label(window, text="Enter todo item:", font=("Arial", 15))
label_text.pack()

# Create an input field for adding new todo items
todo_input_field = tk.Entry(window, font=("Arial", 15))
todo_input_field.pack()

window.mainloop()
