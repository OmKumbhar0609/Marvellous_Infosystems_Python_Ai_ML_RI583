# Find the Largest Number

import tkinter as tk
from tkinter import messagebox

def find_maximum():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())

        largest = max(a, b, c)
        result_label.config(text=f"Largest Number = {largest}")
    except ValueError:
        messagebox.showerror("Error", "Enter all three valid numbers.")

root = tk.Tk()
root.title("Find the Largest Number:")
root.geometry("350x300")

tk.Label(root, text="Enter First Number:").pack(pady=3)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number:").pack(pady=3)
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Enter Third Number:").pack(pady=3)
entry3 = tk.Entry(root)
entry3.pack()

tk.Button(
    root, text="Find Maximum", command=find_maximum
).pack(pady=10)

result_label = tk.Label(root, text="Largest number will appear here")
result_label.pack()

root.mainloop()
