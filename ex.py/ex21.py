def add(a, b):
    print ("Adding %d + %d"%(a,b))
    return a + b

def subtract(a, b):
    print ("Subtracting %d - %d"%(a, b))
    return a -b

def multiply(a, b):
    print ("Multiplying %d * %d"%(a, b))
    return a * b

def divide(a, b):
    print ("Dividing %d / %d"%(a, b))
    return a / b

print ("Now doing math!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print ("Age: %d.\nHeight: %d.\nWeight: %d.\nIQ: %d"%(age,height,weight,iq))

print ("This is puzzle")

what = add(age, subtract(height, multiply(weight,divide(iq,2))))

print ("that result into", what)
