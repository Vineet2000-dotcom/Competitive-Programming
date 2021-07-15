# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 19:51:18 2021

@author: Vineet
"""

t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    list1.sort()
    sum1=0
    count=0
    for i in list1:
        sum1=sum1+i
        if sum1<=60:
            count+=1
        else:
            break
    print(count)
            
    