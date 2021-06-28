# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:22:16 2021

@author: Vineet
"""

t=int(input())
while(t!=0):
    a=input()
    if a[0]!='1':
        c="1"+a
        print(c)
    else:
        ans=a[0]+"0"+a[1:]
        print(ans)
    t=t-1