# PASSWORD GENERATOR
# GENERADOR DE CONTRASEÑAS
from tkinter import *
from tkinter import messagebox

import random


root = Tk()
root.resizable(False, False)
root.title("Generador de Contraseñas")

# Obtener el ancho y alto de la ventana
anchoVentana = root.winfo_reqwidth()
altoVentana = root.winfo_reqheight()

# obtiene la mitad de las dimensiones de la pantalla y la ventana
posicionDerecha = int(root.winfo_screenwidth()/2 - anchoVentana/2)
posicionAbajo = int(root.winfo_screenheight()/2 - altoVentana/2)

# Posiciona la ventana en el centro de la pantalla
root.geometry("+{}+{}".format(posicionDerecha, posicionAbajo))

frame = Frame(root)
frame.pack()


def generaPassword():
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'
    simbolos = '[]{}%&$;._-'

    todo = minusculas + mayusculas + numeros + simbolos

    longitud = 16
    password = ''.join(random.sample(todo, longitud))
    entrada.delete(0, END)
    entrada.insert(0, (password))


def copiarPass():
    if entrada.get() == "":
        messagebox.showinfo("Info", "Debes generar la contraseña primero")
    else:
        root.clipboard_clear()
        root.clipboard_append(entrada.get())
        messagebox.showinfo("Info", "¡¡Contraseña copiada!!")
        root.update()  # SE QUEDA EN EL PORTAPAPELES HASTA QUE SE CIERRE LA APLICACIÓN


entrada = Entry(root, bd=5)
entrada.pack(side=TOP)
boton = Button(root, text="Generar Password", command=generaPassword)
boton.pack(side=BOTTOM)
btnCopiar = Button(root, text="Copiar contraseña", command=copiarPass)
btnCopiar.pack(side=BOTTOM)

root.mainloop()
