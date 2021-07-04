# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 18:43:53 2021

@author: Vineet
"""

t=int(input())
while(t!=0):
    n=int(input())
    list1=list(map(int,input().split()))
    count=0
    even=[]
    odd=[]
    for i in range(0,len(list1)):
        if list1[i]%2==0:
           
            even.append(list1[i])
        else:
            odd.append(list1[i])
        
    
    if len(even)==len(odd):
        print("Yes")
    else:
        if len(odd)>len(even):
            if len(even)==n:
                print("Yes")
            else:
                print("No")
        else:
            if len(odd)==n:
                print("Yes")
            else:
                print("No")
    
    t=t-1