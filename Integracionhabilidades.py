# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:45:15 2020

@author: Yolanda
"""
#Alexis Bajaña
from random import randint
from time import sleep
while True:
    auxiliar =int()
    vector=[int() for ind0 in range(29)]
    print("Ingrese el tamaño del vector que sea mayor a 3 y menor que 30: ")
    tamanovector=int(input())
    if tamanovector>3 and tamanovector<30:
        print("Digite la opcion con la que desea trabajar en el programa: ")
        print("1. Con numeros")
        print("2. Con Caracteres")
        opc1=int(input())
        if opc1 == 1:
            for i in range (1,tamanovector+1):
                vector[i-1]=randint(0,99)
                print("El valor en la posicion ", i ," es ",vector[i-1])
                sleep(1)
            sleep(1)
            
        elif opc1==2:
            for i in range (1,tamanovector+1):
                print("\n")
                print("Ingrese el nombre ", i,":")
                vector[i-1]=input()
                print("El nombre en la posicion ", i ," es ",vector[i-1])
                sleep(1)
            sleep(1)

        print("\n")
        print("Digite la opcion con la que desea ordenar el programa: ")
        print("1. De menor a mayor")
        print("2. De mayor a menor")    
        opc2=int(input())
        if opc2==1:    
            for j in range (1,tamanovector+1):
                for l in range(1,tamanovector):
                    if vector[l-1]>vector[l]:
                        auxiliar=vector[l-1]
                        vector[l-1]=vector[l]
                        vector[l]=auxiliar
            for k in range(1,tamanovector+1):
                print("El vector ordenado en la posicion ",k," es ", vector[k-1])
                sleep(1)
        elif opc2==2:
            for j in range (1,tamanovector+1):
                for l in range(1,tamanovector):
                    if vector[l-1]<vector[l]:
                        auxiliar=vector[l-1]
                        vector[l-1]=vector[l]
                        vector[l]=auxiliar
            for k in range(1,tamanovector+1):
                print("El vector ordenado en la posicion ",k," es ", vector[k-1])
                sleep(1)
     
    else:
        print("\n")
        print("El numero ingresado no es el correcto")
        
    print("\n")
    print("si desea continuar con el programa digite SI ")
    print("Si desea finalizar el programa presione cualquier tecla")
    finpr=input()
    if finpr.upper() != "SI":
        break
    