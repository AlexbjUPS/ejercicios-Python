# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:05:44 2020

@author: Yolanda
"""


dato=input("Ingrese el numero de veces que desea contar: ")
dato=int(dato)
contador=1
acumulador=0
while True :
    print(contador)
    contador+=1
    if contador>dato:
        break