'''
Created on Apr 25, 2018

@author: eusinnb
'''
import threading



local_shcool = threading.local()

def process_thread(name):
    local_shcool.student = name
    process_student()
    
def process_student():
    std = local_shcool.student
    print('Hello,%s (in %s)' % (std,threading.current_thread().name))
    
t1 = threading.Thread(target=process_thread,args=('Alice',))
t2 = threading.Thread(target=process_thread,args=('Bob',))

t1.start()
t2.start()

t1.join()
t2.join()