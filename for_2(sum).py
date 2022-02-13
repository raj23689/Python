#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 22:39:16 2022

@author: raj
"""

answer = 0
for i in range(10):
    #answer += i
    answer = answer + i
print(answer)

n = input("Enter the range")
d = int(n)
ans = 0
for i in range(0,d):
    ans = ans + i
print(ans)