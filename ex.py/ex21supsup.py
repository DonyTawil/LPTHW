#The numbers are 30,5,78,4,90,2,100,2,2
def Add(a,b,c):
    print ("starting calculation.")
    return a+b-c

def Mult(a,b):
    return a*b

def Div(a,b):
    return a/b

Math= (Add(30,5,- Add(78,-4,Mult(Mult(90,2),Div(Div(100,2),2)))))

print (Math)
