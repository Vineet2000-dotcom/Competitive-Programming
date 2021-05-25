# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:07:52 2021


@author: Vineet
"""
from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase

try:
    n=int(input())
    list1=list(map(int,input().split()))
    count=0
    for i in range(0,len(list1)):
        if list1[i]==0:
            list1[i]=1
            count+=1
            
            for j in range(i+1,len(list1)):
                if list1[j]==0:
                    list1[j]=1
                    
                    
                else:
                    list1[j]=0
                    
                
                    
                   
        else:
            continue
    print(count)
except:
    pass