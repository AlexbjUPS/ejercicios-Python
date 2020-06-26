# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:27:40 2020

@author: Yolanda
"""


nombre=input("Ingrese su nombre: " )
apellido=input("Ingrese su apellido: " )
ubicacion=input("Ingrese su ubicacion: " )
edad=int (input("Ingrese su edad: " ))
espacio=" "
print( "Ha sido una larga busqueda, sin embargo porfin sabemos quien eres, la ubicacion: " + ubicacion+espacio+ "no es tu verdadera ubicacion, y tus datos seran revelados mi estimado: "+nombre+espacio+apellido+ "a tu edad de: " ,edad,espacio+"años")

if edad <=1 and edad >=0:
    print("Usted todavia es un bebe" ) 
elif edad >=2 and edad <= 11:
    print("Usted todavia es un niño" ) 
elif edad >=12 and edad <= 17:
    print("Usted todavia es un adolescente" )
elif edad >=18 and edad <= 50:
    print("Usted todavia es un adulto" )
elif edad >=51 and edad <=110:
    print("Usted todavia es un viejo" )  
else:
    print("Edad no valida" )