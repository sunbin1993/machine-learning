'''
Created on Apr 12, 2018

@author: eusinnb
'''
from _functools import reduce

print("---------map---------")
def f(x):
    return x * x

m = map(f,[1,2,3,4,5,6,7,8,9])
print(m)
print(list(m))

print("---------reduce---------")
def add(x,y):#必须接收两个参数
    return x + y

r=reduce(add,[1,3,5,7,9])
print(r)
print("---------map reduce---------")

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,"8":8,'9':9}[s]

def fn(x,y):
    return x*10 + y

mm=map(char2num,'13579')
print(list(mm))
rr = reduce(fn, map(char2num,'13579'))
print(rr)