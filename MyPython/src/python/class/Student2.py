'''
Created on Apr 23, 2018

@author: eusinnb
'''

class Student2(object):
    '''
    classdocs
    '''
    pass


s =  Student2()
s.name = 'Michael' # 给实例绑定一个属性

# print(s.name)

def set_age(self,age):
    self.age=age
    
from types import MethodType

s.set_age = MethodType(set_age,s) # 给实例绑定一个方法,另一个实例不起作用
s.set_age(25)

print(s.age) 



def set_score(self, score):
    self.score = score

Student2.set_score = MethodType(set_score, Student2) # 给class绑定方法，给所有实例绑定方法


