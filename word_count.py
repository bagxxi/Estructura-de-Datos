import sys
import os

archivo = sys.argv[1]

print(archivo)

with open(f'{archivo}', 'r') as file:
    texto = file.read()  #leyendo el archivo
    letras = set(texto)

    sin_cosas = texto.strip(',.\n')   #quitando comas y puntos
    separado = sin_cosas.split(' ')
    #separando palabras
    nuevo_set = set(separado)
    #eliminando palabras repetidas

    print(f'CONTADOR DE PALABRAS'.center(55, "="), end='\n\n')
    print(f'El número de palabras distintas es : {len(nuevo_set)} \n'.center(53, " "))
    print(f'El número de letras distintas es : {len(letras)} \n'.center(55, " "))
    print(f'Hay un total de {len(separado)} palabras en el archivo\n'.center(55, " "))
    print("="*55)