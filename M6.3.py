# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:15:41 2024

@author: xboxl
"""

from datetime import timedelta

d = timedelta(days=100, hours=10, minutes=13)
print(d)

print((d.days, d.seconds, d.microseconds))