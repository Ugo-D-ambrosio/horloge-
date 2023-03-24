from tkinter import *

from time import strftime


root=Tk()
root.title("horloge")

def time():
    string=strftime('%H:%M:%S:%p')
    label.config(text=string)
    label.after(1000,time)
    
label=Label(root,font=('arial',80),foreground='cyan',background='black')
label.pack(anchor='center')
time()

mainloop()