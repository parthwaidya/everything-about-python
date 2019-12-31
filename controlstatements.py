#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 23:36:29 2019

@author: appcraftz
"""

#control statements in loops

x = [0,1,2,3] #A list (arrays in other languages)

for num in x: #iteration through a list
    if not num:
        pass #pass statement does nothing
    print(num) #will print 0,1,2,3
    
for num in x: #iteration through a list
    if not num:
        continue #will skip the next statements for current loop and continue to the next iteration
    print(num) #will print 1,2,3 since 0 is equal to false
    
for num in x: #iteration through a list
    if not num:
        break #break the loop entirely
    print(num) #will print nothing since the first condition will return false i.e 0
    

    