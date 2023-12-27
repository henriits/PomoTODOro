import tkinter as tk

window = tk.Tk()
window.title("Pomodoro TODO List")
window.geometry("600x400")

todo_list_frame = tk.Frame(window)
todo_list_frame.pack(fill=tk.BOTH, expand=True)

window.mainloop()