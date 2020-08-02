# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:51:36 2020

@author: Yolanda
"""

#Alexis Bajaña
costobyn = 0.06
costocol = 0.12  
print("Ingrese el valor inicial de las copias ")
vinicial = int(input())
print("Ingrese el valor final de las impresiones")	
vfinal = int(input())
if vfinal > vinicial:
    print("Si la impresion fue en blanco y negro digite 1")
    print("si la impresion fue a color digite 2")
    byn = int(input())
    if byn ==1:
        numimp=vfinal-vinicial
        costoimp = numimp*costobyn
        print("El total de impresiones es ",numimp)
        print("El costo total de la impresion es","{0:.2f}".format(costoimp))
    elif byn ==2:
         numimp=vfinal-vinicial
         costoimp = numimp*costocol
         print("El costo total de la impresion es","{0:.2f}".format(costoimp))
else:
    print("Error el valor final es mayor que el inicial")
        