import os
import tkinter as tk
from tkinter import ttk , filedialog, messagebox


root= tk.Tk()
root.title("My notebooke")
root.option_add("*tearOff", False)
text_content= dict()

main= ttk.Frame(root)
main.pack(fill="both", expand=True, padx=5, pady=(4,0))

menubar= tk.Menu()
root.config(menu=menubar)

file_menu=tk.Menu(menubar)
help_menu= tk.Menu(menubar)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Help", menu= help_menu)


notebook= ttk.Notebook(main)
notebook.pack(fill="both",expand=True)


def create_file(content='', title='New'):
     container= ttk.Frame(notebook)
     container.pack()
     
     text_erea= tk.Text(container)
     text_erea.insert("end", content)
     text_erea.pack(side="left", fill='both',expand=True)
     
     notebook.add(container, text= title)
     notebook.select(container)
     
     text_content[str(text_erea)] = hash(content)
    
     text_scroll= ttk.Scrollbar(container, orient="vertical", command=text_erea.yview)
     text_scroll.pack(side="right", fill="y")
     text_erea['yscrollcommand']= text_scroll.set
    
     
def select_text_widget():
     tab_widget= root.nametowidget(notebook.select())
     text_widget= tab_widget.winfo_children()[0]
     return text_widget    
     
     
def save_file():
     file_path= filedialog. asksaveasfilename()
     try:
          filename= os.path.basename(file_path)
          text_widget= select_text_widget()
          content= text_widget.get("1.0", "end-1c")
          
          with open(file_path,'w') as f:
               f.write(content) 
      
     except (AttributeError, FileNotFoundError):
          print("Saving operation error!")
          return
     
     notebook.tab('current', text= filename)
     text_content[str(text_widget)]= hash(content)
            

def open_file():
     file_path= filedialog.askopenfilename()
     try:
          filename= os.path.basename(file_path)
          
          
          with open(file_path, "+r") as f:
               content=f.read()
               
     except (AttributeError, FileNotFoundError):
          print("Opening error!")
          return
     create_file(content, filename)

   
def check_changes():
     current_widget= select_text_widget()
     content= current_widget.get("1.0", "end-1c")
     name= notebook.tab("current")["text"]#name of the current tab
     
     if hash(content) != text_content[str(current_widget)]:
          if name[-1] != "*":
               notebook.tab("current", text=name+"*")
     elif name[-1] == "*":
          notebook.tab("current", text=name[:-1])
    
          
def confirm_quit():
     unsaved= False
     
     for tab in notebook.tabs():
          tab_widget=root.nametowidget(tab)
          text_widget= tab_widget.winfo_children()[0]
          content= text_widget.get("1.0", "end-1c")
          if hash(content) != text_content[str(text_widget)]:
               unsaved = True
               break
          
     if unsaved and not confirm_close():
               return
     
     root.destroy()


def close_current_tab():
     current_tab= select_text_widget()
     if unsaved_current_tab() and not confirm_close(): 
          return
     
     if (notebook.tabs()) == 1:
          create_file()
          
     notebook.forget(current_tab)
  
     
def unsaved_current_tab():
     text_widget= select_text_widget()
     content= text_widget.get("1.0", "end-1c")
     return hash(content) != text_content[str(text_widget)]
 

def confirm_close():
     return messagebox.askyesno(
          message="Tab unsaved. Are you sure you want to close it",
          icon="question",
          title="confirm close tab"
     )

     
def show_info():
     info= messagebox.showinfo(
          message="about us is perfect",
          title="about us"
     )
     
file_menu.add_command(label="New", command=create_file, accelerator="Ctrl +N")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl +S")
file_menu.add_command(label="Open...", command=open_file, accelerator="Ctrl +O")
file_menu.add_command(label="Close Tab", command=close_current_tab, accelerator="Ctrl +W")
file_menu.add_command(label="Exit", command=confirm_quit, accelerator="Ctrl +Shift+W")

help_menu.add_command(label="About", command=show_info, accelerator="Ctrl +I")

root.bind("<KeyPress>", lambda event: check_changes())
root.bind("<Control-n>", lambda event: create_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-w>", lambda event: close_current_tab())
root.bind("<Control-Shift-W>", lambda event: confirm_quit())
root.bind("<Control-i>", lambda event: show_info())
create_file()


root.mainloop()