from tkinter import *
from PIL import Image, ImageTk
window= Tk()
window.title("Third GUI app")
window.config(bg="#ffffff")
window.geometry("800x600")

count= 0
def greet():
     global count
     count += 1
     label.config(text= str(greet))
     
     
#  displaying count on the screen 
label=Label(window, text="0")
label.config(font=("Monospace", 50))
label.pack()

button= Button(window,text="Click Me", command=greet)

orignal_img= Image.open("App GUI\\click.png")
resizing_img= orignal_img.resize((60, 80))
img= ImageTk.PhotoImage(resizing_img)


button.config(command=greet, font= ("Ink free", 15, "bold"), fg="#fff", bg="#909089",
              activebackground="#FF0000", activeforeground="#AAA71B") 
#||  The active bg/fg--> they are switching thier color when clicking
button.pack(pady=10)     # add  some spaces above the image




#  Create label  to show the image bollow the button
imag_label= Label(window, image= img, font=10, bg="#000fff")
imag_label.pack()


window.mainloop()