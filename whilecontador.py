# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:39:18 2020

@author: Yolanda
"""


dato=input("Ingrese el numero de veces que desea contar: ")
dato=int(dato)
contador=1
acumulador=0
while contador<=dato:
    #print(contador)
    print(contador, end=" ")
    acumulador+=contador
    contador+=1
promedio=acumulador/dato
print("La suma de los numeros es:", acumulador)
print("El promedio de los numero es: ", promedio)