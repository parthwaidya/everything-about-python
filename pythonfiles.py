#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:27:10 2019

@author: appcraftz
"""

#python is one of the easiest programming languages to work on files.
#You can open / create and modify files with just a few lines of code

#There are 4 modes in which a file can be opened 1. Read, Write, Append and Create
#in addition to this, you can open the file in binary or text format

#Opening a file for reading
file = open("dogs.txt","w") #Creates the file if it does not exist
file.write("I have 2 Dogs. Mili and Mogli") #This will overwrite any existing data in the file sice it is in mode "w"
file.close() #close the file

file = open("dogs.txt","rt") #opens the file for reading in text format
print(file.read()) #reads and prints the content of the file
file.close()

file = open("dogs.txt","a") #opens the file in append mode and creates the file if it does not exists
file.write("\n and 4 cats") #will append to the existing data of the file
file.close()

#you can delete the file using remove method from os module
import os
os.remove("dogs.txt")
#additionally you can remove the folder in this way
#os.rmdir("foldername")