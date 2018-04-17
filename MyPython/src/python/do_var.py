'''
Created on Apr 12, 2018

@author: eusinnb
'''

# 默认参数 陷阱
print("----------默认参数-----------")

def add_end(L=[]): #默认参数必须指向不变对象
    L.append('END')
    return L

print(add_end()) # ['END']
print(add_end()) # ['END', 'END']

print("用None这个不变对象来优化")
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end2())# ['END']
print(add_end2())# ['END']


#可变参数
print("----------可变参数-----------")
def calc(*numbers):
    sum = 0;
    for n in numbers:
        sum += n
    return sum
    
print(calc(1,2,3)) # 6   
    
#关键字参数
print("----------关键字参数 **  关键字参数在函数内部自动组装为一个dict-----------")

def person(name,age,**kw): #kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
    print('name：',name,'age:',age,'other:',kw)

person('Michael', 30)
person('Bob', 24,gender='M',city='Beijing',job='engineer')

extra={'city':'Beijing','job':'Engineer'}
person('Jack', 33,**extra)

# 命名关键字参数
print("----------命名关键字参数  命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。-----------")
#*不是参数，而是特殊分隔符
def person2(name, age, *, city='nantong', job):# 命名关键字参数可以有缺省值，从而简化调用
    print(name, age, city, job)

person2('Sandy', 25, job='Engineer')

person2('Jack', 24, city='Beijing', job='Engineer')

print("----------参数组合-----------")
'''
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
这5种参数都可以组合使用，除了可变参数无法和命名关键字参数混合。
但是请注意，参数定义的顺序必须是：
必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
'''

def f1(a,b,c=1,*args,**kw):
    print('a=',a,'b=','c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=1,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)


f1(1,2)
f1(1,2,3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1, 2, d=99, ext=None)











