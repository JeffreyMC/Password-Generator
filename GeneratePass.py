# PASSWORD GENERATOR
# GENERADOR DE CONTRASEÑAS
from tkinter import *
from tkinter import messagebox

import random


root = Tk()
root.geometry("200x100")
root.resizable(False, False)
root.title("Generador de Contraseñas")
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
