import tkinter as tk
from tkinter import messagebox

def solve():
    try:
        a1 = float(entry_a1.get())
        b1 = float(entry_b1.get())
        c1 = float(entry_c1.get())
        a2 = float(entry_a2.get())
        b2 = float(entry_b2.get())
        c2 = float(entry_c2.get())

        det = a1 * b2 - a2 * b1
        if det == 0:
            messagebox.showerror("Помилка", "Система не має розв'язків або має нескінченно багато розв'язків.")
            return

        x = (c1 * b2 - c2 * b1) / det
        y = (a1 * c2 - a2 * c1) / det

        result_label.config(text=f"Розв'язок: x = {x:.2f}, y = {y:.2f}")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть числові значення.")

window = tk.Tk()
window.title("Розв'язання системи рівнянь")
window.geometry("300x200")

frame1 = tk.Frame(window)
frame1.pack(pady=5)

tk.Label(frame1, text="a1").grid(row=0, column=0)
entry_a1 = tk.Entry(frame1, width=5)
entry_a1.grid(row=0, column=1)

tk.Label(frame1, text="b1").grid(row=0, column=2)
entry_b1 = tk.Entry(frame1, width=5)
entry_b1.grid(row=0, column=3)

tk.Label(frame1, text="c1").grid(row=0, column=4)
entry_c1 = tk.Entry(frame1, width=5)
entry_c1.grid(row=0, column=5)

frame2 = tk.Frame(window)
frame2.pack(pady=5)

tk.Label(frame2, text="a2").grid(row=0, column=0)
entry_a2 = tk.Entry(frame2, width=5)
entry_a2.grid(row=0, column=1)

tk.Label(frame2, text="b2").grid(row=0, column=2)
entry_b2 = tk.Entry(frame2, width=5)
entry_b2.grid(row=0, column=3)

tk.Label(frame2, text="c2").grid(row=0, column=4)
entry_c2 = tk.Entry(frame2, width=5)
entry_c2.grid(row=0, column=5)

solve_button = tk.Button(window, text="Розв'язати", command=solve)
solve_button.pack(pady=10)

result_label = tk.Label(window, text="Розв'язок: ")
result_label.pack(pady=5)

window.mainloop()