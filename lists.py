#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 07:32:57 2022

@author: raj
"""

#List
shopping = ["Bread","Cofee","Sugar"]
#shopping = [] <- this creates an empty list, that means a list that has no items. Remember always add the items inside the [], followed by "" and , to seperate the items.

# print(shopping)
#  ['Bread', 'Cofee', 'Sugar'] <- to stop printing like this, we can use the 'for' loop.
# To print the number in a for loop we use range(). 
# But for lists we will simply use this syntax -> 
# for i/what_ever in list_Name:
#     print(i/what_ever)

for item in shopping:
    print(item)
