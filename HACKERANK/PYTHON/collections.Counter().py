# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:49:27 2021

@author: Vineet
"""

from collections import Counter
x=int(input())
list1 = list(map(int, input().split()[:x]))
a=Counter(list1)
b=a.values()
cost=[]
sc=[]
n=int(input())
count=0
for i in range(0,n):
    s,price=map(int,input().split())
    if s in list1:
        sc.append(s)
        count=sc.count(s)
        value1=a.get(s)
        if count<=value1:
            cost.append(price)
        else:
            continue
    else:
        continue

amount=sum(cost)
print(amount)            
    