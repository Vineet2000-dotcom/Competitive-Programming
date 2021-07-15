# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 19:42:17 2021

@author: Vineet
"""

t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    if n<5:
        print(-1)
    else:
        list1.sort()
        a=list1[-5]
        print(a)
        