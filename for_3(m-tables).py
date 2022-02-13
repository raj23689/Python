#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 23:17:05 2022

@author: raj
"""
#Multiplication table using a for loop

t = input("Which table do you want?")
t = int(t)
for i in range(111):
    print(t,"X",i,"=",t*i)