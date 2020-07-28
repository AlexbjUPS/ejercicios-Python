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
   
print(daysInMonth(2016, 13))
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30,29]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

#Alexis Bajaña