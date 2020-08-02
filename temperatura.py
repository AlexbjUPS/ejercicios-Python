# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:17:11 2020

@author: Yolanda
"""
contador1=0
contador2=0
solido=0
liquido=0
gaseoso=0
sumac=0
sumaf=0
pcenti=0
pfaren=0
print("Ingrese cantidad de temperaturas a ingresar entre 1 y 10: ")
ctemp=int(input())
if ctemp >=1 and ctemp<=10:
    for i in range (ctemp):
        contador1=contador1+1
        print("Ingrese la temperatura ", contador1, " en °C: ")
        tcent=int(input())
        farenheit=(tcent*(9/5))+32
        sumac=sumac+tcent
        sumaf=sumaf+farenheit
       
        if tcent<=0:
            solido=solido+1   
        elif tcent >=0 and tcent<100:
            liquido=liquido+1
        elif tcent >=100:
            gaseoso=gaseoso+1
    pcenti=sumac/ctemp
    pfaren=sumaf/ctemp
    print("\n")
    print("----RESUMEN DEL ANÁLISIS DE MUESTRAS DE AGUA----")
    print("Cantidad de muestras sólidas: ",solido)     
    print("Cantidad de muestras liquidas: ",liquido)
    print("Cantidad de muestras gasesosas: ",gaseoso)
    print("Temperatura Promedio °C: ","{0:.2f}".format(pcenti))
    print("Temperatura Promedio °F:","{0:.2f}".format(pfaren))
else:
    print("El numero ingresado no es el correcto")


