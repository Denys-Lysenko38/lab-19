import tkinter as tk
from datetime import datetime

def change_color(color_name, color_code):
    window.config(bg=color_code)
    with open("report.txt", "a") as file:
        file.write(f"{datetime.now()}: {color_name}\n")

window = tk.Tk()
window.title("Кольори веселки")
window.geometry("320x260")
window.config(bg="green")

colors = [
    ("Red", "#FF0000"),
    ("Orange", "#FFA500"),
    ("Yellow", "#FFFF00"),
    ("Green", "#008000"),
    ("Light_blue", "#00FFFF"),
    ("Blue", "#0000FF"),
    ("Purple", "#800080")
]

for color_name, color_code in colors:
    button = tk.Button(window, text=color_name, bg=color_code, command=lambda c=color_name, cc=color_code: change_color(c, cc))
    button.pack(fill=tk.BOTH, expand=True)

window.mainloop()