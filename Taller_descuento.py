# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:05:00 2020

@author: Yolanda
"""


c_llanta=int(input("Ingrese la Cantidad de llantas a comprar: "))
p_llanta=int(input("Ingrese el Precio unitario de cada llanta: "))
total_pagar=c_llanta*p_llanta
if c_llanta>4:
    desc_llanta=total_pagar * 0.10
    total_desc=total_pagar - desc_llanta
    print("Cantidad de llantas a comprar: ", c_llanta)
    print("Crecio unitario de cada llanta: ", p_llanta)
    print("Total a pagar: ", total_desc)
else:
    print("Cantidad de llantas a comprar: ", c_llanta)
    print("Crecio unitario de cada llanta: ", p_llanta)
    print("Total a pagar: ", total_pagar)
     
# Alexis Bajaña