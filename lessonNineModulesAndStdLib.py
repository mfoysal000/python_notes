# Lesson 9 Modules and STD lib

print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1

#This whole thing is a module^ in a different .py file okay call it my_module.py

#Another .py file where we want to use this module

import my_module              #need this line to import a module...you can type "as" right after it and a nickname for short hand like
                                    #import my_module as mm
                                    #you can import snippets by typing 'from my_module import function, variable, etc.'

courses = ['History', 'Math', 'English']    #the to_search argument parameter

index = my_module.find_index(courses, 'Math')   #the function from the module in motion...you need to type the module first then the function
print(index)                                    #can type mm.find_index if you put short hand when importing


import math
import calendar
import os
#common modules found in std library to help you do some common functions that are well established like in math its radions = math.radion(sin(90))
