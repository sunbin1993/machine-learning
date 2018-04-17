'''
Created on Apr 3, 2018

@author: eusinnb
'''
counter = 100         #整形变量
miles = 100.0          #浮点型变量
name = "runoob"   #字符串

print(counter)
print(miles)
print(name)


'''
    标准数据类型
'''
print("------------标准数据类型-------------")
a,b,c,d = 20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))
a=111
print(isinstance(a, int))

print("------------list列表  [] -------------")
list = ['abcd',786,2.22,'runoob',70.2]
tinylist = [123,'runoob']

listb = list[:]
print(listb)

print (list)
print (list[0])
print (list[1:3])
print (list[2:])
print (list * 2)
print (list + tinylist)

print("------------列表中元素可以改变 有序-------------")

a = [1,2,3,4,5,6]
a[0] = 9
a[2:5] = [13,14,15]
print(a)

print("------------Tuple元组 有序 () 比list更安全  -------------")
tup = ()
tuple = (1,)# 一个元素的tuple 定义是必须加 “,  ”以免产生歧义
print(tuple)

print("------------set集合  无序不重复 -------------")
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)

#成员测试

if('Rose' in student):
    print('Rose in set')
elif('Tom' in student):
    print('Tom in set')
else:
    print('Rose and Tom are not in set')    

#set进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
    
print("------------Dictionary {}字典是无序的对象集合-------------")
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {"name":"sunbin","age":25,"aaa":11}
print(dict['one'])
print(dict[2])
print(tinydict.keys())
print(tinydict.values())


