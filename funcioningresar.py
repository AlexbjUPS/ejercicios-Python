# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:40:11 2020

@author: Yolanda
"""
def direccion(calle, sector, codigopostal, referencia, numcasa ):
    print("Su direccion es: ", "Sector: ",sector, "Calle: ",calle)
    print("Su casa es la numero: ",numcasa," El codigo postal es: ", codigopostal)
    print("Se enecuentra cerca de: ", referencia)

print("Ingrese los datos de su direccion")
calle=input("Ingrese la calle de su domicilio")
s=input("Ingrese el sector de su domicilio")
cod=input("Ingrese el codigo postal de su domicilio")
ref=input("Ingrese la referencia de su domicilio")
num=input("Ingrese el numero de su domicilio de su domicilio")
direccion(calle,s,cod,ref,num)