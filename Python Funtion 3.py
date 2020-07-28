# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:55:35 2020

@author: Yolanda
"""


def isYearLeap(year):
    if year % 4 == 0 and ((year % 100 != 0) or( year % 400 == 0)):
        return True
    else:
        return False

def daysInMonth(year, month):
    
    if isYearLeap(year)==True and month == 2:
        return 29
    elif month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    elif month in [1,3,5,7,8,10,12]: 
        return 31
    else:
        return None

def dayOfYear(year, month, day):

    diasmes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   
    if (isYearLeap(year)== False and month == 2 and day >28) or day<1 or(
            day > diasmes[month-1] or month <1 or month> 12):
        return None
    dmesanterior = 0
    for i in range(month,1,-1):
        dmesanterior += daysInMonth(year, i-1)
        
    diatotal=dmesanterior + day
    return  diatotal
    
print(dayOfYear(2000, 12, 31))
print(dayOfYear(2013, 2, 29))
print(dayOfYear(2018, 8, 17))
print(dayOfYear(2007, 2, 29))

#Alexis Bajaña