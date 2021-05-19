# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:51:32 2021

@author: Vineet
"""
for _ in range(int(input())):
    s=input()
    f=0
    for i in s:
        f=f+1+ord(i)-ord('a')
    if f%2==0:
        print("YES")
    else:
        print("NO")