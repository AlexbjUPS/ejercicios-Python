# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:56:18 2020

@author: Yolanda
"""

from time import sleep
auxiliar =int()
vector=[int() for ind0 in range(29)]
print("Ingrese el tamaño del vector que sea mayor a 3 y menor que 30: ")
tamanovector=int(input())
for i in range (1,tamanovector+1):
    print("Ingrese un nombre: ")
    vector[i-1]=input()
    print("El nombre en la posicion ", i ," es ",vector[i-1])
    print("\n")
    sleep(1)
sleep(1)
for j in range (1,tamanovector+1):
    for l in range(1,tamanovector):
        if vector[l-1]>vector[l]:
            auxiliar=vector[l-1]
            vector[l-1]=vector[l]
            vector[l]=auxiliar
for k in range(1,tamanovector+1):
    print("El vector ordenado en la posicion ",k," es ", vector[k-1])
    sleep(1)