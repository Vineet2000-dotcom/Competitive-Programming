# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:22:56 2021

@author: Vineet
"""

try:
    t=int(input())
    while(t!=0):
        a,b,x=map(int,input().split())
        c=int((b-a)/x)
        print(c)
        t=t-1
except:
    pass