import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


"""Clicking the button will change the content"""
root= tk.Tk()
root.title("Hello tkinter")
lable= ttk.Label(root, text="Clich the button")
lable.pack()

def on_button_click():
     messagebox.showinfo("Hello", "Tkinter is fun!")
     
     
buttom= ttk.Button(root, text= "Click Me", command= on_button_click)
buttom.pack() 


root.mainloop()   