# -*- coding: utf-8 -*-
"""
Created on Sat May 22 17:52:51 2021

@author: Vineet
"""


k,n,w=map(int,input().split())
list1=[]
for i in range(1,w+1):
    a=k*i
    list1.append(a)
b=sum(list1)
if b<=n:
    print(0)
else:
    c=b-n
    print(c)
    