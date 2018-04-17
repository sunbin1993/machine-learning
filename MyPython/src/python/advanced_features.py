'''
Created on Apr 12, 2018

@author: eusinnb
'''

L=['Michael','Sarah','Tracy','Bob','Jack']
print("取指定索引范围的操作用切片")
print(L[0:3])# print(L[:3])

print("迭代")
for i,value in enumerate(['A','B','C']):
    print(i,value)
print("迭代-同时引用两个变量")    
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)
    
print("列表生成式 ",end="")
print([x*x for x in range(1,11)])
print([m+n for m in 'ABC' for n in 'abc'])

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [x for x in L1 if isinstance(x, str)]
print("L2=",L2)


print("边循环边计算的机制  生成器：generator")

g = (x * x for x in range(10))

for n in g:
    print("n ",n)

print("--------斐波拉契数列--------")
print("--------while循环实现--------")

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print("b",b)
        a,b = b,a + b
        n += 1
    return 'done'

fib(6)

print("--------while循环 yield--------")

def fib2(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1
    return 'done'

print(fib2(6))
for n in fib2(6):
    print(n)













































