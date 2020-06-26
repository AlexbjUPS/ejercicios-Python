# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:15:42 2020

@author: Yolanda
"""


while True:
    x=input("Ingrese un numero para contar: ")
    if x=='q' or x=='quit':
        break
    else:
        x=int(x)
        y=1
        i=0
        while True:
            print(y)
            i+=y
            y=y+1
            if y>x:
                break
print("La suma de los numeros es: ", i)