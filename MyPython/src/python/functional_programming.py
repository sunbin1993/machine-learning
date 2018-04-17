'''
Created on Apr 12, 2018

@author: eusinnb
'''

def add(x,y,f):
    return f(x) + f(y)

print(add(-5,6,abs))