# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 09:56:22 2021

@author: Vineet
"""

n,m=map(int,input().split())
list1=list(map(int,input().split()[:n]))


list2=[]
for i in list1:
    if i<0 :
        list2.append(abs(i))
    else:
        continue
if len(list2)==0:
    print(0)
else:
    list2.sort()
    a=list2[::-1]
    b=a[0:m]
    print(sum(b))
            
