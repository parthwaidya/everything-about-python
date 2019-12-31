#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:36:04 2019

@author: appcraftz
"""

#python dictionary
#Dictionary is essentially a key value pair 
#each key in a dictionary has to be unique 

dict1 = {
        "name":"parth",
        "age":24,
        "occupation":"Business"
        }

print(dict1)


#retrieve a value from dictionary
age = dict1["age"]
print(age)

#change a value
dict1["age"] = 25
print(dict1)

#iterate through dictionary (print values)
for val in dict1:
    print(val)
    
#print keys and values
for key, val in dict1.items():
    print("Key" + key)
    print("val" + val)
    
#add items
dict1["BirthYear"] = 1995

#remove an item
dict1.pop("age")

#remove last item(python 3.7)
dict1.popitem() 