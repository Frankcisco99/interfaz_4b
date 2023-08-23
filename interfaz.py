import tkinter
from tkinter import ttk
import json

ventana = tkinter.Tk()
ventana.title("Codigo de error")

#etiqueta
titulo = ttk.Label(ventana,
                   text="Ingrese codigo",
                   font="Calibri 24 bold")
titulo.pack(padx=10,
            pady=10)
#entrada de texto
entrada = ttk.Entry(ventana)
entrada.pack(padx=10,
             pady=10)

btn_buscar = ttk.Button(ventana,
                        text="Buscar codigo")
btn_buscar.pack(padx=10, pady=10)

ventana.mainloop()
