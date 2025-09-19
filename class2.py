from tkinter import *
from PIL import Image, ImageTk
# Label is an erea widget that holds text or an image within a window
window= Tk()
window.geometry("800x500")

# phto= PhotoImage(file="C:\\Users\\SALIMA\\Pictures\\Saved Pictures\\1.jpg")
#  Tkinter.PhotoImage only support png ,gif, .ppm/.pgm

img = Image.open("C:\\Users\\SALIMA\\Pictures\\Saved Pictures\\1.jpg")
phto= ImageTk.PhotoImage(img)

label_win = Label(window,
                  text="Hello world",
                  font=("Arial", 10, "bold"),
                  fg= "#2f0bd1",
                  bg= "#000",
                  relief="raised",
                  bd=10,
                  padx=20,
                  pady=10,
                  image=phto,
                  compound= "bottom"
                  )
label_win.image=phto
label_win.pack()



window.mainloop()