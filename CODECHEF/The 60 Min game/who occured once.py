# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 09:58:58 2021

@author: Vineet
"""

t=int(input())
for _ in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    for i in list1:
        if list1.count(i)==1:
            if i%2==1:
                print("PASS")
            else:
                print("FAIL")
        else:
            continue
    
            