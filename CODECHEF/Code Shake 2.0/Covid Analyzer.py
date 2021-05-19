# -*- coding: utf-8 -*-
"""
Created on Wed May 19 16:48:59 2021

@author: Vineet
"""
try:

    t=int(input())
    while(t!=0):
        n=int(input())
        def fibonacci(n):
         
        
            list1= [1, 2]
         
         
            for i in range(2, n+1):
                list1.append(list1[i-1] + list1[i-2])
            return list1[-2]
        print(fibonacci(n))
        t=t-1
except:
    pass