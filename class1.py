from tkinter import *
from PIL import Image, ImageTk
window= Tk() # Instantiate an instance of a window
window.geometry("800x550")
window.title("My first GUI app!")
     
# icon= PhotoImage(file=r"C:\Users\SALIMA\Pictures\Saved Pictures\great photo.jpg")
img = Image.open(r"C:\Users\SALIMA\Pictures\Saved Pictures\great photo.jpg")
icon= ImageTk.PhotoImage(img)
window.iconphoto(True, icon)

# Outer frame acts as the colored border
border_frame = Frame(window, bg="#000", padx=2, pady=2)
border_frame.pack(pady=20)

# Inner label sits inside the border

window.config(bg="#a39c9c")   # Make window soft gray
win_Label=Label(window,text="Hello world", 
               font=("Arial", 15, "bold"),
               foreground="red",
               background="#fff",
               bd=5,
               relief="ridge")
win_Label.pack()





window.mainloop()# place window on the computer screen. listen for event