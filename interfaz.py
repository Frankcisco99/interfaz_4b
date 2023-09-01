import tkinter
from tkinter import ttk
import json

with open('errores.json','r') as file:
    data = json.load(file)

def obtenerValores():
    codigo = entrada.get()  
    for error in data['Errores']:
        if error['codigo'] == codigo:
            descripcion.config(text=error['desc'])
            break
        else:
            descripcion.config(text='Descripción no encontrada')

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
                        text="Buscar codigo",
                        command= obtenerValores
                        )
btn_buscar.pack(padx=10, pady=10)

descripcion = ttk.Label(ventana,
                        text="")
descripcion.pack(padx=10,pady=10)
ventana.mainloop()
