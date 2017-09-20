# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:50:29 2017

@author: NeroJ
"""

import xlrd  
import numpy as np
import matplotlib.pyplot as plt
import scipy
import xlwt

top = 150
gradient = -2.29

data = xlrd.open_workbook('zero_fitting.xls')
table = data.sheets()[0] 
X = table.col_values(0)
Y = table.col_values(1)

x=np.array(X)
y=np.array(Y)
cof = np.polyfit(x,y,1) #for original data  range 0 ~ 50, 30 gets the biggest fitting level, with 
p=np.poly1d(cof)
#plt.plot(x,y,'o',label='original values')
#plt.plot(x,p(x),lw = 2,label='curve_fit values' )
#plt.xlabel('x axis')
#plt.ylabel('y axis')
#plt.legend(loc=2)
#plt.title('curve_fit')

X_zero = [] # predicted zero point set
for i in range(177, 177+50):
    X_zero.append(p(i))

for i in range(0, len(X_zero)):
    X_zero[i] = int(X_zero[i]) - int(p(177))

print X_zero


workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Worksheet')

counter = 1
save_X = []
save_Y = []
for i in range(0, len(X_zero)-1):
    temp_x = []
    for j in range(X_zero[i], X_zero[i + 1]):
        temp_x.append(j)
        save_X.append(j)
    x = np.array(temp_x)
    if counter%2 != 0:
        temp_y = []
        for item in temp_x:
            temp_y.append(0)
            save_Y.append(0)
        y = np.array(temp_y)
        
        plt.plot(x,y,'o')
        #plt.plot(x,0,lw = 2)
        plt.xlabel('x axis')
        plt.ylabel('y axis')

    else:
        temp_y = []
        b = top-gradient*temp_x[0]
        for ite in temp_x:
            temp_y.append(gradient*ite + b)
            save_Y.append(gradient*ite + b)
        y = np.array(temp_y)
        
        plt.plot(x,y,'o')
        #plt.plot(x, gradient*x + b,lw = 2)
        plt.xlabel('x axis')
        plt.ylabel('y axis')
    counter += 1

for i in range(0, len(save_X)):
    worksheet.write(i, 0, label = save_X[i] )
    worksheet.write(i, 1, label = save_Y[i])
    
workbook.save('pridicted_data.xls')