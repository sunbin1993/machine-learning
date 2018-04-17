'''
Created on Apr 12, 2018

@author: eusinnb
'''
# -*- coding: utf-8 -*-
print("递归函数")

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))