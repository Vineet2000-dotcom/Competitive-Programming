# -*- coding: utf-8 -*-
"""
Created on Fri May 28 17:57:56 2021

@author: Vineet
"""
try:
    t=int(input())
    while(t!=0):
        list1=[]
        s=input()
        for i in range(0,len(s)):
            if s[i] not in list1:
                list1.append(s[i])
            else:
                continue
        for i in list1:
            print(i,end="")
        print()
        t=t-1
except:
    pass
    