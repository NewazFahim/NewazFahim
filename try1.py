#Import Libraries

import numpy as np 
import csv
import matplotlib.pyplot as plt
import pylab
import style


#Handling value error
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
#import csv file
with open( 'try1.csv', 'r') as i:
    file01= list(csv.reader(i,delimiter=','))[2:]
    file02=[[float(k) if (isfloat(k)) else 0 for k in j] for j in file01] # Picking the values only
   
#creating mumpy array    
        
Data= np.array(file02, dtype=float)
xdata= Data[:,0][::280]
ydata= Data[:,1][::280]

#Plot
plt.figure(1,dpi=800)
plt.title('Force Spectroscopy')
plt.ylabel('Vertical Deflection')
plt.xlabel('Measured Height')
plt.style.use(['dark_background'])
plt.plot(xdata,ydata, color='green',label=('Experimental data'))

#Theoritical Plot
new= -(0.107e-5)*xdata
plt.plot(xdata,new, color= 'purple',label='Theoritical')

#Legend Modification
plt.legend('upper right',fontsize=20)
plt.legend()

    
