#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:11:41 2019

@author: appcraftz
"""

#python classes

#class definition
 
class class1:
    
    #constructor
    def __init__(self): #self keyword represents the current instance of the object of the class
        self._arg = "Default Value"
        print("constructor initialised")
    
    #argumented constructor
    def __init__(self,arg):
        self._arg = arg #underscore befor variable name or functions represent private variables/functions
        
    
    #member function
    def member_function():
        print(self._arg)
        

obj = class1() #initialising class with default constructor
obj.member_function() # calling a member function

obj2 = class1("Mili") #initialising a class with argumented constructor
obj2.member_function()
    