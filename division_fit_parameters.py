# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Administrator\.spyder2\.temp.py
""" 
import xlrd  
import numpy as np
import matplotlib.pyplot as plt
import scipy
import math

consequent_num = 100 #consequent num, smaller, more divisions
division_num = 1.2 # larger, the smaller the difference between aver and Y[i], this is the parameter
data = xlrd.open_workbook('F2.xls')
table = data.sheets()[0] 
X11_12 = table.col_values(0)
Y11_12= table.col_values(1)
aver = np.average(Y11_12)

RSS = 0
TSS = 0
RR = 0

def division(Y):
    break_point = [] #[point, counter]
    index_point = [0] #all breakpoints index
    bp = []
    flag = 0
    counter = 0
    point = 0
    for i in range(0, len(Y)):
        if abs(Y[i] - aver)*division_num  >= aver:
            flag = 1
            counter += 1
            if counter == 1:
                point = i
        else:
            flag = 0
            if counter >= consequent_num: #100: the smallest number of consequent zeros, this is we defined
               bp.append(point)
               bp.append(counter)
               break_point.append(bp)
               index_point.append(point)
               index_point.append(point + counter)
            counter = 0
            point = 1
            bp = []
    index_point.append(len(Y))
    return index_point

r = division(Y11_12)
print division(Y11_12)

for i in range(0, len(r)-1):
    x=np.array(X11_12[r[i] : r[i + 1]])
    y=np.array(Y11_12[r[i] : r[i + 1]])
#####################################################    
    cof = np.polyfit(x,y,3) #for original data  range 0 ~ 50, 30 gets the biggest fitting level, with 
    p=np.poly1d(cof)
    plt.plot(x,y,'o')
    plt.plot(x,p(x),lw = 2)
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.legend(loc=2)
    plt.title('curve_fit')
    for k in range(0, len(y)):
        RSS = RSS + np.square(y[k] - p(x[k]))
        TSS = TSS + np.square(y[k] -aver)

RR = 1- (RSS/TSS)
print RR

    

            

#x=np.array(X11_12)
#y=np.array(Y11_12)
#plt.plot(x,y)
#plt.show()
        

