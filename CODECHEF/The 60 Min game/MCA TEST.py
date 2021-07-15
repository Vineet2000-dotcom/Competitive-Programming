# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 19:30:56 2021

@author: Vineet
"""

t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    a=r-l
    if a==1:
        print("FAIL")
    else:
        list1=[]
        for i in range(l,r+1):
            if i%2==0:
                list1.append(i)
            else:
                continue
        if len(list1)%2==0:
            print("PASS")
        else:
            print("FAIL")
        
        