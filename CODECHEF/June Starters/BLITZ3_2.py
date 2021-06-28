# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:18:33 2021

@author: Vineet
"""

t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    s=2*(180+n)
    t=a+b
    u=s-t
    print(u)