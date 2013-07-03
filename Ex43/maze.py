#Rather than making a maze I'm gonna make a pattern
#Main Pattern: up, right, up, up, left, down
#Postions are: r1, r2,    r3, r4,   r5, r6
##http://en.wikibooks.org/wiki/Think_Python/Classes_and_functions
from random import randint


class Maze(object):

    def __init__(self):
        self.dends=["Can't go that way.","Oh oh you hit a dead end!!","The road is blocked that way.","Rebroussez chemin","Halt no more road that way"]
        self.i=0
        self.n=20

    def mst(self):
        print("You can go up, or left.")
        action=input(">")
        if (action=="up"):
            return"r1"
        elif(action=="left"):
            return"w10"
        else:
            print("Does not compute")
            return"mst"   

    def r1(self):
        print("You can go up,right,down")
        action=input(">")
        if (action=="up"):
            return"w20"
        if  (action=="right"):
            return"r2"
        if (action=="down"):
            return"mst"
        else:
            print("Wrong input")
            return"r1"

    def w10(self):
        print("down,right")
        action=input(">")
        if (action=="down"):
            print(self.dends[randint(0,4)])
            self.i=self.i+1
            return"w10"
        if (action=="right"):
            return"r1"
        else:
            print("Wrong input")
            return"w10"        

    def w20(self):
        print("up,left,down")
        action=input(">")
        if (action=="up"):
            print(self.dends[randint(0,4)])
            self.i=self.i+1
            return"w20"
        if (action=="left"):
            print(self.dends[randint(0,4)])
            self.i=self.i+1
            return"w20"
        if (action=="down"):
            return"r1"
        else:
            print("Does not compute")
            return"w20"    

    def r2(self):
        print("Up,left")
        action=input(">")
        if (action=="up"):
            return"r3"
        if (action=="left"):
            return"r1"
        else:
            print("does not compute")
            return"r2"

    def r3(self):                      
        print("Up,down,right")
        action=input(">")
        if (action=="down"):
            return"r2"
        if (action=="up"):
            return"r4"
        if (action=="right"):
            return"w3"
        else:
            print("DOes not compute")
            return"r3"            

    def w3(self):
        print("right,left")
        action=input(">")
        if(action=="right"):
            return"w4"
        if(action=="left"):
            return"r3"
        else:
            print("Not computed")
            return"w3"

    def w4(self):
        print("left,up")
        action=input(">")
        if (action=="left"):
            return"w3"
        if (action=="up"):
            print(self.dends[randint(0,4)])
            self.i=self.i+1
            return"w4"
        else:
            print("Wrong input")     
            return"w4"

                                    
    def r4(self):
        print("down,left")
        action=input(">")
        if (action=="left"):
            return"r5"
        if (action=="down"):
            return"r3"
        else:
            print("Not computed")
            return"r4"

    def r5(self):
        print("down,right")
        action=input(">")
        if (action=="right"):
            return"r4"
        if (action=="down"):
            print("You won")    
                       

    def p_maze(self):

        pos="mst"
        while(self.i<=self.n):
            pos1=pos    #To know initial postion (read below).
            next=getattr(self,pos)
            pos=next()
            if(pos!=pos1):#If wrong input the numbers of moves left remains the same
                self.i=self.i+1
            print("You have made %d moves"%self.i)

        print("You lost.")
            
        
                                                
