#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 17:06:38 2019

@author: appcraftz
"""

#If else 

x = 0

if x == 0:
    print("x is 0")
else:
    print("x is not 0")
    
#if elif

y =6

if y>3:
    print("Y greater than 3")
elif y==3:
    print("Y is equal to 3")
else:
    print("No condition satisfied")
    
#nested if else
a , b = 3,2

if a==3:
    if b==2:
        print("A is 3 and B is 2")
else:
    print("No condition satisfied")
    
#we can also write the above condition as

if a==3 and b==2:
    print("A is 3 and B is 2")
else:
    print("No condition satisfied")
    
    