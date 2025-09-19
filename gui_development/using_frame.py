import tkinter as tk


root= tk.Tk()

frame1 = tk.Frame(root, bg="lightblue")
frame1.pack(side="top", fill="both", expand=True)

label1 = tk.Label(frame1, text="Inside Frame 1")
label1.pack(pady=10)

frame2 = tk.Frame(root, bg="lightgreen")
frame2.pack(side="top", fill="both", expand=True)

button1 = tk.Button(frame2, text="Inside Frame 2")
button1.pack(padx=10)

root.mainloop()