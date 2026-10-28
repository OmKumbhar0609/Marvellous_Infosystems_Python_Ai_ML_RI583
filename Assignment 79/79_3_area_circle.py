# Area of a Circle

import tkinter as tk
from tkinter import messagebox
import math

def calculate_area():
    try:
        radius = float(radius_entry.get())

        if radius < 0:
            messagebox.showerror("Error", "Radius cannot be negative.")
            return

        area = math.pi * radius ** 2
        result_label.config(text=f"Area of Circle = {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid radius.")

root = tk.Tk()
root.title("Area of Circle:")
root.geometry("350x200")

tk.Label(root, text="Enter Radius:").pack(pady=5)
radius_entry = tk.Entry(root)
radius_entry.pack()

tk.Button(
    root, text="Calculate Area", command=calculate_area
).pack(pady=10)

result_label = tk.Label(root, text="Area will appear here")
result_label.pack()

root.mainloop()
