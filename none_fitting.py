# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Administrator\.spyder2\.temp.py
""" 
import xlrd 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math


class FittingPolynome:
    def __init__(self):
        self.data = xlrd.open_workbook('F1.xls')
        self.table = self.data.sheets()[0] 
        self.X11_12 = self.table.col_values(0)
        self.Y11_12= self.table.col_values(1)
        self.counter_0 = 0 #number of zero points
        self.X = [] #remove zero points
        self.Y = []
        self.Y11_12_aver = [] #cope with averages
        self.Y11_12_MaxMin = [] #Max,Min
        self.func = 0 #fitting function
        self.RR = 0 #fitting level
        self.Y_day = []
        self.X_day = []
        self.popt = [] #sin fit a, b, c
        for i in range(0, len(self.Y11_12)):
            if self.Y11_12[i] != 0:
                self.Y.append(self.Y11_12[i])
                self.X.append(self.X11_12[i])
                self.counter_0+=1
                
    def PreDeal(self):
        num = 0
        counter = 1
        for i in range(0, len(self.Y11_12)):
            num = num + self.Y11_12[i]
            if (i + 1) % 168 == 0:
                self.Y_day.append(num / 22.0)
                num = 0
                self.X_day.append(counter)
                counter += 1
                
                
    def Average(self):
        aver = np.average(self.Y11_12)
        Y11_12_aver = []
        for item in self.Y11_12:
            x = item - aver
            Y11_12_aver.append(x)
        self.Y11_12_aver = Y11_12_aver
        return Y11_12_aver
    
    def R2(self):
        RSS = 0
        TSS = 0
        RR = 0
        aver = np.average(self.Y11_12)
        #print aver
        for i in range(0, len(self.Y11_12)):
            RSS = RSS + np.square(self.Y11_12[i] - self.func(self.X11_12[i]))
            TSS = TSS + np.square(self.Y11_12[i] -aver)
        RR = 1- (RSS/TSS)
        self.RR = RR
    
    def R2_sin(self):
        RSS = 0
        TSS = 0
        RR = 0
        aver = np.average(self.Y11_12)
        for i in range(0, len(self.Y11_12)):
            RSS = RSS + np.square(self.Y11_12[i] - (self.popt[0]*np.sin(self.popt[1]*self.X11_12[i])+self.popt[2]))
            TSS = TSS + np.square(self.Y11_12[i] -aver)
        RR = 1- (RSS/TSS)
        self.RR = RR
        
    def Fit_Origin(self):
        x=np.array(self.X11_12)
        y=np.array(self.Y11_12)
        cof = np.polyfit(x,y,10) #for original data  range 0 ~ 50, 30 gets the biggest fitting level, with 
        p=np.poly1d(cof)
        plt.plot(x,y,'o',label='original values')
        plt.plot(x,p(x),lw = 2,label='curve_fit values' )
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.legend(loc=2)
        plt.title('curve_fit')
        #print(cof)
        self.func = p
        
    def Fit_Zero(self):
        x=np.array(self.X)
        y=np.array(self.Y)
        cof = np.polyfit(x,y,21) #for data been removed with 0: range 0 ~ 50, 21 gets the biggest fitting level, with 
        p=np.poly1d(cof)
        plt.plot(x,y,'o',x,p(x),lw=2)
        print(cof)
        self.func = p
    
    def fit_sin(self):
        x=np.array(self.X11_12)
        y=np.array(self.Y11_12)
        def func(x,a,b,c):
            return a*np.sin(b*x) + c
        popt, pcov = curve_fit(func, x, y)
        a=popt[0]
        b=popt[1]
        c=popt[2]
        yvals=func(x,-4.6,b,c)
        plot1=plt.plot(x, y, '*',label='original values')
        plot2=plt.plot(x, yvals, 'r',label='curve_fit values')
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.legend(loc=1)
        plt.title('curve_fit')
        plt.show()
        self.popt = popt
        print popt
        return popt
          
a = FittingPolynome()
a.fit_sin()
#a.Fit_Origin()
#a.R2()
a.R2_sin()
print a.RR






    









        

