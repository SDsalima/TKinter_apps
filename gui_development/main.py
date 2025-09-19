import tkinter as tk
from tkinter import ttk


def greet():
     print("Hello world")
     
     
root= tk.Tk() 
root.title("Hello!")

geet_button=ttk.Button(root, text='Greet', command=greet)
geet_button.pack(side="left", fill="x", expand=True)

greet_button= ttk.Button(root, text="Quit", command=root.destroy)
geet_button.pack(side="left", fill="x", expand=True)
tk.mainloop()