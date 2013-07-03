import threading
from threading import Thread

def f1():
    print("N1")

def f2():
    print("N2")

if (__name__=='__main__'):
    Thread(target =f1).start()
    Thread(target =f2).start()

##http://stackoverflow.com/questions/2957116/make-2-functions-run-at-the-same-time            
