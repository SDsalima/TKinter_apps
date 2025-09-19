"""
side-by-side example that shows both tk.Label and ttk.Label in the same window 
so you can compare their appearance and styling behavior directly.
"""
import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Label Comparison")
root.geometry("300x150")

# tk.Label (classic)
tk_label = tk.Label(root, text="Classic tk.Label", bg="lightblue", fg="darkblue", font=("Helvetica", 12))
tk_label.pack(pady=10)

# ttk.Label (themed)
style = ttk.Style()
style.configure("My.TLabel", foreground="darkgreen", background="lightgray", font=("Helvetica", 12))

ttk_label = ttk.Label(root, text="Modern ttk.Label", style="My.TLabel")
ttk_label.pack(pady=10)

# Run the app
root.mainloop()