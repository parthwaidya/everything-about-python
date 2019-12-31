#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:44:04 2019

@author: appcraftz
"""

#Python sets
#Sets are unordered and unindexed collection of values

set1 = {"Mili","Mogli","Aura"}

#check if a value is present

isPresent = "Parth" in set1 #returns a boolean value

print(isPresent)

#iterate through values
for val in set1:
    print(val)
    
#add items
set1.add("Casper")

#remove item
set1.remove("Aura")

#remove last item
set1.pop()

set2 = {"Sigan","Bruno"}

#join 2 sets
set3 = set1.union(set2)