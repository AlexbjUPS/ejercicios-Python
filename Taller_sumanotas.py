# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:25:06 2020

@author: Yolanda
"""


nota_1=int(input("Ingrese la nota de la evaluacion 1: "))
nota_2=int(input("Ingrese la nota de la evaluacion 2: "))
nota_3=int(input("Ingrese la nota de la evaluacion 3: "))

if nota_1>nota_2  and nota_2>nota_3:
    suma_total1= nota_1+nota_2
    print("Su nota total es: ", suma_total1)
else:
    if nota_2>nota_1  and nota_2>nota_3:
        suma_total2= nota_1+nota_2
        print("Su nota total es: ", suma_total2)
    else:
        if nota_1>nota_2 and nota_3>nota_2:
            suma_total3= nota_1+nota_3
            print("Su nota total es: ", suma_total3)
        else:
            suma_total4= nota_2+nota_3
            print("Su nota total es: ", suma_total4)

# Alexis Bajaña