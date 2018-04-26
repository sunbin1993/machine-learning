'''
Created on Apr 23, 2018

@author: eusinnb
'''

class Student(object):
    '''
    classdocs
    '''


    def __init__(self, name,score):
        '''
        Constructor
        '''
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' %(self.__name,self.__score))
        
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)

bart.print_score()

print(bart._Student__score)
print(bart._Student__name)
