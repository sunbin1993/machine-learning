'''
Created on Apr 20, 2018

@author: eusinnb
'''

'''
    filter()也接收一个函数和一个序列。
    filter()把传入的函数依次作用于每个元素，
         然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
def is_odd(n):
    return n % 2 == 1

odd = list(filter(is_odd,[1,2,4,5,6,7,8,9]))
print("odd",odd)

'''
    埃氏筛法计算素数
'''


def main():
    for n in primes():
        if n < 1000:
            pass #print("n")
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
    
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n 
        it = filter(_not_divisible(n),it)
    
a =  _not_divisible(10)   

if __name__ == '__main__':
        main()
     

    
    
    
    
    