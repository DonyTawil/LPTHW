#Bulls and cows (mastermind)
#You have 15 chances to guess 4 digits btw(0-9) they are all diffrent
from random import randint

class Bcows(object):
    def __init__(self):
        c1=randint(0,9)
        c2=randint(0,9)
        c3=randint(0,9)
        c4=randint(0,9)
        while((c1==c2)or(c1==c3)or(c1==c4)):
            c1=randint(0,9)
        while((c2==c1)or(c2==c3)or(c2==c4)):
            c2=randint(0,9)
        while((c3==c1)or(c3==c2)or(c3==c4)):
            c3=randint(0,9)        
        self.c1=c1
        self.c2=c2
        self.c3=c3
        self.c4=c4
        self.code=[str(self.c1),str(self.c2),str(self.c3),str(self.c4)]
    
    def guessing(self):
        print(self.c1,self.c2,self.c3,self.c4)

        for g in range(0,16):
            b=0
            c=0
            g1=input(">")
            g2=input(">")
            g3=input(">")
            g4=input(">")
            print("end of input")

            g=[g1,g2,g3,g4]


            for i in range(0,4):
                if g[i]==self.code[i]:
                    b+=1 
            if b==4:
                print("You won")
                break
            

            for i in range(0,4):
                for j in range(0,4):
                    if ((j==i)or(g[i]==self.code[i])):
                        continue
                    if (g[i]==self.code[j]):
                        c+=1                                
                        break
            print("The number of cows that you have is %d"%c)
            print("The number of bulls is %d"%b)

            
