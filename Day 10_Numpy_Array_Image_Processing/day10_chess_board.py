# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:54:19 2019

@author: BSDU ADMIN
"""


import matplotlib.pyplot as plt
import numpy as np

layout = np.array([0,1]*2048)
new = layout.reshape(64,64)

for row in [range(0,8),range(16,24),range(32,40),range(48,56)]:
    for column in [range(8,16),range(24,32),range(40,48),range(56,64)]:
        for a in row:
            for i in [range(0,8),range(16,24),range(32,40),range(48,56)]:
                for r in i:
                    new[a][r]=0
            for m in column:
                new[a][m]=1
        for a in column:
            for i in row:
                new[a][i]=1
            for m in [range(8,16),range(24,32),range(40,48),range(56,64)]:
                for e in m:
                
                    new[a][e]=0
                    
plt.imshow(new, cmap = 'gray')