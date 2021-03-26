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

def Ventana2(data, title):

    vt2 = Tk()
    vt2.title(title)
    vt2.geometry("600x600")

    canvas = Canvas(vt2)
    scroll_y = Scrollbar(vt2,orient="vertical", command=canvas.yview)

    frame=Frame(canvas)

    i=0;
    for i in range(len(data)):
        e = Label(frame, text=data[i])
        e.grid(row=i, column=2)

    canvas.create_window(0,0, anchor='nw', window = frame)
    canvas.update_idletasks()
    

    canvas.pack(fill='both', expand=True, side='left')
    scroll_y.pack(fill='y', side='right')
    vt2.mainloop()




def new_file():
    my_text.delete("1.0", END)
    root.title()
    status_bar.config(text="New File       ")
    root.title("New File  -  TecWriting Machine")

def open_file():

    my_text.delete("1.0", END)

    text_file = FileDialog.askopenfilename(initialdir = '.',title="Open File", filetypes=[("Text Files", "*.txt")])

    
    global open_status_name
    open_status_name = text_file

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
        root.title(f'Saved: {name} - TecWriting Machine')

        text_file = open(text_file,'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
    else:
        
        messagebox.showwarning(message="Guardado Cancelado!!")

def aLexico():

    cadena = my_text.get(1.0,'end-1c')

    if(len(cadena)>0):
        lexico = analizador
        lexico.input(cadena)
        tok = lexico.token()
        a_tok = []
        while True:
            tok = lexico.token()
            if not tok: break
            a_tok.append(tok)
        Ventana2(a_tok,"Analizador Lexico")
    else:
        messagebox.showwarning(message="Debes escribir código!!", title = "Error")

def aSintactico():

    cadena = my_text.get(1.0, 'end-1c')
    
    if(len(cadena) > 0):
        cad = []

        cont = 0;
        for i in prueba(cadena):

            if(cont==0):
                cont += 1
            else:
                cad.append(i)

        Ventana2(cad, "Analizador Sintactica")
    else:
        messagebox.showwarning(message="Debes escribir código!!", title="Error")


        
    
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
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As", command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command = root.quit)

compile_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Run", menu=compile_menu)
compile_menu.add_cascade(label="Analizador Léxico", command=aLexico)
compile_menu.add_command(label="Analizador Sintáctico",command=aSintactico)


status_bar = Label(root, text = "Ready       ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady = 5)

root.mainloop()





