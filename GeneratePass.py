# PASSWORD GENERATOR
# GENERADOR DE CONTRASEÑAS

import random

minusculas = 'abcdefghijklmnopqrstuvwxyz'
mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '[]{}%&$;._-'

todo = minusculas + mayusculas + numeros + simbolos

longitud = 16
password = ''.join(random.sample(todo, longitud))

print('El password es: ', password)
