'''
Created on Apr 23, 2018

@author: eusinnb
'''

class Student3(object):
    '''
    classdocs
    '''
    
    __slots__ = ('name','age') #用、tuple定义允许绑定的属性名称


    def __init__(self):
        '''
        Constructor
        '''
s = Student3() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
#s.score = 99 # 绑定属性'score'        


# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student3):
    pass



g = GraduateStudent()
g.score = 9999