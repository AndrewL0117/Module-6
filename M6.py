# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:23:15 2024

@author: xboxl
"""


import sys
for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print("{0}\t{1}".format(item, cost))