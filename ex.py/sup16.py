from sys import argv

(script , filetarget) = argv
target = open(filetarget, 'w')
print ("now rewriting target file press any key to continue")
input("press any key to continue ")
print ("now creating text files to be written to computer")
L1 = input('for line 1:')
L2 = input('Line 2:')
target.write(L1)
target.write('\n')
target.write(L2)

print ("and now we read it=>")
target.close()
target2 = open(filetarget)
print (target2.read())
target2.close()
print (target2.closed)
print (target.closed)
