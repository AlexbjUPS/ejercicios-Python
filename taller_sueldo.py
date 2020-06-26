# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:36:36 2020

@author: Yolanda
"""


hora_trabajo=int(input("Ingrese el total de horas que trabajo: "))
tarifa_hora=int(input("Ingresee el costo de la tarifa por hora: "))
descuento_hora=int(input("Ingrese el monto del descuento que se va a realizar: "))
costo_trabajo=hora_trabajo*tarifa_hora
if hora_trabajo>40:
    bonificacion=0.50
    total_bono=tarifa_hora*0.50
    bono_pagar=total_bono*(hora_trabajo-40)
    total_pagar= costo_trabajo+bono_pagar-descuento_hora
    print("El valor a pagar por las horas de trabajo mas la bonificacion del 50% es: ", total_pagar)
else:
    total_salario=costo_trabajo-descuento_hora
    print("El valor a pagar por las horas de trabajo es de: ", total_salario)

# Alexis Bajaña