

def consumer():
    r = ''
    while True:
        print('11111')
        n = yield r
        print("r="+r)
        
        if not n:
            return
        print('[CONSUMER] consuming %s...' %n)
        r = 'OK'
        
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' %n)
        r = c.send(n)
        print('[PRODUCER] Consumer return : %s' %n)
    c.close()
    
c = consumer()
print('============')
produce(c)