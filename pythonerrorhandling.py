#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:51:11 2019

@author: appcraftz
"""

#Python provides a robust exception handling mechanism
#the try except and finally blocks (except is equal to catch in other languages)

x = "Mogli"

try:
    print(x) #try to print x
except NameError: #if a name error is generated 
    print("x not defined") #print that x is not defined
else: #Else block is executed if no error is caught
    print("No error occured") #print a message if no error has occured
finally: #this block will execute regardless of whether an error occurs or not
    print("Thank you")
    
#lets try it with an undefined variable
try:
    print(y) #try to print y (this will raise an error)
except NameError: #if a name error is generated 
    print("x not defined") #print that x is not defined
else: #Else block is executed if no error is caught
    print("No error occured") #print a message if no error has occured
finally: #this block will execute regardless of whether an error occurs or not
    print("Thank you")
    
#you can also raise custom exceptions
try:
    print(x)
    if(x!="Mili"):
        raise("X is not mili")