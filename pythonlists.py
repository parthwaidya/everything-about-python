#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 00:01:31 2019

@author: appcraftz
"""

#Lists in python
#Lists in python are like arrays. Lists are always mutable. Meaning, you can add, update and delete
#the elements in a list

list1 = ["Parth","Rahul",1,2,3,4.0]

#you can access elements like this
print(list1[2]) #indexing starts at 0

#changing an element in the list
list1[2] = "Python"

print(list1[2])

#we can iterate through lists 
for elem in list1:
    print(elem)
    
#appending an element to the end
list1.append("lastelement")
print(list1) #you can also print the list directly

print(len(list1)) #returns the length of a list