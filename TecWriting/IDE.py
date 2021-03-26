from tkinter import *
import os
import codecs
from aLexico import *
from aSintactico import prueba, parser
from tkinter import filedialog as FileDialog
from tkinter import messagebox


root = Tk()
root.title('TecWriting Machine')
root.geometry("800x800")


def new_file():
    my_text.delete("1.0", END)
    root.title()
    status_bar.config(text="New File       ")
    root.title("New File  -  TecWriting Machine")

def open_file():

    my_text.delete("1.0", END)

    text_file = FileDialog.askopenfilename(initialdir = '.',title="Open File", filetypes=[("Text Files", "*.txt")])
    global open_status_name

    name = text_file
    status_bar.config(text=name)
    root.title(f'{name} - TecWriting Machine')

    text_file = open(text_file, 'r')
    reader = text_file.read()

    my_text.insert(END, reader)
    text_file.close()

def save_as_file():
    text_file = FileDialog.asksaveasfilename(defaultextension=".*",initialdir = ".", title="Save File", filetypes=[("Text Files", "*.txt")])
    if text_file:
        name = text_file
        name = name.replace("C:/Users/Familia/Documents/Gabo/Lenguajes y Compi/Compi", "")
        status_bar.config(text=")
        root.title(f'Saved: {name} - TecWriting Machine')

        text_file = open(text_file,'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        
    
my_frame = Frame(root)
my_frame.pack(pady=5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)


my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground = "grey", selectforeground="black",undo = True, yscrollcommand = text_scroll.set)
my_text.pack()

text_scroll.config(command = my_text.yview)

my_menu = Menu(root)
root.config(menu = my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command = save_file)
file_menu.add_command(label="Save As", command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit")

compile_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Run", menu=compile_menu)
compile_menu.add_cascade(label="Analizador Léxico")
compile_menu.add_command(label="Analizador Sintáctico")


status_bar = Label(root, text = "Ready       ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady = 5)




root.mainloop()
