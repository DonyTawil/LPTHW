##Final part of the game Arithmetic
#Use thread
#Now for first step of the game what am I going to do?
#Under construction

import threading
import time
from threading import Thread as thread



class math(object):
    def __init__(self):
        self.dice={"m1":1,"m2":2}
        print("You must get 8 out of 10 correct")

    def time(self,step):
        boom=5
        while (boom>0):
            time.sleep(step)
            boom-=1
        exit    

    def m1(self):
        print("55*11=?")
        x=605    
        answ=input(">")
        if (int(answ)==x):
            return "m2"
    
    def play(self):
        next="m1"
        step=self.dice[next]
        timer=getattr(self,"time")(step)
        print(next)
        test=getattr(self,next)
        thread(target=test).start()
        thread(target=timer).start()
        

a=math()
a.play()
               
