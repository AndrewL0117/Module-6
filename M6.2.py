# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:06:38 2024

@author: xboxl
"""

from datetime import datetime
from datetime import timedelta

# Current time
current_datetime = datetime.now()
print("Current datetime:", current_datetime)

# +1 Day
print("+1 Day:", datetime.now() + timedelta(days=1))

# -60 Seconds
datetime_60_sec = current_datetime + timedelta(seconds=-60)
print("-60 Seconds", datetime_60_sec)

# +2 Years
datetime_2_years = current_datetime + timedelta(days=365*2)
print("+2 Years:", datetime_2_years)
