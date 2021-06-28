# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:17:16 2021

@author: Vineet
"""

t=int(input())
for i in range(t):
    n=int(input())
    d1={}
    list1=[]
    for i in range(n*3):
        x,y=map(str,input().split())
        if x not in d1:
            d1[x]=int(y)
            
            
        else:
            d1[x]=d1[x]+int(y)
            
            
    x=list(d1.values())
    x.sort()
    print(*x)
    
    