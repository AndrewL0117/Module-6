# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:41:09 2024

@author: xboxl
"""

from datetime import datetime

def feet_and_inches(feet, inches):
    datetime_object = datetime.now()
    total_inches= inches + feet * 12
    result = f"Total Inches: {total_inches} | Current DateTime: {datetime_object}"
    return result

feet_input =int(input("How many feet?"))
inches_input=int(input("How many inches?"))
#feet_input = 6
#inches_input = 2
results = feet_and_inches(feet_input, inches_input)
print(results)