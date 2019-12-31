#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:23:53 2019

@author: appcraftz
"""

#Tuples in python
#Tuples in python are like Lists but are immutable. Meaning, you cannot add, update and delete
#the elements in a list

tuple1 = ("Parth","Rahul",1,2,3,4.0)

#you can access elements like this
print(tuple1[2]) #indexing starts at 0


#we can iterate through lists 
for elem in tuple1:
    print(elem)

#you can print length of a tuple using len
print(len(tuple1))