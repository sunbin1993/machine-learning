'''
Created on Apr 23, 2018

@author: eusinnb
'''

class Animal(object):
    '''
    classdocs
    '''

    def run(self):
        print('Animal is running...')
        

        
        
class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()



print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
        
        
def run_twice(animal):
    animal.run()
    animal.run()

# file-like object
class Timer(object):
    def run(self):
        print('Start...')
        
        
        
run_twice(Timer())