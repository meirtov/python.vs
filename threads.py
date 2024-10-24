from threading import Thread
counter=0
def add():
    global counter
    for i in range(100000):
        counter=counter+1
def min():
    global counter
    for i in range(100000):
        counter=counter-1
    
t1=Thread(target=add)
t2=Thread(target=min)
t1.start
t2.start
