# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:08:24 2019

@author: BSDU
"""

time= float(input('Enter time worked: '))
sallery = float(input('Enter dollars paid time:'))
if time <= 40:
    totalsallery = sallery*time
else:
    overtime = time - 40
    totalsallery = sallery*overtime
print('sallery for time are' ,totalsallery)
    
