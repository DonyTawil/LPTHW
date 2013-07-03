#One room is like masterming.
#Next one is like a maze
#Third one is under construction.Arithmetic game with timer.
from bc import*
from maze import*

class Engine(object):

    def __init__(self):
        self.a=Bcows()
        #a.guessing()
        self.b=Maze()
        #b.p_maze()
 
    def guessing(self):
        self.a.guessing()

    def mazing(self):
        self.b.p_maze()

b=Engine()        
b.guessing()
b.mazing()
