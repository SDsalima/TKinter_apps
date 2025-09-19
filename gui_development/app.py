import tkinter as tk
from tkinter import ttk


def greet():
     print(f"Hello, {name_entered.get()}!")
root= tk.Tk()
root.title("Greeter")

name_entered= tk.StringVar()
name_lable= ttk.Label(root, text="Name: ")
name_lable.pack(side="left", padx=(0,10))
name_entry= ttk.Entry(root, width= 15, textvariable= name_entered)
name_entry.pack(side='left')
name_entry.focus()

buttom= tk.Button(root, text="clik here!", command= greet)
buttom.pack(side="right",fill="both", pady=(10,10))

root.mainloop()