# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:21:27 2021

@author: Vineet
"""

t=int(input())
while(t!=0):
    s=input().strip()
    
    if len(s)>3:
        if s[0]=="<" and s[1]=="/" and s[-1]==">":
            a=s[2:-1]
            b=list(a)
            count=0
            for i in b:
                if i.isdigit()  or i.islower():
                    count+=1
                    continue
                
            if count==len(b):
                print("Success")
            else:
                print("Error")
        else:
            print("Error")
            
    else:
        print("Error")
    t=t-1