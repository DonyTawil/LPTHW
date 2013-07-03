from sys import argv
from os.path import exists

(script,from_file,to_file)= argv
print ("Copying from %s to %s."%(from_file,to_file))

put = open(from_file)
indata= (open(from_file).read())

input('>')
print (len(indata))
output = open(to_file,'w')
print (exists(to_file))
output.write(indata)


print ('All done here!')

put.close()
output.close()
print (put.closed)
print (output.closed)
