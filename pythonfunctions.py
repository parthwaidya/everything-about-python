#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:51:47 2019

@author: appcraftz
"""

#Functions in python
#Simple function definition

def print_something():
    print("Hola world")
print_something()

#You can pass arguments to a function

def print_something(arg1):
    print(arg1)
    
print_something("Mili")

#multiple arguments

def print_something(arg1,arg2):
    print(arg1)
    print(arg2)
    
print_something("Mili","Mogli")

#if you dont know how many arguments are going to be passed, you can
#pass arbitary arguments

def print_something_arbitary(*args):
    for val in args:
        print(val)
        
print_something_arbitary("Mili","Mogli","Bruno")

#if you want to follow the sequence for argument passing, you can use
#argument keywords to pass values instead
print_something(arg2="Mili",arg1="Mogli") #note the sequence. This will call the function on line 25


