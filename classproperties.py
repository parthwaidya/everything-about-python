#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:18:22 2019

@author: appcraftz
"""

#class properties / Setters

class class1:
    
    def __init__(self,name=None,breed = None):
        self._name = name
        
    @property
    def name(self):
        return self._name
        
    @name.setter 
    def name(self,name):
        self._name = name
    
    @property
    def breed(self):
        return self._breed
        
    @breed.setter 
    def breed(self,breed):
        self._breed = breed
    

obj1=class1()

obj1.name = "Mili"
obj1.breed = "Labrador"

print(obj1.name)
print(obj1.breed)



    
    
    