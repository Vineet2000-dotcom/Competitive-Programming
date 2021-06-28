# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:19:09 2021

@author: Vineet
"""

t=int(input())
while(t!=0):
    a,b,c,d=map(int,input().split())
    if a+c==180 and b+d==180 and a+b+c+d==360:
        print("Yes")
    else:
        print("No")
    t=t-1