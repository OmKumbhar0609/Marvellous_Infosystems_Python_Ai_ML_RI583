# Voting Eligibility Checker

import tkinter as tk
from tkinter import messagebox

def check_eligibility():
    name = name_entry.get().strip()

    try:
        age = int(age_entry.get())

        if not name:
            messagebox.showerror("Error", "Please enter your name.")
        elif age < 0:
            messagebox.showerror("Error", "Age cannot be negative.")
        elif age >= 18:
            result_label.config(
                text=f"{name} is eligible to vote."
            )
        else:
            result_label.config(
                text=f"{name} is not eligible to vote."
            )
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid age.")

root = tk.Tk()
root.title("Voting Eligibility Checker")
root.geometry("350x250")

tk.Label(root, text="Enter Your Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Enter Your Age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack()

tk.Button(
    root, text="Check Eligibility", command=check_eligibility
).pack(pady=10)

result_label = tk.Label(root, text="Result will appear here")
result_label.pack()

root.mainloop()
