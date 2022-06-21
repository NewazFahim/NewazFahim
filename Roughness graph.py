# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 00:38:30 2022

@author: Fahim
"""


import numpy as np 
import csv
import matplotlib.pyplot as plt
import pylab
import style

with open( '1d.csv', 'r') as i:
    file01= list(csv.reader(i,delimiter=','))
    file02= file01[3:]

data= np.array(file02, dtype=float)
xdata= data[:,0]
ydata= data[:,1]

plt.figure(1,dpi=800)
plt.title('Roughness of A5')
plt.plot(xdata, ydata, color='purple', label='Experimental data')
plt.ticklabel_format(style='sci', axis='x', scilimits=(-6,-6))
plt.ticklabel_format(style='sci', axis='y', scilimits=(-9,-9))
plt.legend("upper right",fontsize=20)
plt.grid('grid_dashes')
plt.legend()
