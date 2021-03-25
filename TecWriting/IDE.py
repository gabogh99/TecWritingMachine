import os
import codecs
from aLexico import *
from aSintactico import prueba, parser
from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox



def Ventana2(data, title):

    vt2 = Tk()
    vt2.title(title)
    vt2.geometry('600x600')

    canvas = Canvas(vt2)
    scroll_y = Scrollbar(vt2,orient="vertical", command=canvas.yview)

    frame=Frame(canvas)

    i=0;
    for i in range(len(data)):
        e = Label(frame, text=data[i])
        e.grid(row=i, column=2)

    canvas.create_window(0,0, anchor='nw', window = frame)
    canvas.update_idletasks()
    canvas.configure(scrollregion = canvas.bbox('all'),
                     yscrollregion = scroll_y.set)

    canvas.pack(fill='both', expand=True, side='left')
    scroll_y.pack(fill='y', side='right')
    vt2.mainloop

def Ventana():

    def aLexico():

        cadena = texto.get(1.0,'end-1c')

        if(len(cadena)>0):
            lexico = analzador
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

        cadena = texto.get(1.0, 'end-1c')

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
            


    
    
