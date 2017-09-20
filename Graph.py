# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Administrator\.spyder2\.temp.py
""" 
class Point:
     def __init__(self, tag, volume, velocity):
         self.tag = tag
         self.volume = volume # the volume of the gas container(L)
         self.velocity = velocity # the velocity of cosuming gas
         self.time = 0
         self.now_volume = self.volume - self.velocity*self.time

A = Point('A', 0, 0)
B = Point('B', 500, 40)
C = Point('C', 250, 25)
D = Point('D', 400, 20)
E = Point('E', 300, 20)
F = Point('F', 300, 20)
G = Point('G', 300, 20)

dic_map = {'A':A, 'B' :B, 'C':C, 'D':D, 'E':E, 'F':F, 'G':G}

class Map:
    def __init__(self):
        self.G = {'A':{'A':0, 'B':3, 'C':1},
                  'B':{'A':3, 'B':0, 'C':2, 'E':5},
                  'C':{'A':1, 'B':2, 'C':0, 'D':2, 'E':4},
                  'D':{'C':2, 'D':0, 'F':4, 'G':10},
                  'E':{'B':5, 'C':4,'E':0, 'G':3},
                  'F':{'D':4, 'F':0, 'G':6},
                  'G':{'E':3, 'D':10, 'F':6, 'G':0}}
        self.result = []
        self.demand_alarm = ['G','C','E','F']
        self.v0 = 'A'
        self.dis = {}
        self.v1 = []     # 出发点         
        self.v2 = []     # 对应的相邻到达点
        self.w  = []     # 顶点v1到顶点v2的边的权值
        for i in self.G:
            for j in self.G[i]:
                if self.G[i][j] != 0:
                    self.w.append(self.G[i][j])
                    self.v1.append(i)
                    self.v2.append(j)
        #print self.v1
        #print self.v2
        #print self.w
    def Bellman_Ford(self, INF=999):
        self.dis = dict((k, INF) for k in self.G.keys())
        self.dis[self.v0] = 0
        for k in range(len(self.G)-1):   # 循环 n-1轮
            check = 0           # 用于标记本轮松弛中dis是否发生更新
            for i in range(len(self.w)):     # 对每条边进行一次松弛操作
                if self.dis[self.v1[i]] + self.w[i] < self.dis[self.v2[i]]:
                    self.dis[self.v2[i]] = self.dis[self.v1[i]] +self.w[i]
                    check = 1
            if check == 0:
                break
     # 检测负权回路
     # 如果在 n-1 次松弛之后，最短路径依然发生变化，则该图必然存在负权回路
        flag = 0
        for i in range(len(self.w)):             # 对每条边再尝试进行一次松弛操作
            if self.dis[self.v1[i]] + self.w[i] < self.dis[self.v2[i]]: 
                flag = 1
                break
        if flag == 1:
            return False
        #print self.dis    
    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not self.G.has_key(start):
            return []
        paths = []
        for node in self.G[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    def give_shortest_path(self, end,shortest = [], d = {}):
        for item in shortest:
            vote = 0
            for i in range(len(item)):
                if i == len(item) - 1:
                    break;
                vote += self.G[item[i]][item[i+1]]
            if vote == d[end]:
                return item
    def ShortestPath(self, start, end, d =[]):
        self.v0 = start
        self.Bellman_Ford()
        result = self.find_all_paths(start, end)
        #print result
        #print self.give_shortest_path(end, result, self.dis)
        return self.give_shortest_path(end, result, self.dis)
    def best_logic(self, dis):
        road = []
        point_begin = 'A'        
        while True:
            point_over = self.demand_alarm[0]
            self.demand_alarm.remove(point_over)
            temp = self.ShortestPath(point_begin, point_over, dis)
            point_begin = point_over
            road.append(temp)
            if len(self.demand_alarm) == 0:
                break
            else:
                for item in temp:
                    if item in self.demand_alarm:
                        self.demand_alarm.remove(item)
            if len(self.demand_alarm) == 0:
                break
        return road
a = Map()
print a.best_logic(a.dis)

    
    

    



        

