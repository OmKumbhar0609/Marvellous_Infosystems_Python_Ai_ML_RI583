# Basic Login Form

import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Predefined credentials for demonstration
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror(
            "Login Failed", "Invalid username or password."
        )

root = tk.Tk()
root.title("Basic Login Form")
root.geometry("350x230")

tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()
