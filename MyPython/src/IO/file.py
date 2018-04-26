'''
Created on Apr 23, 2018

@author: eusinnb
'''
# -*- coding: utf-8 -*-


try:
    f=open('resources/test.txt','r',encoding='utf-8')
    print(f.read())
finally:
    if f:
        f.close

with open('resources/test.txt','w') as ff:
    ff.write('Hello,World')