'''
Created on Apr 23, 2018

@author: eusinnb
'''

class Student4(object):
    '''
    classdocs
    '''
    
    def __init__(self,name):
        self.name = name
    
    # python内置的@property装饰器就是负责把一个方法变成属性调用的
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an Integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value
    
    def __str__(self):#__str__返回用户看到的字符串，__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
        return 'Student object (name:%s)' % self.name
    
s = Student4('SunBin')
s.score = 60
print('s.score: %s'%s.score)
print(s)

#s.score = 9999