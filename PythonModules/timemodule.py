#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:27:01 2019

@author: appcraftz
"""

import time
#A static method is created only one time for each instance of the class and can be called using class name instead of the object
class TimeModule:
    @staticmethod #we are declaring the method as static so we can call it directly using class name
    def print_time():
        print(time.time())