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
import xlwt

consequent_num = 10 #consequent zero num, smaller, more divisions

RSS = 0
TSS = 0
RR = 0

gradient = []
aver_gradient = 0

data = xlrd.open_workbook('F2.xls')
table = data.sheets()[0] 
X11_12 = table.col_values(0)
Y11_12= table.col_values(1)

aver = np.average(Y11_12)

def division(Y):
    break_point = [] #[point, counter]
    index_point = [0] #all breakpoints index
    bp = []
    flag = 0
    counter = 0
    point = 0
    for i in range(0, len(Y)):
        if Y[i] == 0:
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
r_copy = r
#print division(Y11_12)

for i in range(0, len(r)-1):
    x=np.array(X11_12[r[i] : r[i + 1]])
    y=np.array(Y11_12[r[i] : r[i + 1]])
    if y[0] == 0:
        cof = np.polyfit(x,y,1) #for original data  range 0 ~ 50, 30 gets the biggest fitting level, with 
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
    else:
        cof = np.polyfit(x,y,1) #for original data  range 0 ~ 50, 30 gets the biggest fitting level, with 
        p=np.poly1d(cof)
        gradient.append(cof[0])
        plt.plot(x,y,'o')
        plt.plot(x,p(x),lw = 2)
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.legend(loc=2)
        plt.title('curve_fit')
        for l in range(0, len(y)):
            RSS = RSS + np.square(y[l] - p(x[l]))
            TSS = TSS + np.square(y[l] -aver)


aver_gradient = np.average(gradient)
print aver_gradient
RR = 1- (RSS/TSS)
print RR

###############################################################################################################################
print r_copy
x_zero = []
counter = 0
for item in r_copy:
    x_zero.append(counter)
    counter += 1

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Worksheet')
for i in range(0, len(r_copy)):
    worksheet.write(i, 0, label = x_zero[i] )
    worksheet.write(i, 1, label = r_copy[i])
    
workbook.save('zero_fitting.xls')
       

#x=np.array(X11_12)
#y=np.array(Y11_12)
#plt.plot(x,y)
#plt.show()
        

