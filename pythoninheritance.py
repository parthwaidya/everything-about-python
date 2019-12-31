#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:28:00 2019

@author: appcraftz
"""

#python inheritance

class class1:
    def __init__(self,age=None):
        self._age = age
    
class class2(class1):
    def __init__(self,name = None,breed = None,age = None):
        super.__init__(age)
        self._name = name
        self._breed = breed
        self._age = age
    
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
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        self._age = age
        
obj1 = class2()
obj1.name = "Mogli"
obj1.age = 3
obj1.breed = "Labrador"

print("Name {0} Age {1} Breed {2}",obj1.name,obj1.age,obj1.breed)
    