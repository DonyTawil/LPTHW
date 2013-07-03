def print_two(*args):
    (arg1,arg2)= args
    print ("arg1 is %s, arg2 is %s"%(arg1,arg2))

def print_two_again(arg1, arg2):
    print ("arg1_again is %s, arg2_again is %s"%(arg1, arg2))

def print_one(arg1):
    print ("the one and only argument is %s."%arg1)

def print_none():
    print ("I've got nothing.")

print_two("Hello","World!")
print_two_again("Hello","World again!")
print_one("Hi Everybody!")
print_none()
