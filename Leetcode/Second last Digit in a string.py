# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:47:18 2021

@author: Vineet
"""

list1=[]
a=list(s)
for i in a:
    if i.isdigit()==True:
        b=int(i)
        list1.append(b)
    else:
        continue

c=set(list1)
d=list(c)
d.sort()
if len(d)==1:
    return -1
elif len(d)==0:
    return -1
else:
    e=d[-2]
    return e