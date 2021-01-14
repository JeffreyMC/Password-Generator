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
    E1.delete(0, END)
    E1.insert(0, (password))


def copiarPass():
    if E1.get() == "":
        messagebox.showinfo("Info", "Debes generar la contraseña primero")
    else:
        root.clipboard_clear()
        root.clipboard_append(E1.get())
        messagebox.showinfo("Info", "¡¡Contraseña copiada!!")
        root.update()  # SE QUEDA EN EL PORTAPAPELES HASTA QUE SE CIERRE LA APLICACIÓN


E1 = Entry(root, bd=5)
E1.pack(side=TOP)
boton = Button(root, text="Generar Password", command=generaPassword)
boton.pack(side=BOTTOM)
btnCopiar = Button(root, text="Copiar contraseña", command=copiarPass)
btnCopiar.pack(side=BOTTOM)

root.mainloop()
