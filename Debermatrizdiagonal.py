# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:41:24 2020

@author: Yolanda
"""
# Alexis Bajaña

import numpy as np
import random 

print("Ingrese el numero de filas para la matriz: ")
nfila=int(input())
print("Ingrese el numero de columnas para la matriz: ")
ncolumna=int(input())
matriz=np.zeros((nfila,ncolumna))
matrizd1=np.zeros((nfila,ncolumna))
matrizd2=np.zeros((nfila,ncolumna))
contador=ncolumna-1
for fila in range(0,nfila):
    for columna in range(0,ncolumna):
        matriz[fila][columna]=random.randint(1, 99) 
        if fila == columna:
            matrizd1[fila][columna]=matriz[fila][columna]
        if columna == contador:
            matrizd2[fila][columna]=matriz[fila][columna]
    contador=contador-1
print("\n")
print(" La matriz principal es:")
print("\n")
print(matriz)
print("\n")
print(" El valor de la diagonal principal de la matriz es:")
print("\n")
print(matrizd1)
print("\n")
print(" El valor de la diagonal secundaria de la matriz es:")
print("\n")
print(matrizd2)

