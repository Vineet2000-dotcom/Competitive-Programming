# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:40:50 2021

@author: Vineet
"""

try:
    t=int(input())
    while(t!=0):
        a,b=map(int,input().split())
        c=(a/500)*100
        d=(b/500)*100
        if c>d:
            print("A")
        else:
            print("B")
        t=t-1
except:
    pass